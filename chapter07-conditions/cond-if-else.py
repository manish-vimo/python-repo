movie_rating = float(input('Enter a rating number:')) 

print(f'The entered movie rating is: {movie_rating}')

if movie_rating > 8.5:
    print('The movie is awesome with {} rating and you should watch it.'.format(movie_rating))
else:
    print('The movie has merit to be watched with {} rating.'.format(movie_rating))