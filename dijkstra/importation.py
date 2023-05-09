# Importation des données

import os
import pandas as pd


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
    
    def fusion(self, folder2, filename2, clef) :
        """Permet de fusionner 2 fichiers.

        La fonction fusion permet de fusionner deux fichiers de types csv,
        excel (xls ou xlsx) ou json (les formats des fichiers étant éventuellement 
        distincts) sous forme d'un unique DataFrame pandas. Elle vérifiera 
        que la clef permettant de fusionner les 2 fichiers existe.

        Parameters
        ----------
        folder2 : str
        Nom du dossier dans lequel se trouve le fichier à fusionner 
        (avec le fichier importé)

        filename2 : str
        Nom du fichier à fusionner (avec le fichier importé)

        clef : str
        Nom de la colonne en commun des fichiers à fusionner

        Returns
        -------
        pandas.core.frame.DataFrame
        DataFrame pandas contenant les données fusionnées des 2 fichiers.
        """
        dataframe1 = self.read()
        dataframe2 = Import(folder2, filename2).read()
        if not isinstance(clef, str):
            raise TypeError("La clef doit correspondre au nom d'une colonne des deux fichiers.")
        if clef not in dataframe1.columns.intersection(dataframe2.columns):
            raise ValueError("La clef n'est pas commune aux deux tables.")
        else:    
            return pd.merge(dataframe1, dataframe2, on=clef)
        
    def fusion_multiple(self, liste_folders, liste_filenames, liste_clefs):
        """Permet de fusionner plusieurs fichiers.

        La fonction fusion_multiple permet de fusionner plusieurs fichiers de 
        types csv, excel (xls ou xlsx) ou json (les formats des fichiers étant 
        éventuellement distincts) sous forme d'un unique DataFrame pandas. 
        Elle vérifiera que les listes de dossiers, fichiers et clefs sont de 
        même longueur.

        Parameters
        ----------
        liste_folders : list[str]
        Liste des noms de dossiers dans lequels se trouvent les fichiers à 
        fusionner (avec le fichier importé)

        liste_filenames : list[str]
        Liste des noms de fichiers à fusionner (avec le fichier importé)

        liste_clefs : list[str]
        Liste des noms de colonnes permettant les fusions successives

        Returns
        -------
        pandas.core.frame.DataFrame
        DataFrame pandas contenant les données fusionnées des fichiers.
        """
        if not isinstance(liste_folders, list):
            raise TypeError("La liste de dossiers doit être une instance de list")
        if not isinstance(liste_filenames, list):
            raise TypeError("La liste de fichiers doit être une instance de list")
        if not isinstance(liste_clefs, list):
            raise TypeError("La liste de clefs doit être une instance de list")
        
        if (len(liste_folders) != len(liste_filenames)) or (len(liste_folders) != len(liste_clefs)) :
            raise ValueError("La liste de dossiers, la liste de fichiers et la liste de clés de fusion doivent être de même longueur.")
        
        if len(liste_folders) == 0:
            return self.read()
        else:
            if len(liste_folders) == 1:
                return self.fusion(liste_folders[-1], liste_filenames[-1],liste_clefs[-1])
            else:
                Import(liste_folders[-1], liste_filenames[-1]).fusion_multiple(liste_folders.pop(), liste_filenames.pop(), liste_clefs.pop())

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)