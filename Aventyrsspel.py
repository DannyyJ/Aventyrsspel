import random as rand
import time

class Itemm():
    def __init__(self, name, stre, heal):
        self.name = name
        self.stre = stre
        self.heal = heal
        self.equipped = False

class Hjälte():
    def __init__(self, name, health, strength, inventory, level):
        self.name = name
        self.health = health
        self.strength = strength
        self.inventory = inventory
        self.level = level

# Art:
svärd_art = """ """
f = open("svärd.txt", "r")
for rad in f.readlines():
    svärd_art += rad

laserpistol_art = """ """
f = open("laserpistol.txt", "r")
for rad in f.readlines():
    laserpistol_art += rad

lasersvärd_art = """ """
f = open("lasersvärd.txt", "r")
for rad in f.readlines():
    lasersvärd_art += rad

slägga_art = """ """
f = open("slägga.txt", "r")
for rad in f.readlines():
    slägga_art += rad

stridsyxa_art = """ """
f = open("stridsyxa.txt", "r")
for rad in f.readlines():
    stridsyxa_art += rad

dolk_art = """ """
f = open("dolk.txt", "r")
for rad in f.readlines():
    dolk_art += rad

bandage_art = """ """
f = open("bandage.txt", "r")
for rad in f.readlines():
    bandage_art += rad

hälsedryck_art = """ """
f = open("hälsedryck.txt", "r")
for rad in f.readlines():
    hälsedryck_art += rad

katana_art = """ """
f = open("katana.txt", "r")
for rad in f.readlines():
    katana_art += rad


def item():
    procent = rand.randint(1,100)
    if procent == 1:
        print(laserpistol_art)
        print("Du fick en Laserpistol")
        föremål = Itemm("Laserpistol", 50, 0)
    elif procent == 2:
        print(lasersvärd_art)
        print("Du fick ett lasersvärd")
        föremål = Itemm("Lasersvärd", 50, 0)
    elif procent > 2 and procent <=12:
        print(slägga_art)
        print("Du fick en slägga")
        föremål = Itemm("Slägga", 3, 0)
    elif procent > 12 and procent <=24:
        print(svärd_art)
        print("Du fick ett svärd")
        föremål = Itemm("Svärd", 4, 0)
    elif procent > 24 and procent <=34:
        print(stridsyxa_art)
        print("Du fick en Strids yxa")
        föremål =Itemm("Strids yxa", 4, 0)
    elif procent > 34 and procent <= 54:
        print(dolk_art)
        print("Du fick en dolk")
        föremål =Itemm("dolk", 1, 0)
    elif procent > 54 and procent <= 74:
        print(bandage_art)
        print("Du fick bandage")
        föremål = Itemm("Bandage", 0, 1)
    elif procent > 74 and procent <= 89:
        print(hälsedryck_art)
        print("Du fick en Hälsedryck")
        föremål = Itemm("Hälsedryck", 0, 4)
    elif procent > 89 and procent <= 94:
        print(katana_art)
        print("Du fick en katana")
        föremål = Itemm("Katana", 5, 0)
    else:
        print("""
⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⠿⠿⠿⢿⣿⣷⣶⣶⣶⣦⣤⣤⣤⣤⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⣶⣦⠀⣶⣤⣤⣤⣤⣍⣉⣉⣉⡙⠛⠛⠛⠛⠏⣰⣿⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⡿⢠⣿⣿⣿⣿⣿⣿⣿⣿⠻⣿⣿⣿⣿⣿⣆⠸⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡇⢸⣿⣿⣿⣿⣿⣿⣿⡏⠀⠹⠟⠙⣿⣿⣿⠄⢻⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠊⣉⡉⢋⣩⡉⠻⠛⠁⣾⣀⣴⡀⢛⡉⢠⣷⠈⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣼⣿⣿⣿⣿⣿⣷⣿⠀⢿⣿⣿⣿⡿⢁⠚⠛⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠤⠾⠿⣿⡿⠛⣿⣿⣿⣿⣿⣷⣦⣌⣉⣉⣠⣾⡷⠂⣠⠀⠀⠀⠀
⠀⠀⠀⣿⢰⣶⣶⣶⣦⠀⠀⣤⣌⣉⠉⣉⡙⠛⠛⠛⠻⠟⢁⣴⣾⣿⠀⠀⠀⠀
⠀⠀⠀⣿⣆⠻⣿⣿⢇⣸⠀⣯⢉⣿⠀⣿⣿⣿⣿⣿⣷⠀⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⣿⣿⣷⡔⠐⣾⣿⠀⠛⠚⠿⠀⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⠿⠋⠀⠀⠀⠀
⠀⠀⠰⣦⡄⠀⠀⠈⠉⠉⠉⠉⠛⠛⠛⠛⠻⠿⠿⠿⠿⠀⠛⢁⣀⡀⠲⠖⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀
 """)
        print("""Hopsan, du fick tyvvär inget :( 
              
              Men du plockade med dig en värdelös planka
        
              """)
        föremål = Itemm("planka", 0, 0)
    
    return föremål

