import requests

USUARIO = "xi0b7334wqgxvmhj9mcit3tk4"

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
url_info_usuario = f'https://api.spotify.com/v1/users/{USUARIO}'
response_info_usuario = requests.get(url_info_usuario, params=params, headers=headers)
imagen_usuario = response_info_usuario.json()['images']
seguidores_usuario = response_info_usuario.json()['followers']
# email_usuario = response.json()['email']