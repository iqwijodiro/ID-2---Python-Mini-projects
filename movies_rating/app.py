import requests

def movie_rating(title):
    key = 'a50bd5c'
    endpoint = f'http://www.omdbapi.com/?apikey={key}&t={title}'

    resp = requests.get(endpoint)
    data = resp.json()

    if data['Response'] == 'True' and resp.status_code == 200:
        rating_points = data['imdbRating']
        return rating_points
    else:
        print('No se encontró esa pelicula')
        return None

def main():
    title = input('Escribe el nombre de la pelicula que quieres conocer el rating: ')
    rating_points = movie_rating(title)

    if rating_points is not None:
        print(f'La pelicula {title} tiene un rating de {rating_points}')
    else:
        print(f'No encontró el rating de {title}')

if __name__ == '__main__':
    main()