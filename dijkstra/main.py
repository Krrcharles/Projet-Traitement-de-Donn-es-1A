from importation import *
from traitement import *
import pandas as pd


df = Import("data", "tarifs-tgv-inoui-ouigo.csv").read()

print(df.head())

df = Traitement(df, "Gare origine - code UIC", "Gare destination - code UIC", "Prix minimum")

#g = df.graph()

df.df.groupby(["Gare origine"])