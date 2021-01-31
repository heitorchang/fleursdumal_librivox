with open("librivoxlist.py") as inf:
    for line in inf:
        if line[0:3].isdigit() and line[3] == " ":
            print(line)
