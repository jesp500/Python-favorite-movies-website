# Favorites movie website #

This project is made out of three files: 

- fresh_tomatoes.py
- media.py
- entertainment_center.py

Media.py defines a class Movie, that creates an object containing several properties of a film: title, a poster, an image, a slogan from the movie, a synopsis and the code that will make part of the url to be put into the iframe which will be nested into an html file.

This html file will be created by the fresh_tomatoes.py file, which contains the html code. The entertainment_center.py creates three objects with my three favorite movies, then puts this classes into a list which will be the argument passed into the functions from the fresh_tomatoes.py file to make the html specific to those three movies.

In order to watch the html file, first run the entertainment_center.py on python and an html file will be created and open in your default browser.