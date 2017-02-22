
from compo import *
import pandas as pd

"""On se donne une liste de joueurs dont les noms sont dans le fichier stat.xlsx """

player = ['Franketinho','Scalpi','Rocher','La tarantule','Sacha','Marius','Guillaume Bzb','Rozé','Virgile','Cyril']

"""On a au préalable converti le ficher stat au format CSV  pour pouvoir utiliser la bibliothèque pandas. La table est délimité par des espaces,
l'encodage de la table est Latin1 et pas utf-8 et on spécifie que les colonnes sont indéxes par le nom des joueurs suivant les lignes. Cette colonnes particulières
s'appelle Nom des joueurs """

table = pd.read_csv("stat.csv",delim_whitespace = True,encoding = "Latin1",index_col = 'Nom des joueurs')

#print(table['Virgile':'Virgile']['Niveau global'][0])

"""la fonction liste_de_joueur prend en argument une liste de string et renvoit une liste de joueur (cf fichier compo.py pour comprendre) en utilisant les données de chacun des joueurs """

def liste_de_joueur(liste):
    l = []
    for playeur in liste:
        l.append((playeur,float(table[playeur:playeur]['Niveau global'][0])))
    return(l)

#print(liste_de_joueur(player))
#print(compo(liste_de_joueur(player)))
