import pandas as pd

class Traitement:
    
    def __init__(self, df, colonne_noeud_depart, colonne_noeud_arrivee, colonne_distatance):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("df doit être un dataframe pandas")
        self.df = df
        
        if isinstance(colonne_noeud_depart, str):
            self.colonne_noeud_depart = df.columns.get_loc(colonne_noeud_depart)
        
        if isinstance(colonne_noeud_arrivee, str):
            self.colonne_noeud_arrivee = df.columns.get_loc(colonne_noeud_arrivee)
            
        if isinstance(colonne_distatance, str):
            self.colonne_distatance = df.columns.get_loc(colonne_distatance)
        
        
    def ajouter_arrete(self, ligne):
        self.df.append(ligne)
        
    def supprimer_arrete(self, ligne):
        self.df.pop(ligne)
        
    def _graph(self):
        df_grouped = self.df.groupby([self.colonne_noeud_depart])
        graph = {}
        for name, group in df_grouped:
            adj_list = list(zip(group['noeud_arrivee'], group['distance']))
            graph[name] = adj_list