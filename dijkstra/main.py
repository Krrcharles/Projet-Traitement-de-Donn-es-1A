from importation import *
from traitement import *
import pandas as pd
from dijkstra import *

df = Import("data", "tarifs-tgv-inoui-ouigo.csv").read()

#print(df.head())

proc = Traitement(df, "Gare origine - code UIC", "Gare destination - code UIC", "Prix minimum")

df = proc.df



g = proc.graph()
d = Dijkstra(g, 71116000)

print(g[71116000])

print(d.chemin_partout())

