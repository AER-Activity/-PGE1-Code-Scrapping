import requests
from bs4 import BeautifulSoup

# Votre objectif est de récupérer les titres, la date de sortie, et le créateur de chaque film de la page et des les afficher dans la console sous forme d'objet.

# Exemple de résultat attendu :
# {
#     "titre": "Avatar : la voie de l'eau",
#     "date": "14 décembre 2022",
#     "realisateur": "James Cameron"
# }

# Pour récupérer les informations, vous devez utiliser la librairie BeautifulSoup.
# Pour vous aider je vous invite a lire la documentation suivante : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# Pour regarder a quoi ressemble l'html de la page, vous pouvez utiliser l'inspecteur d'élément de votre navigateur. (F12 sur chrome)
# Grace a l'inspecteur d'élement vous pourrez voir les élément qui vous intéressent et les classes ou id qui les identifient.


# Liste des url a scrapper
# ["https://www.allocine.fr/film/meilleurs/", "https://www.allocine.fr/film/aucinema/", "https://www.allocine.fr/film/attendus/"]
url = "URL A METTRE ICI"# time to Scrape

# Ligne de code qui fetch la page (fetch = faire une requête http a l'url pour récupérer le contenu de la page)
response = requests.get(url)

# Ligne de code qui parse le contenu de la page pour pouvoir le manipuler et récupérer les informations aisément
soup = BeautifulSoup(response.text, "html.parser")

# Ici vous devez récupérer les informations qui nous intéressent et les afficher dans la console sous forme d'objet.
# Des fonctions a utiliser grace a beautifulSoup ::
# soup.find_all
# soup.find
# Ces 2 fonction permettent de récupérer des éléments de la page en fonction de leur tag ou de leur classe ou id.
# Pour vous aider je vous invite a lire la documentation suivante : https://towardsdatascience.com/a-step-by-step-guide-to-web-scraping-in-python-5c4d9cef76e8

# Bonne chance !
