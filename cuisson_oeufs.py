import platform 
import winsound
import time

# time.sleep(1)

minutes_cuisson = 0


def choix_menu():
    choix_str = ""
    choix = 0
    
    choix_str = input("Choisissez un parmi les trois menus: ")
    
    try: 
        choix = int(choix_str)
            
    except ValueError:
        print("Veuillez entrer un nombre numérique")
        
    else: 
        if choix == 1:
            print("Vous avez choisi: Les Oeufs à la coque")
            
        elif choix == 2:
            print("Vous avez choisi: Les Oeufs mollets")
            
        elif choix == 3:
            print("Vous avez choisi: Les Oeufs durs")
            
        else:
            print("Choisissez 1 ou 2 ou 3")
                              
    return choix


def temps_cuisson():
    choix = 0
    duree_cuisson = 0
    
    while not(choix == 1 or choix == 2 or choix == 3):
        choix = choix_menu()
    
    if choix == 1:
        duree_cuisson = 3
    elif choix == 2:
        duree_cuisson = 6
    else:
        duree_cuisson = 9
        
    return duree_cuisson
                
        

print("Voila notre menu: ")
print("1- Oeufs à la coque: 3 minutes")
print("2- Oeufs mollets: 6 minutes")
print("3- Oeufs durs: 9 minutes")
print("")


if platform.system() == "Windows":
    frequency = 500
    duration = 1000
    
    duree = temps_cuisson() * 60
    compte = 0
    
    for i in range(duree):
        minutes = duree // 60
        seconds = duree - (minutes * 60)
        # seconds = seconds if seconds >= 10 else f"0{seconds}"
        
        time.sleep(1)
        print(".", end="", flush=True)
        
        if compte == 10:
            # print(f"Il vous reste: 0{minutes}:{seconds}")
            print(f"Durée restante : {minutes:02d}m:{seconds:02d}s")
            compte = 0
            
        compte += 1    
        duree -= 1
   
    winsound.Beep(frequency, duration)

else:
    print("Driiiiiiiiiiiiiiiiiiiiiing!!!")
    
    