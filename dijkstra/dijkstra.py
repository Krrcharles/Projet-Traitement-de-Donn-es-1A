class Dijkstra:

    def __init__(self,graphe,source):
        if not isinstance(graphe,dict):
            raise TypeError("'graphe' n'est pas bien défini")
        if not (source in graphe.keys()):
            raise ValueError("'source' n'est pas dans le graphe")
        for i in graphe.values():
            for j in i:
                if not isinstance(j[1],float):
                    raise TypeError("Les poids associés aux arrêtes ne sont pas des nombres réels")
                if j[1]<0:
                    raise ValueError("Les poids associés aux arrêtes ne sont pas des réels strictement positifs")
                
         #graphe={noeud : [(noeud,distance),...],...}              
        
        self.graphe= graphe
        self.source= source

    def chemin_partout(self, infini=2**30):
        
        marques = []  # Contiendra le nom des sommets visités
        # Distance minimale trouvée pour chaque valeur dès le départ
        distances = {sommet: (None, infini) for sommet in self.graphe}
        # Sommet d'origine (None par défaut), distance
        distances[self.source] = 0  # On initialise la distance du départ
        # Nombre de sommets du graphe, longueur du dictionnaire
        taille_graph = len(self.graphe)
        selection = self.source
        coefficient = 0
        while len(marques) < taille_graph:
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
                    d = distances[noeud][1]
                    if coefficient + poids < d:
                        # Si c'est plus petit, on remplace
                        distances[noeud] = (selection, coefficient + poids)
                    # On recherche le minimum parmi les non marqués
            minimum = (None, infini)
            for sommet in self.graphe:
                if sommet not in marques and distances[sommet][1] < minimum[1]:
                    minimum = (sommet, distances[sommet][1])
 
            # puis il devient notre nouvelle 'selection'
            selection, coefficient = minimum

        dict_parcours={}
        for sommet in self.graphe :
            if sommet != self.source :
                parcours = [sommet]
                longueur = distances[sommet][1]
                # On parcours le graphe à l'envers pour obtenir le chemin
                while sommet != self.source:
                    sommet = distances[sommet][0]
                    parcours.append(sommet)
                parcours.reverse()
                dict_parcours[sommet]= [parcours, longueur]
 
        #{noeud : [[noeud,...],distance],...} Non optimisé 
        return dict_parcours
     
    
    def chemin_destination(self,destination,infini=2**30):
        if not (destination in self.graphe.keys()):
            raise ValueError("'destination' n'est pas dans le graphe")
        

        marques = []  # Contiendra le nom des sommets visités
        # Distance minimale trouvée pour chaque valeur dès le départ
        distances = {sommet: (None, infini) for sommet in self.graphe}
        # Sommet d'origine (None par défaut), distance
        distances[self.source] = 0  # On initialise la distance du départ
        # Nombre de sommets du graphe, longueur du dictionnaire
        taille_graph = len(self.graphe)
        selection = self.source
        coefficient = 0
        while len(marques) < taille_graph:
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
                    d = distances[noeud][1]
                    if coefficient + poids < d:
                        # Si c'est plus petit, on remplace
                        distances[noeud] = (selection, coefficient + poids)
                    # On recherche le minimum parmi les non marqués
            minimum = (None, infini)
            for sommet in self.graphe:
                if sommet not in marques and distances[sommet][1] < minimum[1]:
                    minimum = (sommet, distances[sommet][1])
 
            # puis il devient notre nouvelle 'selection'
            selection, coefficient = minimum

        sommet = destination
        parcours = [destination]
        longueur = distances[destination][1]
        # On parcours le graphe à l'envers pour obtenir le chemin
        while sommet != self.source:
            sommet = distances[sommet][0]
            parcours.append(sommet)
        parcours.reverse()
 
        # On renvoie le chemin le plus court et la longueur
        return [parcours, longueur]
        ### [[noeud,...],distance cumulée]
    
