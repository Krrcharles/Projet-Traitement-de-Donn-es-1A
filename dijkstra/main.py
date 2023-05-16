from importation import *
from traitement import *
import pandas as pd


df = Import("data", "tarifs-tgv-inoui-ouigo.csv").read()

#print(df.head())

proc = Traitement(df, "Gare origine - code UIC", "Gare destination - code UIC", "Prix minimum")

df = proc.df

# Initialisation du dictionnaire
graphe = {}

# Groupement des données par noeud de départ
grouped = df.groupby('Gare origine - code UIC')

for noeud, data in grouped:
    graphe[noeud] = list(zip(data['Gare destination - code UIC'], data['Prix minimum']))

print(graphe)

