import requests

# Credenciales de la aplicación de Spotify
CLIENT_ID = "29bed310d7e941a482c165c3fb0ece73"
CLIENT_SECRET = "247c2bc1dcf34c58a6355647ba3a12e2"
PLAYLIST_ID = "6GoCv4D28ouddWei5yYOFq"

params = {
    'q': 'DeBÍ TiRAR MáS FOToS',  # Término de búsqueda
    'type': 'album',              # Buscar solo álbumes
    'limit': 1                    # Limitar la búsqueda a 1 resultado
}

# URL para obtener el token de acceso
url = 'https://accounts.spotify.com/api/token'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
data = {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
}

# Solicitud POST para obtener el token de acceso
# Obtener el token de acceso del JSON de respuesta
auth_response = requests.post(url, headers=headers, data=data)
access_token = auth_response.json().get('access_token')
headers = {'Authorization': f'Bearer {access_token}'}


url_info_usuario_lista_reproducción = f'https://api.spotify.com/v1/playlists/{PLAYLIST_ID}'
response_info_playlist = requests.get(url_info_usuario_lista_reproducción, params=params, headers=headers)
item_playlist = response_info_playlist.json()


for item in item_playlist['tracks']['items']:
    print(item['track']['name'])


print("Cantidad de canciones en la playlist:", item_playlist['tracks']['total'])