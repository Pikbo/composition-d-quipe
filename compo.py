"""On génère une équipe test. Il s'agit d'une liste de tuple. Les tuples comportent en position 0: le nom du joueur et en position 1: la note moyenne du joueur.
Ce type de liste sera appelé liste de joueur"""

joueur = [('frankette',5.625),('scalpi',5.2),('Roché',5.1875),('La Tarantule',4),('Sacha',6.75),('Hippo',8.08),('Guillaume bzb',6.5),('Rozé',7.66),('Verge',8.16),('Cyril',6.33)]

"""somme() est une fonction qui prend en argument une liste de tuple le même type de liste que la liste joueur précédente, et qui somme toutes les notes des joueurs """

def somme(liste):
    result = 0
    l = len(liste)
    if l == 0:
        return(0)
    else:
        for i in range(l):
            result = result + liste[i][1]
        return(result)

"""la fonction couple_proche prend en argument une liste de joueurs et trouve dans cette deux joueurs ayant les notes les plus proches possibles. Dans l'exemple de la liste joueur,
les deux joueurs les plus proche sont Roché et Scalpi """

def couple_proche(liste):
    couple = ('','')
    maxi = 10000
    l = len(liste)
    for i in range(l-1):
        for j in range(i+1,l):
            if abs(liste[i][1]-liste[j][1]) < maxi:
                couple = (liste[i],liste[j])
                maxi = abs(liste[i][1]-liste[j][1])
    return(couple)

print(couple_proche(joueur))

""" La fonction compo prend en argument une liste de joueurs et renvoie deux listes de joueurs le niveau de chacune des deux listes et la différence de niveau.
Tant que la liste joueurs est non vide je cherche dans cette liste avec la fonction couple_proche, deux joueurs ayant le plus proche niveau. Pour répartir ces deux joueurs(qu'on j1 et j2) dans les
équipes equipe1 et equipe2, je les répartie de tel façon que la différence de niveau entre les deux équipes en comptant ce deux nouveaux joueurs soit la plus petite possible.

A la fin de la boucle while, les équipes ne sont pas à priori équilibré car les deux derniers joueurs n'étaient sûrement pas d'un niveau proche. J'appelle diff, la différence de niveau des
deux équipes que je divise ensuite par 2. Je parcours ensuite les deux listes afin de trouver deux joueurs qui ont une différence de niveau suffisament proche de diff. Si le plus fort de ces
deux joueurs est dans l'équipe la plus forte je lui fais changer d'équipe avec l'autre joueur. Sinon je continue à parcourir la liste afin de trouver un tel couple."""

def compo(liste):
    equipe1 = []
    equipe2 = []
    joueurs = liste
    while joueurs != []:
        a = somme(equipe1)
        b = somme(equipe2)
        couple = couple_proche(joueurs)
        joueurs.pop(joueurs.index(couple[0]))
        joueurs.pop(joueurs.index(couple[1]))
        if abs((a + couple[0][1]) - (b +couple[1][1])) < abs((a + couple[1][1]) - (b + couple[0][1])) :
            equipe1.append(couple[0])
            equipe2.append(couple[1])
        else:
            equipe1.append(couple[1])
            equipe2.append(couple[0])
    diff = abs(somme(equipe1) - somme(equipe2))/2
    """return(equipe1,equipe2)"""
    if diff == 0:
        return(equipe1,equipe2)
    else:
        for i in range(5):
            for j in range(5):
                if abs(abs(equipe1[i][1]-equipe2[j][1]) - diff) < diff:
                    if somme(equipe1) > somme(equipe2) and equipe1[i][1] > equipe2[j][1]:
                        a = equipe1[i]
                        b = equipe2[j]
                        equipe1.pop(equipe1.index(a))
                        equipe1.append(b)
                        equipe2.pop(equipe2.index(b))
                        equipe2.append(a)
                        break
                    elif somme(equipe1) < somme(equipe2) and equipe1[i][1] < equipe2[j][1]:
                        a = equipe1[i]
                        b = equipe2[j]
                        equipe1.pop(equipe1.index(a))
                        equipe1.append(b)
                        equipe2.pop(equipe2.index(b))
                        equipe2.append(a)
                        break
    return(equipe1,somme(equipe1),equipe2,somme(equipe2),diff)

print(compo(joueur))
