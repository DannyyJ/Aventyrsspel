import random as rand

class Zombie():
    def __init__(self, hälsa, styrka, färg):
        self.hälsa = hälsa
        self.styrka = styrka
        self.färg = färg

def main():
    hjältenamn = "Lennart"
    hjältehp = 10
    hjältestyrka = rand.randint(0,10)

    for i in range(100):
        hälsa = rand.randint(1,10)
        styrka = rand.randint(7,10)
        färg = rand.choice(["blå", "grön", "gul"])

        Ny_zombie = Zombie(hälsa, styrka, färg)
        print(Ny_zombie.färg)



    while hjältehp >= 0:        
        print(
            """

            Vad vill du göra?
            1. Välj dörr
            2. Kolla ryggsäck
            3. Kolla stats
            
            """)
        
        val = input("")

        if val == "1":
            pass
        elif val == "2":
            pass
        elif val == "3":
            pass
        else:
            print("Välj 1, 2 eller 3!")

main()
    