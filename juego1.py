# Cree el juego Piedra, Papel o Tijera explicado en clases.
# Realice mejoras al juego para que no sea necesario ejecutar el programa varias veces para seguir jugando.

from random import randint

opciones = ["Piedra", "Papel", "Tijeras"]

while True:
    random = randint(0, 2)
    juego_computadora = opciones[random]

    print("La computadora sacó:", juego_computadora)

    jusuario = input("¿Cuál deseas escoger? Papel, Piedra o Tijeras (escribe 'exit' para salir): ")

    if jusuario.lower() == 'exit':
        print("¡Gracias por jugar!, suerte para la próxima")
        break

    if jusuario not in opciones:
        print("Opción inválida. Por favor, elige entre Piedra, Papel o Tijeras.")
        continue

    if jusuario == juego_computadora:
        print("Has empatado")
    elif (jusuario == "Piedra" and juego_computadora == "Tijeras") or \
         (jusuario == "Papel" and juego_computadora == "Piedra") or \
         (jusuario == "Tijeras" and juego_computadora == "Papel"):
        print("Has ganado")
    else:
        print("Has perdido")

    print("Para cerrar el juego escribe: exit")