#pip install imdbpy

import imdb

# IMDb class
ia = imdb.IMDb()

#search a person
people = ia.search_person('angelina')

#print person's name
people[0]

#search company
companies = ia.search_company('rko')

#print the company name
companies[0]


#search a movie
movies = ia.search_movie('matrix')

#search keywords
keywords = ia.search_keyword('dystopia')

#search movies that match a kewyword
movies = ia.get_keyword('dystopia')

# get a movie/person/company, if you already know the ID of the movie
movie = ia.get_movie('0309987')
person = ia.get_person('0000206')
company = ia.get_company('0017902')

# print the names of the directors of the movie
print('Directors:')
for director in movie['directors']:
    print(director['name'])

# print the genres of the movie
print('Genres:')
for genre in movie['genres']:
    print(genre)

# search for a person name
people = ia.search_person('Louis Garrel')
for person in people:
   print(person.personID, person['name'])

# get a movie and print its director(s)
the_dreamers = ia.get_movie('0309987')
for director in the_dreamers['directors']:
    print(director['name'])

# show all information that are currently available for a movie
print(sorted(the_dreamers.keys()))

# show all information sets that can be fetched for a movie
print(ia.get_movie_infoset())


# update a Movie object with more information
ia.update(the_dreamers, ['technical'])

# show which keys were added by the information set
print(the_dreamers.infoset2keys['technical'])

# print one of the new keys
print(the_dreamers.get('tech'))

#top 250 movies
top = ia.get_top250_movies()

#bottom 100 movies
bottom = ia.get_bottom100_movies()

# you can also search Adult movies
movies = ia.search_movie_advanced('Janine Loves Jenna', adult=True)

# to search for members of the cast:
movie = ia.get_movie('0075860')
actor = movie['cast'][6]
actor['name'] # will print the real name of the 6th actor on the cast list
actor.currentRole # will print the role of the 6th cast member
