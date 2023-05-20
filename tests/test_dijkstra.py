""" Tests sur le calcul du plus court chemin avec pytest """
import re
import pytest
from dijkstra.dijkstra import Dijkstra


@pytest.mark.parametrize('''dataf, colonne_noeud_depart, colonne_noeud_arrivee,
 colonne_distance, message_erreur, type_erreur''', [
  (),()])

def test_erreur_init_dijkstra(dataf, colonne_noeud_depart,
                              colonne_noeud_arrivee, colonne_distance,
                              message_erreur, type_erreur):
    with pytest.raises(type_erreur, match=re.escape(message_erreur)):
        Dijkstra(dataf, colonne_noeud_depart, colonne_noeud_arrivee,
                 colonne_distance)

dataf_ex =
colonne_noeud_depart_ex =
colonne_noeud_arrivee_ex =
colonne_distance_ex =

@pytest.mark.parametrize('source, message_erreur', [
  (),()])


def test_erreur_partout_dijkstra(source, message_erreur):
    with pytest.raises(ValueError, match=re.escape(message_erreur)):
        Dijkstra(dataf_ex, colonne_noeud_depart_ex, colonne_noeud_arrivee_ex,
                 colonne_distance_ex).chemin_partout(source)

@pytest.mark.parametrize('source, destination, message_erreur', [
  (),()])


def test_erreur_destination_dijkstra(source, destination, message_erreur):
    with pytest.raises(ValueError, match=re.escape(message_erreur)):
        Dijkstra(dataf_ex, colonne_noeud_depart_ex, colonne_noeud_arrivee_ex,
                 colonne_distance_ex).chemin_destination(source, destination)

@pytest.mark.parametrize('''dataf, colonne_noeud_depart, colonne_noeud_arrivee,
 colonne_distance, message_erreur, type_erreur''', [
([], 1),
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

def test_resultat_graph_dijkstra(dataf, colonne_noeud_depart,
                                 colonne_noeud_arrivee, colonne_distance,
                                 resultat):
    assert Dijkstra(dataf, colonne_noeud_depart, colonne_noeud_arrivee,
                    colonne_distance).graph() == resultat

@pytest.mark.parametrize('''dataf, colonne_noeud_depart, colonne_noeud_arrivee,
 colonne_distance, message_erreur, type_erreur''', [
  (),()])


def test_resultat_partout_dijkstra(source, resultat):
    assert Dijkstra(dataf_ex, colonne_noeud_depart_ex, colonne_noeud_arrivee_ex,
                    colonne_distance_ex).chemin_partout(source) == resultat

@pytest.mark.parametrize('''dataf, colonne_noeud_depart, colonne_noeud_arrivee,
 colonne_distance, message_erreur, type_erreur''', [
  (),()])


def test_resultat_destination_dijkstra(source, destination, resultat):
    assert (Dijkstra(dataf_ex, colonne_noeud_depart_ex, colonne_noeud_arrivee_ex,
                     colonne_distance_ex).chemin_destination(source, destination)
            == resultat)



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

source1 = 'Paris'
source2 = 'Ville A'
A = Dijkstra(graph2, source2)
print(A.chemin_partout())