class Monster():
    def __init__(self, hälsa, styrka, färg, monster_type):
        self.hälsa = hälsa
        self.styrka = styrka
        self.färg = färg
        self.monster_type = monster_type

def monster():

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
        
    return Monster(hälsa, styrka, färg, monster_type)
    

def strid(hs,monster,hp,xp):

    print("Du mötte ett monster, hur ska det gå?!")
    time.sleep(2)
    
    print(
        f"""
        
        Du mötte en {monster.färg} {monster.monster_type} med styrkan {monster.styrka} och din styrka är {hs}

        """)
    time.sleep(2)

    print("1. FIGHT")
    print("2. FLY")



    strid_pågår = True

    while strid_pågår:
        stridval = input("")
        
        if stridval == "1":
            if hs > monster.styrka:
                print("Du vann")
                xp += 1
                break
            elif hs == monster.styrka:
                print("Ni är lika starka så ingen av er förlorar")
                break
            else:
                print("Du förlora")
                hp -= 1
                break

        elif stridval == "2":
        # FLY
            print("Du flydde från striden.")
            break
        else:
            print("Välj 1 eller 2")
        
    time.sleep(2)
    return hp, xp
    
    
def fälla(hp):
    bokstäver = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    bokstav = rand.choice(bokstäver)
    print(""" 
          
⠀⠀⢠⠀⠀⣾⡆⠀⠀⣠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢀⡀⠀⠀⠀⡄⠀⠀⠀⠀
⠀⠀⣾⣆⣼⣿⣧⣤⣴⣿⣇⠀⢀⣾⠀⠀ ⢀⣆⠀⠀⣸⣧⠀⠀⢰⣷⠀⠀⡀⠀
⠀⣸⡟⠋⠉⠉⠉⠙⠛⠻⠿⣿⣿⠟⢀⡀⠘⣿⣶⣶⣿⣿⣶⣶⣾⣿⣤⣼⡇⠀
⠀⣿⠁⠀⣼⠀⠀⠀⠀⠀⠀⠀⠈⠀⠛⠛⠀⠛⠉⠉⠉⠉⠉⠉⠉⠉⠛⢿⣇⠀
⠀⢻⣧⣴⣿⠀⠀⠀⣰⠀⠀⠀⢶⣶⣶⣶⣶⣤⠀⠀⠀⠀⠀⠀⢀⣇⠀⢸⣿⠀
⠀⠈⠻⣿⣿⣤⣀⣼⣿⠀⠀⠀⡀⠉⣉⠉⠉⠁⠀⠀⢠⣇⠀⠀⢸⣿⣤⣼⠇⠀
⠀⠀⠀⠀⠙⠻⢿⣿⣿⣤⣀⣾⡇⠀⠻⠀⢠⣧⠀⠀⣼⣿⣤⣴⣿⣿⠿⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⠟⠀⣶⣶⡄⢸⣿⣿⣿⡿⠿⠟⠛⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

""")
    print("DU HAMNA I EN FÄLLA!")
    print(f"TRYCK: {bokstav}")
    start = time.time()
    svar = input()
    if svar.lower() == bokstav.lower():
        slut = time.time()
        if slut - start < 1.5:
            print(f"DU KLARADE DET PÅ: {slut-start}")
            time.sleep(2)
        else:
            print("Hopsan, Du hann inte och förlorade 1 hp")
            hp -= 1
            time.sleep(2)
    
    return hp

