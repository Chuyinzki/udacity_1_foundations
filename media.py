import webbrowser


class Movie:

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, image, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
