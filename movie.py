class Movie:

    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return "Movie: {}".format(self.name)

    def movie_json(self):
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }

    #  Argument unpacking: passing a dictionary as a set of named parameters
    @classmethod
    def movie_from_json(cls, json_data):  # format: {'name': '...', 'genre': '...', 'watched': '...'}
        # return Movie(json_data['name'], json_data['genre'], json_data['watched'])
        return Movie(**json_data)

