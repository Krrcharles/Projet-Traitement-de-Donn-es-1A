""" Tests sur le calcul du plus court chemin avec pytest """
import re
import pytest
from dijkstra.dijkstra import Dijkstra


@pytest.mark.parametrize(
'graphe, source, message_erreur, type_erreur',[
({'Ville A': ['Ville B', 10.5, 'Ville C', 5.2],
'Ville B': [('Ville A', 10.5), ('Ville C', 3.1)],
'Ville C': [('Ville A', 5.2), ('Ville B', 3.1)]},
'Ville A', "'graphe' n'est pas bien défini", TypeError),
(['Ville A', [('Ville B', 10.5), ('Ville C', 5.2)],
'Ville B', [('Ville A', 10.5), ('Ville C', 3.1)],
'Ville C', [('Ville A', 5.2), ('Ville B', 3.1)]],
'Ville B', "'graphe' n'est pas bien défini", TypeError),
({'Paris': [('Lyon', 4), ('Rennes', 3)],
'Marseille': [('Lyon', 2), ('Rennes', 4),('Isnatabul')],
'Istanbul' : None ,
'Lyon': [('Marseille', 2),('Paris', 4), ('Rennes', 3)],
'Rennes': [('Lyon', 3), ('Marseille', 4),('Paris', 3)]},
'Lyon', "'graphe' n'est pas bien défini", TypeError),
({'Paris': [('Lyon', 4), ('Rennes', 3)],
'Marseille': [('Lyon', 2), ('Rennes', 4),('Isnatabul')],
'Ajaccio' : [],
'Lyon': [('Marseille', 2),('Paris', 4), ('Rennes', 3)],
'Rennes': [('Lyon', 3), ('Marseille', 4),('Paris', 3)]},
'Istanbul', "'source' n'est pas dans le graphe", ValueError),
(['Ville A', [('Ville B', 10.5), ('Ville C', 5.2)],
'Ville B', [('Ville A', 10.5), ('Ville C', 3.1)],
'Ville C', [('Ville A', 5.2), ('Ville B', 3.1)]],
5.2, "'source' n'est pas dans le graphe", ValueError),
(['Ville A', [('Ville B', 10.5), ('Ville C', 5.2)],
'Ville B', [('Ville A', '3'), ('Ville C', 3.1)],
'Ville C', [('Ville A', 5.2), ('Ville B', 3.1)]],
'Ville A', "Les poids associés aux arrêtes ne sont pas des nombres réels", TypeError),
(['Ville A', [('Ville B', 10.5), ('Ville C', 5.2)],
'Ville B', [('Ville A', -3), ('Ville C', 3.1)],
'Ville C', [('Ville A', 5.2), ('Ville B', 3.1)]],
'Ville A', "Les poids associés aux arrêtes ne sont pas des réels strictement positifs", ValueError)])

def test_erreur_partout_dijkstra(graphe, source, message_erreur, type_erreur):
    with pytest.raises(type_erreur, match=re.escape(message_erreur)):
        Dijkstra(graphe, source).chemin_partout()

@pytest.mark.parametrize(
'graphe, source, resultat_attendu',
[({'Ville A', [('Ville B', 10.5), ('Ville C', 5.2)],
'Ville B', [('Ville A', 10.5), ('Ville C', 3.1)],
'Ville C', [('Ville A', 5.2), ('Ville B', 3.1)]},'Ville A',
{'Ville B': [['Ville A', 'Ville C', 'Ville B'], 8.3], 'Ville C': [['Ville A', 'Ville C'], 5.2], 'Ville D': [['Ville A', 'Ville D'], 8.7]}),
({'Paris': [('Lyon', 4), ('Rennes', 3)],
'Marseille': [('Lyon', 2), ('Rennes', 4),('Isnatabul')],
'Ajaccio' : [],
'Lyon': [('Marseille', 2),('Paris', 4), ('Rennes', 3)],
'Rennes': [('Lyon', 3), ('Marseille', 4),('Paris', 3)]},'Marseille',
{'Paris': [['Marseille', 'Ville C', 'Ville B'], 8.3], 'Ville C': [['Ville A', 'Ville C'], 5.2], 'Ville D': [['Ville A', 'Ville D'], 8.7]}),
([2], 2),
([1, 2], 2),
([2, 3, 4], 24),
([-3, 6, 5], -90),
([0, 2, 4, 7, 12], 0),
([12, 12], 144),
([3, 3, 3], 27),
([2, 2, 2, 2, 2, 2], 64),
([1, 2, 3, 4, 5, 6], 720),
([1, -2, 3, -4, 5, -6], -720)]
)
def test_resultat_partout_dijkstra(graphe, source, resultat_attendu):
    assert Dijkstra(graphe, source).chemin_partout() == resultat_attendu

