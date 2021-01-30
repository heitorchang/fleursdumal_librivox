# Generate an index file and individual pages for each poem.
# A poem has the text and mp3 file

# This script should produce in the dist/ folder,
# an index.html and an individual html file for each poem.

TEST_INDEX = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>My Title</title>
    </head>
    <body>
        <pre>
LES FLEURS DU MAL par CHARLES BAUDELAIRE

    <a href="test_lalbatros.html">L'ALBATROS</a>
        </pre>
    </body>
</html>
"""


TEST_LALBATROS = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>My Title</title>
    </head>
    <body>
        <pre>
  L'ALBATROS


  Souvent, pour s'amuser, les hommes d'équipage
  Prennent des albatros, vastes oiseaux des mers,
  Qui suivent, indolents compagnons de voyage,
  Le navire glissant sur les gouffres amers.

  A peine les ont-ils déposés sur les planches,
  Que ces rois de l'azur, maladroits et honteux,
  Laissent piteusement leurs grandes ailes blanches
  Comme des avirons traîner à côté d'eux.

  Ce voyageur ailé, comme il est gauche et veule!
  Lui, naguère si beau, qu'il est comique et laid!
  L'un agace son bec avec un brûle-gueule,
  L'autre mime, en boitant, l'infirme qui volait!

  Le Poète est semblable au prince des nuées
  Qui hante la tempête et se rit de l'archer;
  Exilé sur le sol au milieu des huées,
  Ses ailes de géant l'empêchent de marcher.
        </pre>

        <figure>
            <figcaption>LibriVox audio</figcaption>
            <audio controls src="fleursdumal_002_baudelaire_64kb.mp3" autoplay>
                Audio not supported.
            </audio>
        </figure>
    </body>
</html>
"""

