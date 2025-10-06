from tablero import tablero_pc
from tablero import tablero

"""
def recibir_disparo(tablero, coordenada):
    if tablero[coordenada] == "O":
        tablero[coordenada] = "X"
        print("Tocado ⛵ 🎯 ")
    elif tablero[coordenada] == "X":
        print("Deja de perder el tiempo, dispara a otro sitio, looser")
    else:
        tablero[coordenada] = "-"
        #print("Agua 💧 ")
        
recibir_disparo(tablero,(4,2))
#print(tablero)
"""

def disparar(tablero_pc):
    coordenada = input("Introduce coordenadas (Ej:C3):").upper()
    coordenada_letra = coordenada[0]
    coordenada_numero = coordenada[1]
    
    letra = "ABCDEFGHIJ"
    numero ="123456789"
    

    if coordenada_letra in letra and coordenada_numero in numero:
        
        
        if tablero[coordenada] == "O":
            print("Tocado ⛵ 🎯 ")
        elif tablero[coordenada] == "X":
            print("Deja de perder el tiempo, dispara a otro sitio, looser")
        else:
            tablero[coordenada] = "-"
        print("Agua 💧 ")
        
        
    else: print("Coordenada invalida ❌, introduce una coordenada valida ej: C3")
        

        
#disparar (tablero, (2,3))
