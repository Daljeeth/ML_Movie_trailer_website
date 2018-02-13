import webbrowser
class Movie():
    """ This class provides a way to store movie related information"""

    valid_ratings = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,
                    movie_user_rating, movie_duration, movie_launch_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.user_rating = movie_user_rating
        self.duration = movie_duration
        self.launch_date = movie_launch_date
        
    #Opens a widget to view the movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


    
