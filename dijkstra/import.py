# Importation des données

import os
import pandas as pd


class Import:
    """Importation d'une base de données.

    Cette classe permet d'importer une base de données
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
        >>> trajets_sncf = Import("Data", "referentiel-gares-voyageurs.csv")
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
                        "Le nom de l'extension du fichier ne correspond pas à son format. cause erreur:"
                        + exception
                    )

            case "xlsx":
                try:
                    data = pd.read_excel(file_path)
                except Exception as exception:
                    print(
                        "Le nom de l'extension du fichier ne correspond pas à son format. cause erreur:"
                        + exception
                    )

            case ".xls":
                try:
                    data = pd.read_excel(file_path)
                except Exception as exception:
                    print(
                        "Le nom de l'extension du fichier ne correspond pas à son format. cause erreur:"
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


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
