from user import User
import json

user = User("Ann")
user.add_movie("Spiderman HomeComing", "Fiction")
user.add_movie("Iron man 3", "Fiction")
user.add_movie("Bad Boys 2", "Action")
user.add_movie("Just Go With It", "Comedy")

with open("users.txt", 'w') as f:
    json.dump(user.user_json(), f)


# user = User.load_from_file("Ann.txt")
# print("{}\n {}".format(user.name, user.movies))

# user = User("Jon")
# user.add_movie("Heros", "Action")
# user.add_movie("Triple Frontiers", "Adventure")
# user.add_movie("Jumanji", "Action")
# user.add_movie("Now You See Me", "Thriller")
# user.save_to_file()



# user.delete_movie("Bad Boys 2")
# print(user)
# print("Movie List: {}".format(user.movies))


# user.delete_movie("Iron man 3")
# print(user)
# print("Movie List: {}".format(user.movies))

# print("Watched: {}".format(user.watched_movies()))
