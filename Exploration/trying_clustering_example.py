import itertools
import numpy as np
import spotipy
import spotipy.util
import Project.WebScrapeCharts as wsc
from spotipy.oauth2 import SpotifyClientCredentials

# Create your own Spotify app to get the ID and secret.
# https://beta.developer.spotify.com/dashboard/applications
cid = "6b39dcecc7094e78bb939b60c9313930"
secret = "3fda20db056f45c18fb136ad791933b3"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# Get the Spotify URIs of each of my saved songs.
scraper = wsc.WebScrapeCharts()
scraper.get_charts('global', 'daily')
uris = scraper.song_ids_array

# Function that returns the next n elements from the iterator. Used because
# Spotify limits how many items you can group into each of its API calls.
def grouper(n, iterable):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk

# Get the audio features of each of the URIs fetched above.
uris_to_features = {}
for group in grouper(50, uris):
    res = sp.audio_features(tracks=group)
    for item in res:
        uris_to_features[item['uri']] = item

FEATURE_VECTOR = [
    'acousticness',
    'danceability',
    'energy',
    'instrumentalness',
    'key',
    'loudness',
    'mode',
    'speechiness',
    'tempo',
    'valence'
]

def features_to_vector(item):
    return np.array([item[key] for key in FEATURE_VECTOR])

vectors = [(x[0], features_to_vector(x[1])) for x in uris_to_features.items()]


#############################################################

import sklearn.preprocessing

# Gets an X-matrix given data as 2-element tuples with IDs and vectors.
def get_x(values):
    return np.vstack([x[1] for x in values])

# Given an object with a .transform(), apply it to the data vectors.
def apply_transform(transformer, data):
    return [(x[0], transformer.transform(x[1].reshape(1, -1))) for x in data]

def train_and_apply(transformer, data):
    X = get_x(data)
    transformer.fit(X)
    return apply_transform(transformer, data)

scaled = train_and_apply(sklearn.preprocessing.StandardScaler(), vectors)


##############################################################

import sklearn.cluster

RUN_ON = scaled

# Select the 'elbow' and classify the tracks
NUM_CLUSTERS = 8
PLAYLIST_NAME_FMT = 'Version {}: Cluster {}'
VERSION = 6

model = sklearn.cluster.KMeans(n_clusters=NUM_CLUSTERS,
                               n_jobs=-1)
model.fit(get_x(RUN_ON))
classified = [(x[0], model.predict(x[1])[0]) for x in RUN_ON]

playlists = dict()
for cluster in range(NUM_CLUSTERS):
    playlists[cluster] = []

for song in classified:
    uri = song[0].split(':')[-1]
    clst = song[-1]
    for key in playlists:
        if key == clst:
            song = sp.track(f"spotify:track:{uri}")
            playlists[clst].append((song['name'], song['artists'][0]['name']))

for cluster in range(NUM_CLUSTERS):
    songlist = playlists[cluster]
    print(f"Cluster {cluster}")
    for song in songlist:
        print(song[0], '-----------', song[1])
    print(f"\n")



### Determining the optimal k value -> https://pythonprogramminglanguage.com/kmeans-elbow-method/

from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt

# k means determine k

X = get_x(RUN_ON)
distortions = []
K = range(1,15)
for k in K:
    kmeanModel = sklearn.cluster.KMeans(n_clusters=k).fit(X)
    kmeanModel.fit(X)
    distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])

# Plot the elbow
plt.figure()
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()

# Now convert the classified songs into some playlists.
# ids = []
# for cluster in range(NUM_CLUSTERS):
#     playlist_id = sp.user_playlist_create(USERNAME,
#                                           PLAYLIST_NAME_FMT.format(VERSION, cluster))['id']
#     ids.append(playlist_id)
#
# def get_all_classified_as(classified, item_class):
#     return [x[0] for x in classified if x[1] == item_class]
#
# for cluster in range(NUM_CLUSTERS):
#     tracks = get_all_classified_as(classified, cluster)
#     playlist = ids[cluster]
#     for group in grouper(100, tracks):
#         sp.user_playlist_add_tracks(USERNAME, playlist, group)

#####################################################################################

