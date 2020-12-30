import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '313b5aa711d44596b4308635c73e73dd'
client_secret = '1e9c0d2c879149f8abfc7ebffec40e8c'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)  # spotify object to access API


analysis = sp.audio_analysis('696DnlkuDOXcMAnKlTgXXK')
print(analysis['timbre'])

