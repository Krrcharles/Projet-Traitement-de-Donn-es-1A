# Tests sur l'importation des données avec pytest

from dijkstra.importation_donnees() import Import()

def test_importation_sncf() :
    assert Import("Data", "referentiel-gares-voyageurs.csv").read() == "87784793"