def dörr(x, hjältestyrka, hjälte):
    Händelser = ["Fälla", "Monster", "Kista"]
    Vald_Händelse = rand.choice(Händelser)
    print(f"Bakom dörr {x}: {Vald_Händelse}")
    if Vald_Händelse == "Fälla":
        hjälte.health = fälla(hjälte.health)

        time.sleep(1)
    elif Vald_Händelse == "Monster":

        valt_monster= monster()
        
        hjälte.health, hjälte.level = strid(hjältestyrka, valt_monster, hjälte.health, hjälte.level)
    elif Vald_Händelse == "Kista":
        Vunnet = item()
        while True:
            if len(hjälte.inventory) == 4:
                print(
                f"""
        while True:
            if len(hjälte.inventory) == 4:
                print(
                f"""

                Du har fullt inventory. Vad gör du?
                1. Byt ut item
                2. Släng {Vunnet.name}
                Du har fullt inventory. Vad gör du?
                1. Byt ut item
                2. Släng {Vunnet.name}

                
                """)
                val = (input("Välj mellan 1 o 2: "))
                try:
                    val = int(val)
                    if val == 1:
                        print("Dina items:")
                        # enumerate räknar inventory och gör så att det printas ut som alternativ att välja mellan
                        for i, sak in enumerate(hjälte.inventory, 1):
                                print(f"{i}. {sak.name}")
                        x = int(input("Välj vilket föremål du vill ta bort (OBS! Du måste skriva rätt position på listan): "))
                        try: 
                            x = int(x)
                            if 1 <= x <= len(hjälte.inventory):
                                x -= 1
                                borttagna = hjälte.inventory.pop(x)
                                hjälte.inventory.append(Vunnet)
                                print(f"Du har bytit ut ett item för itemet {borttagna.name}")
                                time.sleep(2)
                                break
                            else:
                                print("Ange en giltig position.")
                        except ValueError:
                            print("Ange en giltig position.")
                    elif val == 2:
                        print(f"Du slänger itemet {Vunnet.name}")
                        break
                    else:
                        print("Välj mellan 1 eller 2.")
                except ValueError:
                    print("Ange en giltig siffra.")
            else:
                hjälte.inventory.append(Vunnet)
                time.sleep(2)
                break
                
                """)
                val = (input("Välj mellan 1 o 2: "))
                try:
                    val = int(val)
                    if val == 1:
                        print("Dina items:")
                        # enumerate räknar inventory och gör så att det printas ut som alternativ att välja mellan
                        for i, sak in enumerate(hjälte.inventory, 1):
                                print(f"{i}. {sak.name}")
                        x = int(input("Välj vilket föremål du vill ta bort (OBS! Du måste skriva rätt position på listan): "))
                        try: 
                            x = int(x)
                            if 1 <= x <= len(hjälte.inventory):
                                x -= 1
                                borttagna = hjälte.inventory.pop(x)
                                hjälte.inventory.append(Vunnet)
                                print(f"Du har bytit ut ett item för itemet {borttagna.name}")
                                time.sleep(2)
                                break
                            else:
                                print("Ange en giltig position.")
                        except ValueError:
                            print("Ange en giltig position.")
                    elif val == 2:
                        print(f"Du slänger itemet {Vunnet.name}")
                        break
                    else:
                        print("Välj mellan 1 eller 2.")
                except ValueError:
                    print("Ange en giltig siffra.")
            else:
                hjälte.inventory.append(Vunnet)
                time.sleep(2)
                break
    
    return hjälte.health, hjälte.inventory, hjälte.level
