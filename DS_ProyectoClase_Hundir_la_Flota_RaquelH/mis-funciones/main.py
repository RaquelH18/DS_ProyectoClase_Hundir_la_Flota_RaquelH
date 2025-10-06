from menujuego import mostrar_menu
import time
from tablero import tablero
from tablero import tablero_pc

print("\n🎮⚓🚢 Bienvenid@ a Hundir la Flota 🎮⚓🚢 ")
print("\n1. Jugar")
print("2. Salir")

while True:
    opcion = input ("\nSelecciona 1 para jugar 2 para salir ")
    if opcion in ["1", "2"]:
        if opcion == "1":
            print("VAMOS A JUGAR 🚀!")
            time.sleep(1)
            mostrar_menu()
            break
        
        elif opcion == "2":
            print (" Bye Grumete 👋, hasta la proxima!")
            break
    else:
        print ("opcion invalida ❌ por favor escribe 1 o 2\n")
        