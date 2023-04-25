import pandas as pd

data = pd.read_csv("data/tarifs-tgv-inoui-ouigo.csv", sep= ";")

print(data.iat[0,1])
print(data.head())