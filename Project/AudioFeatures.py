import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class AudioFeatures():
    def __init__(self):
        self.features = dict()
        self.selected_features = ['danceability', 'energy', 'key', 'loudness', 'mode', \
                               'speechiness', 'acousticness', 'instrumentalness', 'valence', 'tempo']
        self.song_names = []

    def get_features(self, song_ids):
        cid = "5981b769c7664e4fbb62599aafb79173"
        secret = "0ec407bb50aa48aeab9c3b8224e0c6a8"

        client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        for id in song_ids:
            try:
                features_song = sp.audio_features(f"spotify:track:{id}")[0]

                if features_song is not None:
                    self.features[id] = list()
                    for feature in self.selected_features:
                        self.features[id].append(features_song[feature])
                else:
                    print(f'FEATURE ERROR -> id: {id}, has no features')

            except:
                #raise NameError
                print('Get Features Error')
                #return False

        return self.features

    def get_names(self, song_ids):
        cid = "5981b769c7664e4fbb62599aafb79173"
        secret = "0ec407bb50aa48aeab9c3b8224e0c6a8"

        client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        songs = []
        for id in song_ids:
            name = sp.track(f"spotify:track:{id}")
            songs.append((name['name'], name['artists'][0]['name']))

        self.song_names = songs

    def save_features(self,filename, song_ids):
        self.get_features(song_ids)
        with open(filename, 'a+') as af:
            for feature in self.features:
                af.write(f'{feature};{self.features[feature]}\n')

    def load_features(self, filename):
        if self.is_empty():
            with open(filename, 'r') as rf:
                for line in rf:
                    feature_array = line.strip('\n').split((';'))
                    feature_id, tail = feature_array
                    features = tail.strip('[').strip(']').split(',')
                    features_for_id = []
                    for feat_str in features:
                        features_for_id.append(float(feat_str))
                    self.features[feature_id] = features_for_id
            return self.features

    def is_empty(self):
        return len(self.features) == 0

# if __name__ == '__main__':
#     x = AudioFeatures()
#     x.get_features(['696DnlkuDOXcMAnKlTgXXK','3ZCTVFBt2Brf31RLEnCkWJ', '3U2imIBWN0BnTS516Lhjfr'])
#     print(x.features)
#     x.get_names(['696DnlkuDOXcMAnKlTgXXK', '3ZCTVFBt2Brf31RLEnCkWJ', '3U2imIBWN0BnTS516Lhjfr'])
#     print(x.song_names)
#

