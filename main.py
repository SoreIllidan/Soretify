import requests

# Credenciales de la aplicación de Spotify
CLIENT_ID = "29bed310d7e941a482c165c3fb0ece73"
CLIENT_SECRET = "247c2bc1dcf34c58a6355647ba3a12e2"
USUARIO = "xi0b7334wqgxvmhj9mcit3tk4"

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


# Solicitud GET para buscar el álbum
# Obtener el ID del primer álbum encontrado
# URL para obtener información del álbum
# URL de búsqueda de álbum en Spotify
url_search = 'https://api.spotify.com/v1/search'
params = {
    'q': 'DeBÍ TiRAR MáS FOToS',  # Término de búsqueda
    'type': 'album',              # Buscar solo álbumes
    'limit': 1                    # Limitar la búsqueda a 1 resultado
}

response_access_token = requests.get(url_search, params=params, headers=headers)
id = response_access_token.json()['albums']['items'][0]['id']



# Solicitud GET para obtener información del álbum
url_search_album = f'https://api.spotify.com/v1/albums/{id}'
response_informacion_album = requests.get(url_search_album, params=params, headers=headers)
nombre_item_album= response_informacion_album.json()['tracks']['items'][4]['name']
# print(nombre_item_album)


# Solicitud GET para obtener información del usuario
url_info_usuario = f'https://api.spotify.com/v1/users/me'
response = requests.get(url_info_usuario, params=params, headers=headers)
imagen_usuario = response.json()['images']
seguidores_usuario = response.json()['followers']
email_usuario = response.json()['email']


# print(imagen_usuario)
# print("======================")
# print(seguidores_usuario)
print("======================")
print(email_usuario)
