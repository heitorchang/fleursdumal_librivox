with open("librivoxlist.txt", encoding="utf-8") as inf, open("titlelist.py", 'w', encoding="utf-8") as outf:
    print("titles = [", file=outf)
    for line in inf:
        if line[0:3].isdigit() and line[3] == " ":
            print(f'"{line.strip()}",', file=outf)
