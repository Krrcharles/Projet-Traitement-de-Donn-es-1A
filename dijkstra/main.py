from importation import *
from traitement import *
import pandas as pd
from dijkstra import *

df = Import("data", "tarifs-tgv-inoui-ouigo.csv").read()

#print(df.head())

proc = Traitement(df, "Gare origine - code UIC", "Gare destination - code UIC", "Prix minimum")

df = proc.df



g = proc.graph()
d = Dijkstra(df, "Gare origine - code UIC", "Gare destination - code UIC", "Prix minimum")

#print(g[71116000])
#print(d.graph()[71116000])
#print(d.graph()[87671008])  #provoque erreur car pas une clé (normal)
#print(d.chemin_partout(71116000))
#print(d.chemin_partout(87671008))  #cas de tarbes : erreur = 'source' est isolée (normal)
#print(d.chemin_destination(71116000,87671008))


