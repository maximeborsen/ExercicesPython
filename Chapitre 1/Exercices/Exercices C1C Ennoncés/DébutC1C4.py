import sys
def ChooseDestination():
    print("1 - Bruxelles\n2 - Mons\n3 - Nivelles \n4 - Charleroi")
    _destinationChoice = int(input("Entrez La destination que vous voulez atteindre :\n "))
    if _destinationChoice == 1:
        _destination = "Bruxelles"
    elif _destinationChoice == 2:
        _destination = "Mons"
    elif _destinationChoice == 3:
        _destination = "Nivelles"
    elif _destinationChoice == 4:
        _destination = "Charleroi"
    else :
        sys.exit("Erreur : la destination entrée est incorrecte !")
    print("Bien, vous avez choisi d'aller à " + _destination +".\n")
    return _destination

def ChoosePeriodOfTime():
    print("1 - Matin\n2 - Après-midi\n3 - Soir")  
    _timeChoice = int(input("Quand souhaitez vous partir ? "))
    if _timeChoice == 1:
        _time = "Matin"
    elif _timeChoice == 2:
        _time = "Après-midi"
    elif _timeChoice == 3:
        _time = "Soir"
    else :
        sys.exit("Erreur : période entrée n'est pas correcte !")
    print("Ok, vous avez choisi la période : " + _time + "\n")
    return _time

def displaytime(_time, _morning, _afternoon, _evening):
    if _time == "Matin":
        print("Votre train démarre à "+ _morning)
    elif _time == "Après-midi":
        print("Votre train démarre à " + _afternoon)
    elif _time == "Soir":
        print("Votre train démarre à "+ _morning)
        


destination= ChooseDestination()
time= ChoosePeriodOfTime()

if destination == "Bruxelles":
    displaytime(time, "10h33", "14h42", "19h02")
if destination=="Mons":
    displaytime(time, "9h05", "15h00", "18h30")
if destination== "Nivelles":
    displaytime(time, "8h34", "16h00", "20h00")
if destination== "Charleroi":
    displaytime(time, "7h30", "16h34", "21h00")

        
    