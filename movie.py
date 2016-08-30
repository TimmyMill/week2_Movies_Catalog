

class Movie:

    def __init__(self, title, year, rating, genre, length):
        self.title = title
        self. year = year
        self. rating = rating
        self.genre = genre
        self.length = length
    #     Stretch Goal Maybe Own/Want a movie

    def __repr__(self):
        self.str_repr = self.title
        return self.str_repr