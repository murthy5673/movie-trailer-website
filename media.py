import webbrowser
class Movie():
    def __init__(self, movie_title,movie_storyline,poster_image,trailer_youtube,movie_rating,movie_desc,movie_director):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.movie_rating=movie_rating
        self.movie_desc=movie_desc
        self.movie_director = movie_director
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
