class Camarade:
    def __init__(self, prenom, age, nom):
        self.prenom = prenom
        self.age = age
        self.nom = nom
    
    def informations(self):
        print("Je suis {0} {1} et j'ai {2} ans.".format(self.prenom, self.nom, self.age))

    def est_plus_grand_que(self, other):
        if self.age < other.age:
            print("{0} est plus petit.e que {1}".format(self.prenom, other.prenom))
        elif self.age > other.age:
            print("{0} est plus grand.e que {1}".format(self.prenom, other.prenom))
        else:
            print("{0} a le même âge que {1}".format(self.prenom, other.prenom))
    
    def __lt__(self, other):
        return self.age < other.age

def afficher_liste(liste):
    print("[", end='')
    for i, elt in enumerate(liste):
        print("\"{0}\"".format(elt.prenom), end='')
        if i != len(liste) - 1:
            print(", ", end='')
    print("]")

def tri_camarades(liste):
    liste.sort()

if __name__ == "__main__":
    Tanguy = Camarade("Tanguy", 20, "Segarra")
    Garance = Camarade("Garance", 21, "Gourdel")
    Maya = Camarade("Maya", 20, "El Gemayel")

    Tanguy.est_plus_grand_que(Garance)
    Garance.est_plus_grand_que(Tanguy)
    Tanguy.est_plus_grand_que(Tanguy)

    liste_camarades = [Tanguy, Garance, Maya]

    afficher_liste(liste_camarades)
    tri_camarades(liste_camarades)
    afficher_liste(liste_camarades)