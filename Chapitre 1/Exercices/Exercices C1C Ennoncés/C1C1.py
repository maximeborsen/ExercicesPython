# Enoncé : Votre programme demandera la partie "heure" de l'heure à l'utilisateur et stockera la réponse dans une variable
# Ensuite, il demandera la partie "minute" de l'heure à l'utilisateur et stockera cette deuxième information dans une autre variable.
# Après recolte de ces informations, le programme écrira l'heure et les minutes que l'utilisateur a défini. Si l'heure n'est pas correctement encodée 
# (minutes supérieur à 59, heures supérieures à 24,...) alors le programme affichera plusieurs messages d'erreur du style "L'heure encodée est supérieur à 60" 
# pour faire comprendre les problèmes.
# Après ceci, quoi qu'il arrive, le programme souhaitera une bonne journée à l'utilisateur.

#region indice
# pour créer une condition on utilise le petit mot if suivi de la condition à respecter entre parenthèse suivi du signe deux points. A la ligne, avec une tabulation,
# on écrit ce que fait le programme si la condition est respectée.
#endregion

#region indice
# exemple de condition :
# if(condition):
#   JeFaisCeci()
#endregion

#region indice
# Une condition est une expression booléenne, le résultat ne peut être que true ou false, souvenez vous des cours théorique ! (>,<,>=,<=,==,or,and,not)
#endregion

#region indice

# Réflechissez au placement de chacune de vos actions, quelles sont les conditions pour qu'elles se déclanchent, si il faut en respecter une ou pas, et en fonction, placer votre
# action au bon endroit dans le code, attention à l'indentation !!! (tabulations)
#endregion

def Horloge():
    _heure = input('Heure:')
    _minutes = input('Minutes')
    print("Il est "+str(_heure)+"h"+str(_minutes)+", passez une bonne journée!")
    if(int(_heure)>23):
        print("L'heure est trop grande!")
    if(int(_minutes)>59):
        print('Les minutes sont trop grandes!')    
    if(int(_heure)<0):
        print("L'heure est trop grande!")
    if(int(_minutes)<0):
        print('Les minutes sont trop grandes!')  
Horloge()