def main():
    heroname = input("Hej, vad heter du?\n")
    hjälte = Hjälte(heroname, 10, rand.randint(4, 8), [], 1)
    hjältestyrka = hjälte.strength
    valt_vapen = ""
    

    while hjälte.health >= 0:
        print(
            f"""

            Vad vill du göra {heroname}?
            1. Välj dörr
            2. Kolla ryggsäck
            3. Kolla stats
            4. Avsluta spel
            
            """)
    
        val = input("")
        if val == "1":                
            dörrval = " "
            print(""" 
         __________      __________      __________   
        |  __  __  |    |  __  __  |    |  __  __  |
        | |  ||  | |    | |  ||  | |    | |  ||  | |
        | |  ||  | |    | |  ||  | |    | |  ||  | |
        | |__||__| |    | |__||__| |    | |__||__| |
        |  __  __()|    |  __  __()|    |  __  __()|
        | |  ||  | |    | |  ||  | |    | |  ||  | |
        | |  ||  | |    | |  ||  | |    | |  ||  | |
        | |  ||  | |    | |  ||  | |    | |  ||  | |
        | |  ||  | |    | |  ||  | |    | |  ||  | |
        | |__||__| |    | |__||__| |    | |__||__| |     
        |__________|    |__________|    |__________|  
                
                    """)
            while dörrval not in "123":
                print("Du ser 3 olika dörrar. Välj dörr 1, 2 eller 3")
                dörrval = input("")
                if dörrval == "1":
                    hjälte.health, hjälte.inventory, hjälte.level = dörr(1, hjältestyrka, hjälte)
                elif dörrval == "2":
                    hjälte.health, hjälte.inventory, hjälte.level = dörr(2, hjältestyrka, hjälte)
                elif dörrval == "3":
                    hjälte.health, hjälte.inventory, hjälte.level = dörr(3, hjältestyrka, hjälte)
                elif dörrval not in "123":
                    print(f"dörr {dörrval} finns inte. Välj dörr 1, 2 eller 3!")
        elif val == "2":
            #Lägg till att se hjälte.inventory
            print(
                """
                Du öppnade din ryggsäck.
                1. Visa föremål
                2. Equipa vapen
                3. Heala dig
                4. Släng bort item
                5. Stäng ryggsäck
                """)
            itemval = input("")
            if itemval == "1": #Detta är för att visa föremål
                if len(hjälte.inventory) >= 1:
                    #iterera genom lista mha for-loop
                    for sak in hjälte.inventory:
                        print(f"{sak.name} och styrkan är {sak.stre}")
                    time.sleep(2)
                else:
                    print("Du har inget än")
                    pass
            elif itemval == "2": #Detta är för att välja ett föremåla
                try:
                    if len(hjälte.inventory) >= 1:
                        for sak in hjälte.inventory:
                            if sak.equipped == True:
                                sak.equipped = False
                                hjältestyrka -= sak.stre
                        valt_vapen = ""
                        n = 1
                        for sak in hjälte.inventory:
                            print(f"{n}. {sak.name} strenght är {sak.stre}")
                            n += 1
                        
                        val = int(input("vilket vapen vill du använda?"))
                        val -= 1
                        valt_vapen = hjälte.inventory[val]
                        hjältestyrka += valt_vapen.stre
                        valt_vapen.equipped = True
                    else: 
                        pass
                except:
                    print("Välj ett giltigt val")
            elif itemval == "3": #Detta är för att heala med ett föremål
                try:    
                    if len(hjälte.inventory) >= 1:
                        n = 1
                        for sak in hjälte.inventory:
                            print(f"{n}. {sak.name} och den healar {sak.heal}")
                            n += 1
                        val = int(input("Vilket väljer du?"))
                        val -= 1
                        valt_healing = hjälte.inventory[val]
                        if valt_healing.heal > 0:
                            hjälte.health += valt_healing.heal
                            print(f"Du heala dig med {valt_healing.name} och ditt hp är nu {hjälte.health}")
                            hjälte.inventory.pop(val)
                        else:
                            print("Hoppsan, det är inget föremål som man kan heala med")
                            pass
                    else: 
                        pass
                except:
                    print("Välj ett giltigt val")

            elif itemval == "4": #Detta är för att ta bort ett föremål
                if len(hjälte.inventory) >= 1:
                    try:
                        for sak in hjälte.inventory:
                            print(sak.name)
                        x = int(input("Välj vilket föremål du vill ta bort(OBS! Du måste skriva rätt positon på listan) "))
                        x -= 1
                        borttagna=hjälte.inventory.pop(x)
                        print(f"Du har tagit bort itemet {borttagna.name}")
                        time.sleep(2)
                    except:
                        print("Välj ett giltigt val")
                else:
                    pass
            elif itemval == "5":
                pass
        elif val == "3":
            print(f"Ditt hp är {hjälte.health} \nDin styrka är {hjältestyrka}\nDin level är {hjälte.level}")
            time.sleep(2)
        elif val == "4":
            exit("Du avslutar spelet")
        else:
            print("Välj 1, 2, 3 eller 4!")

        if hjälte.level >= 10:
            print("Grattis! Du har vunnit spelet!")
            exit()
    print("Hoppsan, du förlora")
    time.sleep(1)
    omkora = int(input("1.Vill du köra igen?\n2. Vill du avsluta"))
    if omkora == 1:
        print("Okej, då får du köra igen :)")
        main()
    elif omkora == 2:
        print("Okej, vi ses :)")
        time.sleep(2)
        exit()
    else:
        print("Välj ett av alternativen")
main()
