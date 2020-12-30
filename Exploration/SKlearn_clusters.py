import sklearn.preprocessing
from sklearn.cluster import KMeans
import numpy as np
import spotipy
import spotipy.util
import Project.WebScrapeCharts as wsc
from scipy.spatial.distance import cdist
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

kmeans = KMeans(n_clusters=8)
keans.fit(x)
# error =[]
# for i in range(1,11):
#     kmeans =  KMeans(n_clusters= i)
#     kmeans.fit(x)
#     error.append(sum(np.min(cdist(x, kmeans.cluster_centers_, 'euclidean'), axis=1)) / x.shape[0])



