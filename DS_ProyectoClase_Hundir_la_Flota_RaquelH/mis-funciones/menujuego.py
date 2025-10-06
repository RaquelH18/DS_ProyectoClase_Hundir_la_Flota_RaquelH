from barcos import mi_tablero
from barcos import pc_tablero
import time 
from disparar import disparar



def mostrar_menu():
    
    while True:
        print("\nInstrucciones Hundir la flota 🎮⛵")
        print("1. Mostrar mi tablero ")
        print("2. Mostrar tablero PC")
        print("3. Disparar 🔫")
        print("4. Salir ")
        opcion = input ("  ")
        if opcion in ["1", "2", "3", "4"]:
            if opcion == "1":
                print("Este es mi Tablero")
                print(mi_tablero)
                time.sleep(1)
                
            elif opcion == "2":
                print("Este es el Tablero PC")
                print(pc_tablero)
                time.sleep(1)
            
            elif opcion == "3":
                print("Disparar 💥! ")
                disparar(pc_tablero)   
            
            elif opcion == "4":
                print("Bye 👋! ")
                break
            
                
        else:
            print ("opcion Invalida, por favor escribe 1 o 2 o 3 \n")
            
