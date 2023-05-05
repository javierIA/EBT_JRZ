"""
  Este programa está diseñado para crear
  y animar una simple animación con temática de cerveza.
"""

import sys
from sys import stdout as terminal
from time import sleep
from itertools import cycle
from threading import Thread

terminado = False

def animar():
    for c in cycle(['🔵', '🔵🔵', '🔵🔵🔵', '🔵🔵🔵🔵', '🍺']):
        if terminado:
            break
        terminal.write('\rLlenando tu cerveza ' + c)
        terminal.flush()
        sleep(1.2)  # ajusta esto para cambiar la velocidad de la animación
    terminal.write('\r¡Listo! Aquí tienes tu cerveza! 🍺')
    terminal.flush()

def servir_cervezas(cantidad_total):
    print(f"¡Vamos a servir {cantidad_total} cervezas!")
    for numero_cerveza in range(1, cantidad_total + 1):
        cervezas_llenas = "🍺" * (numero_cerveza - 1)  # Emojis de cervezas llenas
        cervezas_restantes = "🥛" * (cantidad_total - numero_cerveza)  # Emojis de cervezas vacías
        terminal.write("\r\nCervezas servidas: " + cervezas_llenas + "\n")
        terminal.write("Cervezas restantes: " + cervezas_restantes + "\n")
        terminal.flush()

        t = Thread(target=animar)
        t.start()

        # Aquí puedes poner el código que estás esperando que se complete
        # En este caso, simplemente hacemos que el programa duerma durante 6 segundos para demostrar el funcionamiento
        sleep(6)

        global terminado
        terminado = True

        # Reinicia el indicador para la próxima cerveza
        terminado = False

if len(sys.argv) > 1:
    try:
        cantidad_cervezas = int(sys.argv[1])
        servir_cervezas(cantidad_cervezas)  # Cambia este número para servir una cantidad diferente de cervezas
    except ValueError:
        print("El argumento debe ser un número entero.")
else:
    print("Por favor, proporciona el número de cervezas a llenar como argumento.")
