from movie import Movie


class User:

    def __init__(self, name):
        self.name = name
        self.movies = []

    def get_user_name(self):
        return self.name

    def add_movie(self, name, genre):  # assuming movie is unwatched(False) by default
        movie = Movie(name, genre, False)
        self.movies.append(movie)
        return self.movies

    def delete_movie(self, name):
        new_movie = []
        for i in self.movies:
            if name in i.name:
                new_movie.append(i)
        self.movies = list(set(self.movies) - set(new_movie))

        # self.movies = list(filter(lambda i: name != i.name, self.movies))

    def watched_movies(self):
        # watched_movies_list = []
        # for movie in self.movies:
        #     if movie.watched is True:
        #         watched_movies_list.append(movie)
        # return watched_movies_list

        # filter(function, sequence)
        # sequence: sequence which needs to be filtered, it can
        # be sets, lists, tuples, or containers of any iterators
        movies_watched = list(filter(lambda movie: movie.watched, self.movies))
        return movies_watched

    def set_watched(self, name):
        for movie in self.movies:
            if name in movie.name:
                movie.watched = True

    def check_if_movie(self):
        for movie in self.movies:
            if len(movie < 1):
                return True
            else:
                return False

    def user_json(self):
        movie_list = []
        for movie in self.movies:
            movie_list.append(movie.movie_json())

        return {
            'name': self.name,
            'movies': movie_list

            # 'movies': [
            #     i.json() for i in self.movies
            # ]
        }

    @classmethod
    def from_json_file(cls, json_data):
        user = User(json_data['name'])

        movies = []
        for movie in json_data['movies']:
            movies.append(Movie.movie_from_json(movie))
        user.movies = movies

        return user

    def __repr__(self):
        return "User: {}".format(self.name)


""""
    def save_to_file(self):
        with open("{}.txt".format(self.name), 'w') as f:
            f.write(self.name + '\n')
            for movie in self.movies:
                f.write("{}, {}, {}\n".format(movie.name, movie.genre, str(movie.watched)))

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as f:
            content = f.readlines()
            username = content[0]
            movies = []
            for line in content[1:]:
                movie_data = line.split(',')  # name, genre, watched
                movies.append(Movie(movie_data[0], movie_data[1], movie_data[2]))

            user = User(username)
            user.movies = movies

            return user

"""
