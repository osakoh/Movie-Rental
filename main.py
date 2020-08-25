from user import User
import json

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

with open("subscribers.txt", 'r') as f:
    json_data = json.load(f)  # load as Python dictionary
    user = User.from_json(json_data)
    print(user.user_json())



# user = User.load_from_file("Ann.txt")
# print("{}\n {}".format(user.name, user.movies))

