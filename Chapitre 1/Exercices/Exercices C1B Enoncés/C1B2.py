# Enoncé : Créez une fonction qui va dire bonjour à quelqu'un. Elle a un paramètre, le nom de la personne
# que le programme salue.
#  Essayez d'appeler la fonction de 4 manières différentes 
# et une fois avec un input 
#  stocké dans une variable.

#region indice
# 1) avec une string directement.
#endregion

#region indice
# 2) Avec une variable qui stocke une string
#endregion

#region indice
# 3) Avec un input direct à l'appel de la fonction
#endregion

#region indice

# 4) Avec le resultat d'un input stocké dans une variable 
#endregion
# Tu dois donner un parametre a ta fonction Mafonction()
def Mafonction (_nameInFunction):
    print("Hello "+_nameInFunction)

name= "George"
Mafonction(name)
name2= input("Entrez votre prénom : ")
Mafonction(name2)
Mafonction("Michel")
Mafonction(input("Quel est votre nom?"))