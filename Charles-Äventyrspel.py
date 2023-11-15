import random as rand

class Zombie():
    def __init__(self, hälsa, styrka, färg):
        self.hälsa = hälsa
        self.styrka = styrka
        self.färg = färg

def Fälla():

def Strid():

def Kista():

def main():
    hjältenamn = "Lennart"
    hjältehp = 10
    hjältestyrka = rand.randint(8,10)

    for i in range(100):
        hälsa = rand.randint(2,10)
        styrka = rand.randint(4,10)
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

            def dörr1():
                Händelser = ["Fälla", "Monster", "Kista"]
                Vald_Händelse = rand.choice(Händelser)
                print(f"Bakom dörr 1: {Vald_Händelse}")

            def dörr2():
                Händelser = ["Fälla", "Monster", "Kista"]
                Vald_Händelse = rand.choice(Händelser)
                print(f"Bakom dörr 2: {Vald_Händelse}")

            def dörr3():
                Händelser = ["Fälla", "Monster", "Kista"]
                Vald_Händelse = rand.choice(Händelser)
                print(f"Bakom dörr 3: {Vald_Händelse}")

                if Vald_Händelse == "Fälla":
                    # Kalla på "def fälla"
                elif Vald_Händelse == "Monster":
                    # Kalla på "def monster"
                elif Vald_Händelse == "Kista":
                    # Kalla på "def kista"
                
            dörrval = " "
            while dörrval not in "123":
                print("Du ser 3 olika dörrar. Välj dörr 1, 2 eller 3")
                dörrval = input("")
                if dörrval == "1":
                    dörr1()
                elif dörrval == "2":
                    dörr2()
                elif dörrval == "3":
                    dörr3()
                else:
                    print(f"dörr {dörrval} finns inte. Välj dörr 1, 2 eller 3!")

        elif val == "2":
            pass
        elif val == "3":
            pass
        else:
            print("Välj 1, 2 eller 3!")

main()
    