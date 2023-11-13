import random as rand


def item():
    procent = rand(1,100)
    if procent == 1:
        print("Du fick en Laserpistol")
    elif procent == 2:
        print("Du fick ett lasersvärd")

    elif procent > 2 and procent <=20:
    


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