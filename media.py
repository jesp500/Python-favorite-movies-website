class Movie():
    # Class which returns an object with a title, a poster,
    # a photo of the movie, the trailer, a synopsis and a brief
    # statement from the movie
    def __init__(
        self,
        title,
        poster_image_url,
        photo_movie,
        trailer_youtube_url,
        synopsis, slogan
    ):
        # initialize instance of class Movie
        self.title = title
        self.poster_image_url = poster_image_url
        self.photo_movie = photo_movie
        self.trailer_youtube_url = trailer_youtube_url
        self.synopsis = synopsis
        self.slogan = slogan  # the statement to be put into the carousel
