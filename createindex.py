import os

def createindex():
    with open("dist/index.html", 'w', encoding="utf-8") as idx:    
        print("""<!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="style.css">
            <title>Les fleurs du mal</title>
        </head>
        <body>
            <pre>
    LES FLEURS DU MAL

      by
        
    CHARLES BAUDELAIRE


Poem numbers follow <a href="https://librivox.org/les-fleurs-du-mal-by-charles-baudelaire/">LibriVox's order</a>.        
    """, file=idx)

        print("Missing poems: ")
        with open("librivoxlist.txt", encoding="utf-8") as lst:
            for i, line in enumerate(lst):
                if os.path.exists(str(i) + ".txt"):
                    tokens = line.split()
                    num = int(tokens[0])
                    disp = str(num) + " " + " ".join(tokens[1:]) + "\n"
                    print(f"""<a href="{i}.html">{disp}</a>""", file=idx)
                else:
                    print(line, end="")

        print("""
 Credits:
        
 Text:

        <a href="http://www.gutenberg.org/ebooks/6099">Project Gutenberg</a>
        
        <a href="https://fleursdumal.org/alphabetical-listing">fleursdumal.org</a>
        
 Audio:

        <a href="https://librivox.org/les-fleurs-du-mal-by-charles-baudelaire/">LibriVox</a>

 Conversion scripts:

        <a href="https://github.com/heitorchang/fleursdumal_librivox">fleursdumal_librivox on GitHub</a>
        """, file=idx)
        print("</pre></body></html>", file=idx)
    print()
    print("End of createindex.")
