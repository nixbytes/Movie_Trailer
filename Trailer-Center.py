#!/usr/bin/python

import Udacity_Movies
import fresh_tomatoes

# added the movie poster pic in Posters folder
# the wiki link didn't display correctly so I added the folder
toy_story = Udacity_Movies.Movie(
    "Toy Story",
    "A story about a boy and his toys",
    "Posters/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

transformer_1 = Udacity_Movies.Movie(
    "Transformer 1",
    "The Autobots intend to use the AllSpark, the object\
     that created their robotic race",
    "Posters/Transformers.jpg",
    "https://www.youtube.com/watch?v=KrUhwet0ngg")

riddick_4 = Udacity_Movies.Movie(
    "Riddick",
    "Five years after Kyra's death, Riddick has become\
     increasingly uneasy in his role as Lord Marshall \
     of the Necromonger fleet.",
    "Posters/Riddick_poster.jpg",
    "https://www.youtube.com/watch?v=8VlV18mGeOI")

princess_mononoke = Udacity_Movies.Movie(
    "Princess Mononoke",
    "The story follows the young Emishi warrior Ashitaka's \
     involvement in a struggle between forest gods and the \
     humans who consume its resources.",
    "Posters/Princess_Mononoke_Japanese_Poster_(Movie).jpg",
    "https://www.youtube.com/watch?v=4OiMOHRDs14")

movie_list = (toy_story, transformer_1, riddick_4, princess_mononoke)
fresh_tomatoes.open_movies_page(movie_list)
