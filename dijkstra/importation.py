# Importation des données
class Import:
    """Importation des données.

    Cette classe permet d'importer des données
    et de vérifier que le fichier associé soit lisible.

    Parameters
    ----------
    folder : str
    Nom du dossier à importer

    filename : str
    Nom du fichier à importer
    """

    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename

    def read(self):
        """Permet d'importer un fichier.

        La fonction read permet d'importer un fichier csv, excel (xls ou xlsx)
        ou json sous forme de DataFrame pandas. Elle vérifiera que le fichier
        à importer a une extension valable et le format correspondant.


        Returns
        -------
        pandas.core.frame.DataFrame
        DataFrame pandas contenant toutes les données du fichier importé.

        Examples
        --------
        >>> trajets_sncf = Import("data", "referentiel-gares-voyageurs.csv")
        >>> print(trajets_sncf.read().iat[0,2])
        87784793
        """

        file_path = os.path.abspath(os.path.join(self.folder, self.filename))

        match file_path[-4:]:
            case ".csv":
                try:
                    data = pd.read_csv(file_path, sep=";")
                except Exception as exception:
                    print(
                        "Le nom de l'extension du fichier ne correspond pas à son format. Cause erreur:"
                        + exception
                    )

            case "xlsx":
                try:
                    data = pd.read_excel(file_path)
                except Exception as exception:
                    print(
                        "Le nom de l'extension du fichier ne correspond pas à son format. Cause erreur:"
                        + exception
                    )

            case ".xls":
                try:
                    data = pd.read_excel(file_path)
                except Exception as exception:
                    print(
                        "Le nom de l'extension du fichier ne correspond pas à son format. Cause erreur:"
                        + exception
                    )

            case "json":
                try:
                    data = pd.read_json(file_path)
                except Exception as exception:
                    print(
                        "Le nom de l'extension du fichier ne correspond pas à son format. cause erreur:"
                        + exception
                    )

            case _:
                raise TypeError("Mauvaise extension")

        return data
    
    def fusion(self, folder2, filename2, clef1, clef2, type_fusion='inner'):
        """Permet de fusionner 2 fichiers.

        La fonction fusion permet de fusionner deux fichiers de types csv,
        excel (xls ou xlsx) ou json (les formats des fichiers étant éventuellement 
        distincts) sous forme d'un unique DataFrame pandas. Elle vérifiera 
        que les clefs permettant de fusionner les 2 fichiers existent.

        Parameters
        ----------
        folder2 : str
        Nom du dossier dans lequel se trouve le fichier à fusionner 
        (avec le fichier importé)

        filename2 : str
        Nom du fichier à fusionner (avec le fichier importé)

        clef1 : str
        Nom de la colonne en commun des fichiers à fusionner
        (pour le fichier 1)

        clef2 : str
        Nom de la colonne en commun des fichiers à fusionner
        (pour le fichier 2)

        type_fusion : str
        Type de fusion entre les deux fichiers (on utilisera ici 
        une jointure interne, "inner join" en anglais)

        Returns
        -------
        pandas.core.frame.DataFrame
        DataFrame pandas contenant les données fusionnées des 2 fichiers.
        """
        if clef2 is None:
            clef2 = clef1
        dataframe1 = self.read()
        dataframe2 = Import(folder2, filename2).read()
        if not isinstance(clef1, str):
            raise TypeError("La clef doit correspondre au nom d'une colonne du fichier 1.")
        if not isinstance(clef2, str):
            raise TypeError("La clef doit correspondre au nom d'une colonne du fichier 2.")
        
        if clef1 not in dataframe1.columns or clef2 not in dataframe2.columns:
            raise ValueError("Les clefs de fusion doivent être des colonnes des fichiers.")
        else:    
            return pd.merge(dataframe1, dataframe2, on=[clef1, clef2], how = type_fusion)
        

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)