import json
import os

from user import User


# user = User("Ann")
# user.add_movie("Spiderman HomeComing", "Fiction")
# user.add_movie("Iron man 3", "Fiction")
# user.add_movie("Bad Boys 2", "Action")
# user.add_movie("Just Go With It", "Comedy")

# user = User("Jon")
# user.add_movie("Heros", "Action")
# user.add_movie("Triple Frontiers", "Adventure")
# user.add_movie("Jumanji", "Action")
# user.add_movie("Now You See Me", "Thriller")
# print(user.user_json())
# user.set_watched("Heros")
# print(user.user_json())
# user.set_watched("Now You See Me")
# print(user.user_json())


# with open("{}.txt".format(user.name), 'w') as f:
#     json_data = json.dumps(f)  # load as Python dictionary
#     user = User.from_json_file(json_data)
#     print(user.user_json())
# json.dump(user.user_json(), f)


# user = User.load_from_file("Ann.txt")
# print("{}\n {}".format(user.name, user.movies))

def menu():
    name = input("Enter your name: ").strip()
    filename = "{}.txt".format(name)

    # check if file exist
    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)  # loads contents of a file in the JSON format
        user = User.from_json_file(json_data)
    # if file doesn't exist create one
    else:
        user = User(name)

    print("\t\tWelcome, {}!".format(name.capitalize()))  # display a welcome message

    menu_options()  # display a list of options for the user to choose from
    user_input = int(input("Select from the menu: "))  # capture the users input and typecast into an integer

    while user_input != 0:
        if user_input == 1:  # add a movie
            movie_name = input("Enter movie name: ").strip()
            movie_genre = input("Enter movie genre: ").strip()
            user.add_movie(movie_name, movie_genre)

        elif user_input == 2:  # view list of movies
            if user.emptylist(user.movies):  # first check if the user has movies
                print("No movies yet, Enter (1) to add a movie!\n")
            else:
                for count, movie in enumerate(user.movies):
                    print("{})".format(count + 1))
                    print("Name: {}\nGenre: {}\nWatched: {}\n".format(movie.name, movie.genre, movie.watched))

        elif user_input == 3:  # set  movie as watched
            if user.emptylist(user.movies):  # first check if the user has movies
                print("No movies in the list.")
            else:
                movie_name = input("Enter the name of movie to set as watched: ").strip()
                user.set_watched(movie_name)

        elif user_input == 4:  # delete a movie
            if user.emptylist(user.movies):  # first check if the user has movies
                print("No movies in the list.")
            else:
                movie_name = input("Enter the name of movie to set as watched: ").strip()
                user.delete_movie(movie_name)

        elif user_input == 5:  # show watched movies
            if user.emptylist(user.watched_movies()):   # first check if the user has watched any movie
                print("No movies watched")
            else:
                for count, movie in enumerate(user.watched_movies()):
                    print("{})".format(count + 1))
                    print("Name: {}\nGenre: {}\nWatched: {}\n".format(movie.name, movie.genre, movie.watched))

        elif user_input == 6:  # save user profile
            with open(filename, 'w') as f:
                json.dump(user.user_json(), f)
            print("File saved successfully as '{}'".format(filename))

        menu_options()  # display a list of options for the user to choose from
        user_input = int(input("Select from the menu: "))


def file_exists(filename):
    return os.path.isfile(filename)  # checks if a file is in the current project directory


def menu_options():
    print("____________________________________\n"
          "¦____ Movie Rental Application ____¦\n"
          "| 1.     Add a movie               |\n"
          "| 2.     View list of movies       |\n"
          "| 3.     Set a movie as watched    |\n"
          "| 4.     Delete a movie            |\n"
          "| 5.     View watched movies       |\n"
          "| 6.     Save profile              |\n"
          "| 0.     Exit application          |\n"
          "|__________________________________|")


# if __name__ == '__main__':
menu()
