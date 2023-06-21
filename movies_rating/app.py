import requests

def movie_rating(title):
    key = 'https://www.omdbapi.com/apikey.aspx' #solicita tu key en este enlace
    endpoint = f'http://www.omdbapi.com/?apikey={key}&t={title}'

    resp = requests.get(endpoint)
    data = resp.json()

    # Validamos que la respuesta de la api sea correcta
    if data['Response'] == 'True' and resp.status_code == 200:
        rating_points = data['imdbRating'] # Asignamos la propiedad imdbRating al puntaje que manejaremos y lo devolvemos
        return rating_points
    else:
        print('No se encontró esa pelicula')
        return None

def main():
    title = input('Escribe el nombre de la pelicula que quieres conocer el rating: ') #Recibimos del usuario el titulo de la pelicula
    rating_points = movie_rating(title) #Se lo pasamos como parametro a la funcion de consulta

    if rating_points is not None:
        print(f'La pelicula {title} tiene un rating de {rating_points}')
    else:
        print(f'No encontró el rating de {title}')

if __name__ == '__main__':
    main()