def pre():
    print("")
    print("Vererbung in Python")
    print("--------------------------------------------------------")
pre()

# Vererbung von classen
class Lebewesen:
    augen = 2
    print("erzeuge eine Lebewesen Klasse mit ", augen, " Augen")
    
    # constructor
    def __init_(self):
        self.klasse = "Tier"
        
    # Funktion der Basisklasse
    def lebe(self):
        self.augen = 4

# extra Klassen für Mehrfachvererbung
class Haustier(Lebewesen):
    ohren = 2
class Tier:
    hatZaehne = 1
    
# Hund ist ein Lebewesen
class Hund(Haustier, Tier):
    print("erzeuge eine Hund Klasse")
    beine = 4
    name ="some name"
    
    # überschreiben der Basisklasse
    def lebe(self):
        self.beine = 3


# Main to start python 
if __name__ == "__main__":
    
    # erzeuge einen Hund names rocky
    rocky = Hund()

    #direkter parameter Zugriff auf die Augen des Lebewesens
    print("Name: ",rocky.name, " | Augenanzahl: ", rocky.augen, " | Beine: ", rocky.beine )

    # ändere parameter Beine
    rocky.lebe()
    print("Name: ",rocky.name, " | Augenanzahl: ", rocky.augen , " | Beine: ", rocky.beine )

    print("")
    
    print("Haustrier")
    print("---------")
    print("Name:  ", rocky.name)
    print("Augen: ", rocky.augen)
    print("Ohren: ", rocky.ohren)
    print("Beine: ", rocky.beine)
    print("Zähne: ", rocky.hatZaehne)
    


