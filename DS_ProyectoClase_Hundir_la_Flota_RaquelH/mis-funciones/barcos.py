from tablero import tablero
from tablero import tablero_pc
import random
import numpy as np


def coloca_barco(tablero, barco):
    # Nos devuelve el tablero si puede colocar el barco, si no devuelve False, y avise por pantalla
    tablero_temp = tablero.copy()
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    for pieza in barco:
        fila = pieza[0]
        columna = pieza[1]
        if fila < 0  or fila >= num_max_filas:
            #print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if columna <0 or columna>= num_max_columnas:
            #print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if tablero[pieza] == "O" or tablero[pieza] == "X":
            #print(f"No puedo poner la pieza {pieza} porque hay otro barco")
            return False
        tablero_temp[pieza] = "O"
    return tablero_temp

def crea_barco_aleatorio(tablero,eslora = 4, num_intentos = 100):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    while True:
        barco = []
        # Construimos el hipotetico barco
        pieza_original = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))
        barco.append(pieza_original)
        orientacion = random.choice(["N","S","O","E"])
        fila = pieza_original[0]
        columna = pieza_original[1]
        for i in range(eslora -1):
            if orientacion == "N":
                fila -= 1
            elif orientacion  == "S":
                fila += 1
            elif orientacion == "E":
                columna += 1
            else:
                columna -= 1
            pieza = (fila,columna)
            barco.append(pieza)
        tablero_temp = coloca_barco(tablero, barco)
        if type(tablero_temp) == np.ndarray:
            return tablero_temp
        #print("Tengo que intentar colocar otro barco")
        
mi_tablero = crea_barco_aleatorio(tablero, eslora = 2)
mi_tablero =crea_barco_aleatorio(mi_tablero, eslora = 2)
mi_tablero = crea_barco_aleatorio(mi_tablero, eslora = 2)
mi_tablero = crea_barco_aleatorio(mi_tablero, eslora = 3)
mi_tablero =crea_barco_aleatorio(mi_tablero, eslora = 3)
mi_tablero = crea_barco_aleatorio(mi_tablero, eslora = 4)

pc_tablero = crea_barco_aleatorio(tablero_pc, eslora = 2)
pc_tablero = crea_barco_aleatorio(pc_tablero, eslora = 2)
pc_tablero = crea_barco_aleatorio(pc_tablero, eslora = 2)
pc_tablero = crea_barco_aleatorio(pc_tablero, eslora = 3)
pc_tablero = crea_barco_aleatorio(pc_tablero, eslora = 3)
pc_tablero = crea_barco_aleatorio(pc_tablero, eslora = 4)

