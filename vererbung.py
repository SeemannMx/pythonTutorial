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



# Hund ist ein Lebewesen
class Hund(Lebewesen):
    print("erzeuge eine Hund Klasse")
    beine = 4
    name ="some name"
    
    # überschreiben der Basisklasse
    def lebe(self):
        self.beine = 3


if __name__ == "__main__":
    
    # erzeuge einen Hund names rocky
    rocky = Hund()

    #direkter parameter Zugriff auf die Augen des Lebewesens
    print("Name: ",rocky.name, " | Augenanzahl: ", rocky.augen, " | Beine: ", rocky.beine )

    # ändere parameter Beine
    rocky.lebe()
    print("Name: ",rocky.name, " | Augenanzahl: ", rocky.augen , " | Beine: ", rocky.beine )

    print("")


