"""Algorithme de Dijkstra permettant de trouver le plus court chemin
dans un graphe"""


class Dijkstra:
    """Algorithme du plus court chemin.

    Classe modélisant deux versions de l'algorithme de Dijkstra :
    la première calculant le plus court chemin entre le noeud de
    départ et tous les noeuds atteignables tandis que la deuxième
    se contente de trouver le plus court chemin avec une destination
    souhaitée et le noeud de départ.

    Parameters
    ----------
    graphe : {noeud : [(noeud,distance),...],...} dict
            modélisation par un dictionnaire dont les clés
            représentent des noeuds et dont les valeurs sont
            des listes contenant un tuple formé du noeud voisin
            et le coût associé au déplacement

    source : str
            noeud de départ nécessairement contenu dans le graphe
    """

    def __init__(self, graphe, source):

        if not isinstance(graphe, dict):
            raise TypeError("'graphe' n'est pas bien défini")

        if source not in graphe.keys():
            raise ValueError("'source' n'est pas dans le graphe")

        for i in graphe.values():
            for j in i:
                if not isinstance(j[1], (float, int)):
                    raise TypeError("""Les poids associés aux arrêtes ne sont
                    pas des nombres réels""")
                if j[1] < 0:
                    raise ValueError("""Les poids associés aux arrêtes ne sont
                    pas des réels strictement positifs""")

        self.graphe = graphe
        self.source = source

    def chemin_partout(self):

        """Trouve le plus court chemin pour une multitude de destinations
          atteignables.

        Renvoie pour chaque destination ateignable à partir du point de départ
        -c'est à dire s'il existe un chemin reliant le point de départ et la
        destination- une liste contenant les points dans l'ordre du passage du
        chemin ainsi que le coût minimal associé au trajet. Si le point n'est
        pas ateignable, renvoie 'Pas de trajet'.

        Returns
        -------
        {noeud : [[noeud,...],distance],...} : dict
            renvoie un dictionnaire dont les clés sont représentés par des
            noeuds et les valeurs une liste comportant le plus court chemin
            et son coût si le noeud est atteignable sinon le
            string 'Pas de trajet'
        """

        infini = 2**30
        marques = []  # Contiendra le nom des sommets visités
        # Distance minimale trouvée pour chaque valeur dès le départ
        distances = {sommet: (None, infini) for sommet in self.graphe}
        # Sommet d'origine (None par défaut), distance
        distances[self.source] = 0  # On initialise la distance du départ
        # Nombre de sommets du graphe, longueur du dictionnaire
        taille_graph = len(self.graphe)
        selection = self.source
        coefficient = 0

        while len(marques) < taille_graph and selection is not None:
            # On marque la 'selection'
            marques.append(selection)
            # On parcours les voisins de 'selection'
            for voisin in self.graphe[selection]:
                # voisin est le couple (noeud, poids)
                noeud = voisin[0]  # Le sommet qu'on parcourt
                poids = voisin[1]  # Le poids de selection au sommet
                if noeud not in marques:
                    # Pour chaque voisin non marqué,
                    # on compare coefficient + arête
                    # avec la distance du dictionnaire
                    if coefficient + poids < distances[noeud][1]:
                        # Si c'est plus petit, on remplace
                        distances[noeud] = (selection, coefficient + poids)
                    # On recherche le minimum parmi les non marqués

            minimum = (None, infini)
            for sommet in self.graphe:
                if sommet not in marques and distances[sommet][1] < minimum[1]:
                    minimum = (sommet, distances[sommet][1])
            # puis il devient notre nouvelle 'selection'
            selection, coefficient = minimum

        dict_parcours = {}
        for sommet in self.graphe:
            if sommet != self.source:
                parcours = [sommet]
                longueur = distances[sommet][1]
                intermediaire = sommet
                if longueur == infini:
                    dict_parcours[sommet] = 'Pas de trajet'

                else:  # Parcourt le graphe à l'envers pour obtenir le chemin
                    while intermediaire != self.source:
                        intermediaire = distances[intermediaire][0]
                        parcours.append(intermediaire)

                    parcours.reverse()
                    dict_parcours[sommet] = [parcours, longueur]

        return dict_parcours

    def chemin_destination(self, destination):

        """Trouve le plus court chemin pour une destination
          atteignable donnée.

        Renvoie pour une destination atteignable à partir du point de départ
        -c'est à dire s'il existe un chemin reliant le point de départ et la
        destination- une liste contenant les points dans l'odre de passage
        du chemin ainsi que le coût minimal associé au trajet.

        Parameters
        ----------
        destination : str
            point d'arrivée qui doit être contenu dans le graphe

        Returns
        -------
        [[noeud,...],distance] : list
            liste comportant le plus court chemin et son coût.

        Examples
        --------
        >>>
        """
        if destination == self.source:
            raise ValueError("'destination' est la source")

        if destination not in self.graphe.keys():
            raise ValueError("'destination' n'est pas dans le graphe")

        infini = 2**30
        marques = []  # Contiendra le nom des sommets visités
        # Distance minimale trouvée pour chaque valeur dès le départ
        distances = {sommet: (None, infini) for sommet in self.graphe}
        # Sommet d'origine (None par défaut), distance
        distances[self.source] = 0  # On initialise la distance du départ
        # Nombre de sommets du graphe, longueur du dictionnaire
        taille_graph = len(self.graphe)
        selection = self.source
        coefficient = 0

        while len(marques) < taille_graph and selection is not None:
            # On marque la 'selection'
            marques.append(selection)
            # On parcours les voisins de 'selection'
            for voisin in self.graphe[selection]:
                # voisin est le couple (noeud, poids)
                noeud = voisin[0]  # Le sommet qu'on parcourt
                poids = voisin[1]  # Le poids de selection au sommet
                if noeud not in marques:
                    # Pour chaque voisin non marqué,
                    # on compare coefficient + arête
                    # avec la distance du dictionnaire
                    if coefficient + poids < distances[noeud][1]:
                        # Si c'est plus petit, on remplace
                        distances[noeud] = (selection, coefficient + poids)
                    # On recherche le minimum parmi les non marqués

            minimum = (None, infini)
            for sommet in self.graphe:
                if sommet not in marques and distances[sommet][1] < minimum[1]:
                    minimum = (sommet, distances[sommet][1])
            # puis il devient notre nouvelle 'selection'
            selection, coefficient = minimum

        parcours = [destination]
        longueur = distances[destination][1]
        sommet = destination

        if longueur == infini:
            return 'Pas de trajet'

        # Parcourt le graphe à l'envers pour obtenir le chemin
        while sommet != self.source:
            sommet = distances[sommet][0]
            parcours.append(sommet)

        return [parcours.reverse(), longueur]
