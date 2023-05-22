df1 = Import("data", "tarifs-tgv-inoui-ouigo.csv").read()
df1 = df1.drop(["Gare origine", "Destination", "Profil tarifaire", "Prix maximum"], axis= 1)
df1 = df1.set_axis(["Transporteur", "Origine", "Destination", "Classe", "Prix"], axis= 1)


df2 = Import("data", "tarifs-ter-par-od.csv").read()
df2 = df2.drop(["Région", "Origine", "Destination", "Libellé tarif", "Type tarif"], axis= 1)
df2 = df2.set_axis(["Origine", "Destination", "Prix"], axis= 1)


df = pd.concat([df1, df2],ignore_index=True, sort=False)

print(df)


#print(g[71116000])
#print(d.graph()[71116000])
#print(d.graph()[87671008])  #provoque erreur car pas une clé (normal)
#print(d.chemin_partout(71116000))
#print(d.chemin_partout(87671008))  #cas de tarbes : erreur = 'source' est isolée (normal)
#print(d.chemin_destination(71116000,87671008))


