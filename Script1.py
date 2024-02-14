#  Martínez Herrera Miguel Agustín

# Pedir nombres de los jugadores
jugador1 = input("Ingrese el nombre del primer jugador: ")
jugador2 = input("Ingrese el nombre del segundo jugador: ")

# Inicializar puntajes
global acabar
global sets_jugador1 
global sets_jugador2 
global juegos_jugador1 
global juegos_jugador2 
global  puntaje_jugador1 
global puntaje_jugador2 
global contadorSaque 
acabar = True
sets_jugador1 = 0
sets_jugador2 = 0
juegos_jugador1 = 0
juegos_jugador2 = 0
puntaje_jugador1 = 0
puntaje_jugador2 = 0
contadorSaque = 0

def mostrar_marcador():
    global sets_jugador1 
    global sets_jugador2 
    global juegos_jugador1 
    global juegos_jugador2 
    global  puntaje_jugador1 
    global puntaje_jugador2 
    global contadorSaque 
    print("Marcador:")
    print(f"{jugador1}: Puntaje: {toStringPuntaje(puntaje_jugador1)}. Juegos:{juegos_jugador1}. Sets:{sets_jugador1}")
    print(f"{jugador2}: Puntaje: {toStringPuntaje(puntaje_jugador2)}. Juegos:{juegos_jugador2}. Sets:{sets_jugador2}")

def toStringPuntaje(puntaje):
    if puntaje == 0:
        return "0"
    elif puntaje == 1:
        return "15"    
    elif puntaje == 2:
        return "30"
    elif puntaje == 3:
        return "40"
    elif puntaje == 10:
        return "Adv"

def definirCancha():
    global sets_jugador1 
    global sets_jugador2 
    if ((sets_jugador1 + sets_jugador2) % 2) == 1:
        print("La otra cancha")
    else:
        print("Misma cancha")

def definirSaque():
    global contadorSaque 
    if (contadorSaque  % 2) == 0:
        print("Saca jugador1")
    else:
        print("Saca jugador2")

def ganarPartido(sets1, sets2):
    global acabar
    if sets1 == 2:
        print("jugador1 gana el encuentro.")
        acabar = False
    elif sets2 == 2:
        print("jugador2 gana el encuentro.")
        acabar = False

def ganarSet(juegos1, juegos2):
    global sets_jugador1 
    global sets_jugador2 
    global juegos_jugador1 
    global juegos_jugador2 
    if (juegos1 >= 6) & (abs(juegos1-juegos2) >= 2):
        print("jugador1 gana el set")
        sets_jugador1+=1
        ganarPartido(sets_jugador1, sets_jugador2)
        juegos_jugador1 = 0
        juegos_jugador2 = 0
    elif (juegos2 >= 6) & (abs(juegos1-juegos2) >= 2):
        print("jugador2 gana el set")
        sets_jugador2+=1
        ganarPartido(sets_jugador1, sets_jugador2)
        juegos_jugador2 = 0
        juegos_jugador2 = 0

def ganarJuego(puntaje1, puntaje2):
    global juegos_jugador1 
    global juegos_jugador2 
    global contadorSaque

    if (puntaje1 == 4):
        print("jugador1 gana el juego.")
        juegos_jugador1+=1
        contadorSaque+=1
        ganarSet(juegos_jugador1, juegos_jugador2)
    if (puntaje2 == 4):
        print("jugador2 gana el juego.")
        juegos_jugador2+=1
        contadorSaque+=1
        ganarSet(juegos_jugador1, juegos_jugador2)

def ganarPunto(ganador_punto, puntaje1, puntaje2):
    global  puntaje_jugador1 
    global puntaje_jugador2 
    if ganador_punto == jugador1:
        if (puntaje2 == 3) & (puntaje1 == 3):
            puntaje_jugador1 = 10 #10 es Advantage
        elif (puntaje1 == 3) & (puntaje2 == 10):
            puntaje_jugador2 = 3
        elif (puntaje1 == 10):
            puntaje_jugador1 = 4
            ganarJuego(puntaje_jugador1, puntaje_jugador2)
            puntaje_jugador1 = 0
            puntaje_jugador2 = 0
        elif (puntaje1 == 3) & (puntaje2 <= 2):
            puntaje_jugador1+= 1
            ganarJuego(puntaje_jugador1, puntaje_jugador2)
            puntaje_jugador1 = 0
            puntaje_jugador2 = 0
        else:
            puntaje_jugador1 += 1

    if ganador_punto == jugador2:
        if (puntaje1 == 3) & (puntaje2 == 3):
            puntaje_jugador2 = 10 #10 es Advantage
        elif (puntaje2 == 3) & (puntaje1 == 10):
            puntaje_jugador1 = 3
        elif (puntaje2 == 10):
            puntaje_jugador2 = 4
            ganarJuego(puntaje_jugador1, puntaje_jugador2)
            puntaje_jugador2 = 0
            puntaje_jugador1 = 0
        elif (puntaje2 == 3) & (puntaje1 <= 2):
            puntaje_jugador2+= 1
            ganarJuego(puntaje_jugador1, puntaje_jugador2)
            puntaje_jugador2 = 0
            puntaje_jugador1 = 0
        else:
            puntaje_jugador2 += 1
    
# Loop para registrar los puntos
while acabar:
    definirSaque();
    definirCancha();
    try:
        ganador_punto = input(f"¿Quién gana el punto, {jugador1} o {jugador2}? (Ingrese 'fin' para terminar): ")
        if ganador_punto.lower() == 'fin':
            break
        elif ganador_punto == jugador1:
            ganarPunto(ganador_punto, puntaje_jugador1, puntaje_jugador2)
        elif ganador_punto == jugador2:
            ganarPunto(ganador_punto, puntaje_jugador1, puntaje_jugador2)
        else:
            raise    
    except:
        print("Nombre de jugador inválido")
    
    mostrar_marcador()

print("Fin del partido")