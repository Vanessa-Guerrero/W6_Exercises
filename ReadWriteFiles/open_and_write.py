# creating a new file using open function and append parameter, then closing file
with open("about_me.txt", "a") as f:
    # Updated my file
    f.write('\nPerfect night out?: Eat at a new restaurant and go watch a movie')
