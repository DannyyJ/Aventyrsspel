import random as rand

def item():
    procent = rand.randint(1,100)
    if procent == 1:
        print("Du fick en Laserpistol")
    elif procent == 2:
        print("Du fick ett lasersvärd")
    elif procent > 2 and procent <=12:
        print("Du fick en slägga")
    elif procent > 12 and procent <=24:
        print("Du fick ett svärd")
    elif procent > 24 and procent <=34:
        print("Du fick en battle axe")
    elif procent > 34 and procent <= 54:
        print("Du fick en dagger")
    elif procent > 54 and procent <= 74:
        print("Du fick 5 bandage")
    elif procent > 74 and procent <= 89:
        print("Du fick en Hälsedryck")
    elif procent > 89 and procent <= 94:
        print("Du fick en katana")
    else:
        print("Hopsan, du fick tyvvär inget :(")

def strid(hs,fs,hp):
    if hs > fs:
        print("Du vann")
    else:
        print("Du förlora")
        hp -= 1
    return hp


def main():
    heroname = input("Hej, vad heter du?\n")
    hjältenamn = {heroname}
    hjältehp = 10
    hjältestyrka = rand.randint(0,10)

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
                    pass
                elif Vald_Händelse == "Monster":
                    # Kalla på "def strid"
                    pass
                elif Vald_Händelse == "Kista":
                    # Kalla på "def kista"
                    pass
                
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