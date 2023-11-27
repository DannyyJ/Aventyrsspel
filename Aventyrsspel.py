import random as rand
import time

class Itemm():
    def __init__(self, name, stre, heal):
        self.name = name
        self.stre = stre
        self.heal = heal




# I1 = Item("Katana", 12)
# I2 = Item("Kaktus", 1)
# I3 = Item("asdfgh", 999)

# [I1, I2, I3]

# I1.name
# I1.stre



def item():
    procent = rand.randint(1,100)
    if procent == 1:
        print("Du fick en Laserpistol")
        föremål = Itemm("Laserpistol", 50)
    elif procent == 2:
        print("Du fick ett lasersvärd")
        föremål = Itemm("Lasersvärd", 50)
    elif procent > 2 and procent <=12:
        print("Du fick en slägga")
        föremål = Itemm("Slägga", 23)
    elif procent > 12 and procent <=24:
        print("Du fick ett svärd")
        föremål = Itemm("Svärd", 20)
    elif procent > 24 and procent <=34:
        print("Du fick en Strids yxa")
        föremål =Itemm("Strids yxa", 25)
    elif procent > 34 and procent <= 54:
        print("Du fick en dolk")
        föremål =Itemm("dolk", 10)
    elif procent > 54 and procent <= 74:
        print("Du fick bandage")
        föremål = Itemm("Bandage", 0, 2)
    elif procent > 74 and procent <= 89:
        print("Du fick en Hälsedryck")
        föremål = Itemm("Hälsedryck", 0, 7)
    elif procent > 89 and procent <= 94:
        print("Du fick en katana")
        föremål = Itemm("Katana", 35)
    else:
        print("Hopsan, du fick tyvvär inget :(")
        föremål = None
        return föremål

class Monster():
    def __init__(self, hälsa, styrka, färg, monster_type):
        self.hälsa = hälsa
        self.styrka = styrka
        self.färg = färg
        self.monster_type = monster_type

def monster():
    monsters = []
    hälsa = rand.randint(2,10)
    styrka = rand.randint(4,10)
    färg = rand.choice(["blå", "grön", "gul"])

    monster_type_chans = rand.randint(1, 100)
    if monster_type_chans <= 35:
        monster_type = "Skeleton"
        styrka += 4
    elif monster_type_chans <= 20:
        monster_type = "Brute"
        styrka += 10
    else:
        monster_type = "Zombie"
        
    monsters.append(Monster(hälsa, styrka, färg, monster_type))
    return monsters
    

def strid(hs,monsters,hp,xp):
    print("Du mötte ett monster, hur ska det gå?!")
    time.sleep(2)
    
    for monster in monsters:
        print(f"Du mötte en {monster.färg} {monster.monster_type} med styrkan {monster.styrka} och din styrka är {hs}")

    # Här gör vi så att man kan fighta, flee, heala
        if hs > monster.styrka:
            print("Du vann")
            xp += 1
        elif hs == monster.styrka:
            print("Ni är lika starka så ingen av er förlorar")
        else:
            print("Du förlora")
            hp -= 1
        time.sleep(2)

    return hp, xp

def fälla(hp):
    bokstäver = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    bokstav = rand.choice(bokstäver)
    print("DU HAMNA I EN FÄLLA!")
    print(f"TRYCK: {bokstav}")
    start = time.time()
    svar = input()
    if svar.lower() == bokstav.lower():
        slut = time.time()
        print(slut-start)
        if slut - start < 3:
            print("DU KLARADE DET")
            time.sleep(2)
        else:
            print("Hopsan, Du hann inte och förlorade 1 hp")
            hp -= 1
            time.sleep(2)
    
    return hp


def dörr(x, hjältestyrka, hjältehp, inventory, hjältelv):
    Händelser = ["Fälla", "Monster", "Kista"]
    Vald_Händelse = rand.choice(Händelser)
    print(f"Bakom dörr {x}: {Vald_Händelse}")
    if Vald_Händelse == "Fälla":
        hjältehp = fälla(hjältehp)

        time.sleep(1)
    elif Vald_Händelse == "Monster":
        monsterstyrka= monster()
        hjältehp, hjältelv = strid(hjältestyrka, monsterstyrka, hjältehp, hjältelv)
    elif Vald_Händelse == "Kista":
        Vunnet = item()
        inventory.append(Vunnet)
    
        if len(inventory) == 4:
            print(
            f"""

            Du har fullt inventory. Vad gör du?
            1. Byt ut item
            2. Släng {Vunnet}

            
            """)
            fullinventory=int(input("Välj mellan 1 o 2: "))
            if fullinventory == 1: 
                for sak in inventory:
                    print(sak)
                x = int(input("Välj vilket föremål du vill ta bort(OBS! Du måste skriva rätt positon på listan) "))
                x -= 1
                borttagna=inventory.pop(x)
                inventory.append(Vunnet)
                print(f"Du har tagit bort itemet {borttagna} och nu har du dessa items: {inventory}")
                time.sleep(2)
            else: 
                print(f"Du slänger itemet {Vunnet}")
        else:
            inventory.append(Vunnet)
            time.sleep(2)
    
    return hjältehp, inventory, hjältelv
def main():
    heroname = input("Hej, vad heter du?\n")
    hjältenamn = {heroname}
    hjältehp = 10
    hjältestyrka = rand.randint(4,8)
    inventory = []
    hjältelv = 1
    

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
                    hjältehp, inventory, hjältelv = dörr(1, hjältestyrka, hjältehp, inventory, hjältelv)
                elif dörrval == "2":
                    hjältehp, inventory, hjältelv = dörr(2, hjältestyrka, hjältehp, inventory, hjältelv)
                elif dörrval == "3":
                    hjältehp, inventory, hjältelv = dörr(3, hjältestyrka, hjältehp,inventory, hjältelv)
                else:
                    print(f"dörr {dörrval} finns inte. Välj dörr 1, 2 eller 3!")

        elif val == "2":
            #Lägg till att se inventory
            print(
                """
                Du öppnade din ryggsäck.
                1. Visa föremål
                2. Släng bort item
                3. Stäng ryggsäck
                """)
            itemval = input("")
            if itemval == "1":
                #iterera genom lista mha for-loop
                for sak in inventory:
                    print(sak)
                
                time.sleep(2)
            elif itemval == "2":
                for sak in inventory:
                    print(sak)
                x = int(input("Välj vilket föremål du vill ta bort(OBS! Du måste skriva rätt positon på listan) "))
                x -= 1
                borttagna=inventory.pop(x)
                print(f"Du har tagit bort itemet {borttagna} och nu har du dessa items {inventory}")
                time.sleep(2)
            elif itemval == "3":
                pass
        elif val == "3":
            print(f"Ditt hp är {hjältehp} \nDin styrka är {hjältestyrka}\nDin level är {hjältelv}")
            time.sleep(2)
        elif val == "4":
            exit("Du avslutar spelet")
        else:
            print("Välj 1, 2, 3 eller 4!")
main()