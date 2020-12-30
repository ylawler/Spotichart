
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid ="6b39dcecc7094e78bb939b60c9313930"
secret = "3fda20db056f45c18fb136ad791933b3"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Then run your query
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

results = sp.audio_features("0Eq00PRTmts0eI1raaF1AW")[0]
print(results)
print(results["danceability"])
