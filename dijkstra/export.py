# Exportation des données
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
        match self.format:
            case "csv":
                try:
                    return self.dataframe.to_csv()
                except Exception as exception:
                    print(
                        "Le nom de l'extension du fichier ne correspond pas à son format. Cause erreur:"
                        + exception
                    )

            case "xlsx":
                try:
                    return self.dataframe.to_xlsx()
                except Exception as exception:
                    print(
                        "Le nom de l'extension du fichier ne correspond pas à son format. Cause erreur:"
                        + exception
                    )

            case "xls":
                try:
                    return self.dataframe.to_xls()
                except Exception as exception:
                    print(
                        "Le nom de l'extension du fichier ne correspond pas à son format. Cause erreur:"
                        + exception
                    )

            case "json":
                try:
                    return self.dataframe.to_json()
                except Exception as exception:
                    print(
                        "Le nom de l'extension du fichier ne correspond pas à son format. cause erreur:"
                        + exception
                    )

            case _:
                raise TypeError("type d'exportation pas possible")




