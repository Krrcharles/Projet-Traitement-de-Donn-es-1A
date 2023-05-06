# Exportation des données

import pandas as pd


class Export :
    """Exportation des données.

    Cette classe permet d'exporter le fichier de données traité au format voulu par l'utilisateur.

    Parameters
    ----------
    dataframe : pandas.core.frame.DataFrame
    DataFrame correspondant au fichier de données déjà traité

    """

    def __init__(self,dataframe,format) :
        self.dataframe = dataframe
        self.format = format
    
    def export(self) :
        """Permet d'exporter un fichier.

        La fonction export permet d'exporter un fichier csv, excel (xls ou xlsx)
        ou json initialement sous forme de DataFrame pandas. Elle vérifiera que
        le format voulu existe et puisse être créé à partir d'un DataFrame pandas.


        Returns
        -------
        fichier csv, json ou excel
        Fichier exporté.

        Examples
        --------
        >>> trajets_sncf = Import("Data", "referentiel-gares-voyageurs.csv")
        >>> print(trajets_sncf.read().iat[0,2])
        87784793
        """
        match self.format:
            case "csv":
                try:
                    return self.dataframe.to_csv()
                except Exception as exception:
                    print(
                        "Le nom de l'extension du fichier ne correspond pas à son format. Cause erreur :"
                        + exception
                    )

            case "xlsx":
                try:
                    return self.dataframe.to_excel()
                except Exception as exception:
                    print(
                        "Le nom de l'extension du fichier ne correspond pas à son format. Cause erreur :"
                        + exception
                    )

            case "xls":
                try:
                    return self.dataframe.to_excel()
                except Exception as exception:
                    print(
                        "Le nom de l'extension du fichier ne correspond pas à son format. Cause erreur :"
                        + exception
                    )

            case "json":
                try:
                    return self.dataframe.to_json()
                except Exception as exception:
                    print(
                        "Le nom de l'extension du fichier ne correspond pas à son format. cause erreur :"
                        + exception
                    )

            case _:
                raise TypeError("type d'exportation pas possible")

