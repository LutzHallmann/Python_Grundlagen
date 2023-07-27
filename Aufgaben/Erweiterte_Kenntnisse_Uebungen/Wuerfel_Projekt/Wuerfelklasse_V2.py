

class Wuerfel():

    # Zuerst mal als Klassenvariablen
    INT_MinAugen = 1    # kleinste Augenzahl unseres Würfels
    INT_MaxAugen = 6    # höchste Augenzahl unseres Würfels
    INT_SummeAugenzahlWuerfe = 0

    def __init__(self, AnzahlWuerfe = 10):
        self._MinAugen = Wuerfel.INT_MinAugen
        self._MaxAugen = Wuerfel.INT_MaxAugen
        self._AnzahlWuerfe = AnzahlWuerfe

    # Wir geben dem Objekt die Chance, seine Eigenschaften
    # zu verändern
    # Zuerst muss der Getter definiert werden "@property"
    @property
    def MinAugen(self):
        return self._MinAugen

    @MinAugen.setter
    def MinAugen(self, MinAugen: int):
        self._MinAugen = MinAugen

    @property
    def MaxAugen(self):
        return self._MaxAugen

    @MaxAugen.setter
    def MaxAugen(self, Param: int):
        self._MaxAugen = Param

    def wuerfeln(self):
        import random
        random.seed()
        for _ in range(1, self._AnzahlWuerfe + 1):
            augenzahl = random.randint(self._MinAugen, self._MaxAugen)
            self.INT_SummeAugenzahlWuerfe += augenzahl
            print(augenzahl)
        return

    def durchschnitt(self):
        durchschnitt = self.INT_SummeAugenzahlWuerfe / self._AnzahlWuerfe
        return(f'Der Durchschnitt der geworfen Augenzahlen beträgt: {durchschnitt}')

    def summe(self):
        return(f'Summe aller Würfe ist: {self.INT_SummeAugenzahlWuerfe}')


OBJ_MyWuerfel = Wuerfel(6)  # Erzeugung des Objekts ohne Parameter

# Wir nutzen nun die Getter und Setter Methoden
# Welche Methode angesteuert wird, wird über den Parameter entschieden:
# Ist ein Parameter vorhanden -> Setter
# Ist kein Parameter vorhanden -> Getter
OBJ_MyWuerfel.MinAugen = 1
OBJ_MyWuerfel.MaxAugen = 6
print(OBJ_MyWuerfel.wuerfeln())
print(OBJ_MyWuerfel.summe())
print(OBJ_MyWuerfel.durchschnitt())