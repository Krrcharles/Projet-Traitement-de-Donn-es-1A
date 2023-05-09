# Tests sur l'importation des données avec pytest
import pytest
from dijkstra.importation import Import

@pytest.mark.parametrize(
        'folder, filename, resultat_attendu',
        [("data", "tarifs-ter-par-od.csv", 87751321),
         ("data", "tarifs-tgv-inoui-ouigo.csv", 71116000)]
)

def test_importation_sncf(folder,filename,resultat_attendu):
    assert Import(folder, filename).read().iat[0,2] == resultat_attendu
