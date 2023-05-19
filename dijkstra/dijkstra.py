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
    dataf : pandas.DataFrame
        Le dataframe contenant les données du graphe.
    colonne_noeud_depart : int
        L'indice de la colonne contenant les nœuds de départ.
    colonne_noeud_arrivee : int
        L'indice de la colonne contenant les nœuds d'arrivée.
    colonne_distance : int
        L'indice de la colonne contenant les distances entre les nœuds.
    """

    def __init__(self, dataf, colonne_noeud_depart, colonne_noeud_arrivee,
                 colonne_distance):

        for i in dataf[colonne_distance]:
            if not isinstance(i, (float, int)):
                raise TypeError("""Les poids associés aux arrêtes ne sont
                    pas tous des nombres réels""")
            if i < 0:
                raise ValueError("""Les poids associés aux arrêtes ne sont
                    pas tous des réels strictement positifs""")

        self.dataf = dataf
        self.colonne_noeud_depart = colonne_noeud_depart
        self.colonne_noeud_arrivee = colonne_noeud_arrivee
        self.colonne_distance = colonne_distance

    def graph(self):
        """Crée un graphe représentant les nœuds et les distances entre eux.

        Retour :
        --------
        dict :
            Le graphe représenté sous forme de dictionnaire.
        """
        df_grouped = self.dataf.groupby([self.colonne_noeud_depart])
        graphe = {}
        for noeud, data in df_grouped:
            graphe[noeud] = list(zip(data[self.colonne_noeud_arrivee],
                                     data[self.colonne_distance]))
        return graphe

    def chemin_partout(self, source):
        """Trouve le plus court chemin pour une multitude de destinations
          atteignables.

        Renvoie pour chaque destination ateignable à partir du point de départ
        -c'est à dire s'il existe un chemin reliant le point de départ et la
        destination- une liste contenant les points dans l'ordre du passage du
        chemin ainsi que le coût minimal associé au trajet. Si le point n'est
        pas ateignable, renvoie 'Pas de trajet'.

        Parameters
        ----------
        source : str / int
            noeud de départ nécessairement contenu dans le graphe

        Returns
        -------
        {noeud : [[noeud,...],distance],...} : dict
            renvoie un dictionnaire dont les clés sont représentés par des
            noeuds et les valeurs une liste comportant le plus court chemin
            et son coût si le noeud est atteignable sinon le
            string 'Pas de trajet'
        """
        if source not in self.dataf[self.colonne_noeud_depart]:
            raise ValueError("'source' est isolée")

        graphe = self.graph()
        marques = []  # Contiendra le nom des sommets visités
        # Distance minimale trouvée pour chaque valeur dès le départ
        distances = {sommet: (None, 2**30) for sommet in
                     set(self.dataf[self.colonne_noeud_depart]).union(
                     set(self.dataf[self.colonne_noeud_arrivee]))}
        # Sommet d'origine (None par défaut), distance
        distances[source] = 0  # On initialise la distance du départ
        # Nombre de sommets du graphe, longueur du dictionnaire
        selection = source
        coefficient = 0

        while len(marques) < len(graphe) and selection is not None:
            # On marque la 'selection'
            marques.append(selection)
            # On parcours les voisins de 'selection'
            for voisin in graphe[selection]:
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

            minimum = (None, 2**30)
            for sommet in graphe:
                if sommet not in marques and distances[sommet][1] < minimum[1]:
                    minimum = (sommet, distances[sommet][1])
            # puis il devient notre nouvelle 'selection'
            selection, coefficient = minimum

        dict_parcours = {}
        for sommet in graphe:
            if sommet != source:
                parcours = [sommet]
                intermediaire = sommet
                if distances[sommet][1] == 2**30:
                    dict_parcours[sommet] = 'Pas de trajet'

                else:  # Parcourt le graphe à l'envers pour obtenir le chemin
                    while intermediaire != source:
                        intermediaire = distances[intermediaire][0]
                        parcours.append(intermediaire)

                    parcours.reverse()
                    dict_parcours[sommet] = [parcours,
                                             distances[sommet][1]]

        return dict_parcours

    def chemin_destination(self, source, destination):
        """Trouve le plus court chemin pour une destination
          atteignable donnée.

        Renvoie pour une destination atteignable à partir du point de départ
        -c'est à dire s'il existe un chemin reliant le point de départ et la
        destination- une liste contenant les points dans l'odre de passage
        du chemin ainsi que le coût minimal associé au trajet.

        Parameters
        ----------
        source : str / int
            noeud de départ nécessairement contenu dans le graphe
        destination : str
            noeud d'arrivée qui doit être contenu dans le graphe

        Returns
        -------
        [[noeud,...],distance] : list
            liste comportant le plus court chemin et son coût.
        """
        if destination == source:
            raise ValueError("'destination' est la source")
        if source not in self.dataf[self.colonne_noeud_depart]:
            raise ValueError("'source' est isolée")
        if destination not in self.dataf[self.colonne_noeud_arrivee]:
            raise ValueError("'destination' n'est pas atteignable")

        graphe = self.graph()
        marques = []  # Contiendra le nom des sommets visités
        # Distance minimale trouvée pour chaque valeur dès le départ
        distances = {sommet: (None, 2**30) for sommet in
                     set(self.dataf[self.colonne_noeud_depart]).union(
                     set(self.dataf[self.colonne_noeud_arrivee]))}
        # Sommet d'origine (None par défaut), distance
        distances[source] = 0  # On initialise la distance du départ
        # Nombre de sommets du graphe, longueur du dictionnaire
        selection = source
        coefficient = 0

        while len(marques) < len(graphe) and selection is not None:
            # On marque la 'selection'
            marques.append(selection)
            # On parcours les voisins de 'selection'
            for voisin in graphe[selection]:
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

            minimum = (None, 2**30)
            for sommet in graphe:
                if sommet not in marques and distances[sommet][1] < minimum[1]:
                    minimum = (sommet, distances[sommet][1])
            # puis il devient notre nouvelle 'selection'
            selection, coefficient = minimum

        parcours = [destination]
        longueur = distances[destination][1]
        sommet = destination

        if longueur == 2**30:
            return 'Pas de trajet'

        # Parcourt le graphe à l'envers pour obtenir le chemin
        while sommet != source:
            sommet = distances[sommet][0]
            parcours.append(sommet)
        parcours.reverse()
        return [parcours, longueur]
