import random as rand

def Item():
    procent = rand.randint(1,100)
    if procent == 1:
        print("Du fick en Laserpistol")
        föremål = "Laserpistol" 
    elif procent == 2:
        print("Du fick ett lasersvärd")
        föremål ="Lasersvärd"
    elif procent > 2 and procent <=12:
        print("Du fick en slägga")
        föremål = "Slägga"
    elif procent > 12 and procent <=24:
        print("Du fick ett svärd")
        föremål ="Svärd"
    elif procent > 24 and procent <=34:
        print("Du fick en Strids yxa")
        föremål ="Strids yxa"
    elif procent > 34 and procent <= 54:
        print("Du fick en dolk")
        föremål ="Dolk"
    elif procent > 54 and procent <= 74:
        print("Du fick 5 bandage")
        föremål = "Bandage"
    elif procent > 74 and procent <= 89:
        print("Du fick en Hälsedryck")
        föremål = "Hälsedryck"
    elif procent > 89 and procent <= 94:
        print("Du fick en katana")
        föremål = "Katana"
    else:
        print("Hopsan, du fick tyvvär inget :(")
        föremål = None
    return föremål

class Zombie():
    def __init__(self, styrka, färg):
        self.styrka = styrka
        self.färg = färg
def monster():
    return 5
    

def strid(hs,fs,hp):
    if hs > fs:
        print("Du vann")
    else:
        print("Du förlora")
        hp -= 1
    return hp

def dörr(x, hjältestyrka, hjältehp, inventory):
    Händelser = ["Fälla", "Monster", "Kista"]
    Vald_Händelse = rand.choice(Händelser)
    print(f"Bakom dörr {x}: {Vald_Händelse}")
    if Vald_Händelse == "Fälla":
        # Kalla på "def fälla"
        pass
    elif Vald_Händelse == "Monster":
        print("Du mötte ett monster, hur ska det gå?!")
        monsterstyrka= monster()
        strid(hjältestyrka, monsterstyrka, hjältehp)
    elif Vald_Händelse == "Kista":
        Vunnet=Item()
        inventory.append(Vunnet)
    
    return hjältehp, inventory
        
        

# def inventory(läggtill)
#     ryggsäck = []
#     apend.ryggsäck(läggtill)

def main():
    heroname = input("Hej, vad heter du?\n")
    hjältenamn = {heroname}
    hjältehp = 10
    hjältestyrka = rand.randint(5,10)
    inventory = []

    for i in range(100):
        hälsa = rand.randint(2,10)
        styrka = rand.randint(4,10)
        färg = rand.choice(["blå", "grön", "gul"])

        Ny_zombie = Zombie(styrka, färg)
        print(Ny_zombie.färg)
    

    while hjältehp >= 0:        
        print(
            """

            Vad vill du göra?
            1. Välj dörr
            2. Kolla ryggsäck
            3. Kolla stats
            4. Avsluta spel
            
            """)
    
        val = input("")
        if val == "1":                
            dörrval = " "
            while dörrval not in "123":
                print("Du ser 3 olika dörrar. Välj dörr 1, 2 eller 3")
                dörrval = input("")
                if dörrval == "1":
                    hjältehp, inventory = dörr(1, hjältestyrka, hjältehp, inventory)
                elif dörrval == "2":
                    hjältehp, inventory = dörr(2, hjältestyrka, hjältehp, inventory)
                elif dörrval == "3":
                    hjältehp, inventory = dörr(3, hjältestyrka, hjältehp,inventory)
                else:
                    print(f"dörr {dörrval} finns inte. Välj dörr 1, 2 eller 3!")

        elif val == "2":
            #Lägg till att se inventory
            itemval = " "
            while itemval not in "123":
                print(
            """

            Du öppnade din ryggsäck.
            1. Byt Item
            2. Släng bort item
            3. Stäng ryggsäck
            
            """)
                print(inventory)
                if itemval == "1":
                    pass
                elif itemval == "2":
                    pass
                elif itemval == "3":
                    pass
        elif val == "3":
            pass
        elif val == "4":
            exit("Du avslutar spelet")
        else:
            print("Välj 1, 2, 3 eller 4")

main()