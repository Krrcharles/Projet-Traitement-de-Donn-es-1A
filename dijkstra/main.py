from importation import *
from traitement import *


df = Import("data", "tarifs-tgv-inoui-ouigo.csv").read()

print(df.head())

temp = Traitement()

#df = Traitement(df, "Gare origine - code UIC", "Gare destination - code UIC", "Prix minimum")


