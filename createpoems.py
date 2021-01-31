import os
from titlelist import titles


def previdx(idx):
    idx -= 1
    while idx > 0:
        if os.path.exists(f"{idx}.txt"):
            return idx
        idx -= 1
    return 0
    
def nextidx(idx):
    idx += 1
    while idx < 152:
        if os.path.exists(f"{idx}.txt"):
            return idx
        idx += 1
    return 0
    

def createpoem(idx):
    try:
        fin = open(f"{idx}.txt", encoding="utf-8")
        poem = fin.read().strip()
        fin.close()
    except FileNotFoundError:
        return ""
    
    with open(f"dist/{idx}.html", 'w', encoding="utf-8") as idxf:
        previdxn = previdx(idx)
        nextidxn = nextidx(idx)

        print(f"""<!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="style.css">
            <title>{titles[idx]} - Les fleurs du mal</title>        
        </head>
        <body>
        <a href="index.html">Homepage</a><br><br>
""", file=idxf)
        if idx > 0:
            print(f"""<a href="{previdxn}.html">&lt;&lt; {titles[previdxn]}</a> &nbsp;&nbsp;&nbsp; """, file=idxf)
        if idx < 151:
            print(f"""<a href="{nextidxn}.html">{titles[nextidxn]} &gt;&gt;</a><br><br>""", file=idxf)
        print(f"""
                <figure>
            <audio controls src="fleursdumal_{str(idx).zfill(3)}_baudelaire_64kb.mp3">
                Audio not supported.
            </audio>
        </figure>""", file=idxf)

        print(f"<pre>{idx} ", file=idxf, end="")
        print(poem, file=idxf)
        print(f"""</pre>
        """, file=idxf)

        print("""<br><br><a href="index.html">Homepage</a><br><br>
""", file=idxf)
        if idx > 0:
            print(f"""<a href="{previdxn}.html">&lt;&lt; {titles[previdxn]}</a> &nbsp;&nbsp;&nbsp; """, file=idxf)
        if idx < 151:
            print(f"""<a href="{nextidxn}.html">{titles[nextidxn]} &gt;&gt;</a><br><br>""", file=idxf)
        
        print("<br><br></body></html>", file=idxf)