@pytest.mark.parametrize(
'graphe, source, destination, message_erreur',[
({'Ville A': ['Ville B', 10.5, 'Ville C', 5.2],
'Ville B': [('Ville A', 10.5), ('Ville C', 3.1)],
'Ville C': [('Ville A', 5.2), ('Ville B', 3.1)]},
'Ville A', 'Ville A', "'destination' est la source"),
({'Paris': [('Lyon', 4), ('Rennes', 3)],
'Marseille': [('Lyon', 2), ('Rennes', 4),('Isnatabul')],
'Ajaccio' : [],
'Lyon': [('Marseille', 2),('Paris', 4), ('Rennes', 3)],
'Rennes': [('Lyon', 3), ('Marseille', 4),('Paris', 3)]},
'Paris', 'Istanbul', "'destination' n'est pas dans le graphe"),
({'Paris': [('Lyon', 4), ('Rennes', 3)],
'Marseille': [('Lyon', 2), ('Rennes', 4),('Isnatabul')],
'Ajaccio' : [],
'Lyon': [('Marseille', 2),('Paris', 4), ('Rennes', 3)],
'Rennes': [('Lyon', 3), ('Marseille', 4),('Paris', 3)]},
'Paris', Marseille, "'destination' n'est pas dans le graphe")])

def test_erreur_destination_dijkstra(graphe, source, destination, message_erreur):
    with pytest.raises(ValueError, match=re.escape(message_erreur)):
        Dijkstra(graphe, source).chemin_destination(destination)

@pytest.mark.parametrize(
'graphe, source, destination, resultat_attendu',
[([], 1),
([1], 1),
([2], 2),
([1, 2], 2),
([2, 3, 4], 24),
([-3, 6, 5], -90),
([0, 2, 4, 7, 12], 0),
([12, 12], 144),
([3, 3, 3], 27),
([2, 2, 2, 2, 2, 2], 64),
([1, 2, 3, 4, 5, 6], 720),
([1, -2, 3, -4, 5, -6], -720)]
)

def test_resultat_destination_dijkstra(graphe, source, destination, resultat_attendu):
    assert Dijkstra(graphe, source).chemin_destination(destination) == resultat_attendu


graphe = {'Paris': [('Lyon', 4), ('Rennes', 3)],
            'Marseille': [('Lyon', 2), ('Rennes', 4)],
            'Istanbul' : [],
            'Lyon': [('Marseille', 2),('Paris', 4), ('Rennes', 3)],
            'Rennes': [('Lyon', 3), ('Marseille', 4),('Paris', 3)]}
graph2 = {
    'Ville A': [('Ville B', 10.5), ('Ville C', 5.2), ('Ville D', 8.7)],
    'Ville B': [('Ville A', 10.5), ('Ville C', 3.1)],
    'Ville C': [('Ville A', 5.2), ('Ville B', 3.1), ('Ville D', 6.8)],
    'Ville D': [('Ville A', 8.7), ('Ville C', 6.8)]
}

source = 'Paris'
source2 = 'Ville A'
A = Dijkstra(graph2, source2)
print(A.chemin_partout())