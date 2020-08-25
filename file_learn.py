from user import User

with open("subscribers.txt", 'r') as f:
    # f.write("This is my file")
    print(f.readlines())


"""
You don't have to 'close()' a file if it's read/written to using the 'with' operator
r: read from a file
w: write to a file
"""