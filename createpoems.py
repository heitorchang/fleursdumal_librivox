from titlelist import titles

def createpoem(idx):
    try:
        fin = open(f"{idx}.txt", encoding="utf-8")
        poem = fin.read().strip()
        fin.close()
    except FileNotFoundError:
        print(f"File {idx} not found.")
        return ""
    
    with open(f"dist/{idx}.html", 'w', encoding="utf-8") as idxf:    
        print("""<!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="style.css">
            <title>{titles[0]} - Les fleurs du mal</title>        
        </head>
        <body>
        <a href="index.html">Homepage</a><br><br>
""", file=idxf)
        if idx > 0:
            print(f"""<a href="{idx-1}.html">&lt;&lt; {titles[idx-1]}</a> *** """, file=idxf)
        if idx < 152:
            print(f"""<a href="{idx+1}.html">{titles[idx+1]} &gt;&gt;</a><br><br>""", file=idxf)

        print(f"<pre>{idx} ", file=idxf, end="")
        print(poem, file=idxf)
        print(f"""</pre>
        <figure>
            <audio controls src="fleursdumal_{str(idx).zfill(3)}_baudelaire_64kb.mp3">
                Audio not supported.
            </audio>
        </figure>
        """, file=idxf)
        print("</body></html>", file=idxf)


for i in range(4):
    createpoem(i)
