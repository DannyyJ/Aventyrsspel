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

heroname = input("Hej, vad heter du?\n")
def main():
    
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
            4. Avsluta spelet
            
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