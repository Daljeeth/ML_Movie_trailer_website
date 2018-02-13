import webbrowser


#https://google.github.io/styleguide/pyguide.html?showone=Classes#Classes
#If a class inherits from no other base classes, explicitly inherit from object. This also applies to nested classes.
class Movie(object):
    """ This class provides a way to store movie related information"""

    """
    Initialize the movie instance.
    Arguments:
    movie_title: title of the movie
    movie_storyline: A breif about the movie
    poster_image: image of the movie poster
    trailer_youtube: movie trailer url from youtube
    movie_user_rating: user ratings from IMDB website for the movie
    movie_duration: duration of the movie
    movie_launch_date: Movies launch date
    Returns:
    None
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,
                    movie_user_rating, movie_duration, movie_launch_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.user_rating = movie_user_rating
        self.duration = movie_duration
        self.launch_date = movie_launch_date

    """ 
    Opens a widget to view the movie trailer
    Arguments:
    None
    Returns:
    None
    """   
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


    
