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
LES FLEURS DU MAL par CHARLES BAUDELAIRE
""", file=idx)
    
    with open("librivoxlist.txt", encoding="utf-8") as lst:
        for i, line in enumerate(lst):
            print(f"""<a href="{i}.html">{line}</a>""", file=idx)

    print("</pre></body></html>", file=idx)
