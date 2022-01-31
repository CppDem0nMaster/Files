"""Min Bil Klass"""

class Bil():
    """Klass Bil"""
    hjul = 4

    def __init__(self, bilinfo_1, radio, acceleration = 1, fwd = False):
        """Skapar attributer till bilen"""
        self.bilinfo_1 = bilinfo_1
        self.radio = radio
        self.acceleration = acceleration
        self.fwd = fwd

    def presentera_bil(self):
        """Presenterar bilen"""
        return f"Den här bilen är av modellen {self.bilinfo_1[0]} och kostar {self.bilinfo_1[1]} kr"

    def bränsletest(self):
        """Bränsle test"""
        if self.bilinfo_1[2] is True:
            print("Bilen har bränsle")
        else:
            print("Bilen har inget bränsle")

    def radio_test(self):
        """Radio för bilen"""
        if self.radio is False:
            svar = input("Vill du sätta på radio? skriv ja eller nej")
            if svar.lower() == "ja":
                andra_svar = input(
                  "Vilken kanal vill du lyssna på? skriv ett heltal mellan 90 till 110")
            else:
                print("Radion sattes inte på")
        else:
            andra_svar = input(
              "Din radio är på vilken kanal vill du lyssna på? skriv ett heltal mellan 90 till 110")
        print(f"Kanal FM {andra_svar} spelas")

    def acceleration_förändring(self):
        """Radio för bilen"""
        print(f"Din acceleration är {self.acceleration} meter per kvadrat sekund")
        self.acceleration = float(input("Vad är din nya acceleration?"))
        print("Uppdatering av acceleration är genomförd!")

    def aktivera_fdw(self):
        """Aktivera fyrhjulsdrift"""
        svar = input("Vill du aktivera fyrhjulsdrift? svara ja/nej:")
        if svar.lower() is True:
            self.fwd = True
            print("Nu kör vi!")
        else:
            print("Tråkigt tvåhulsdrift är på")
