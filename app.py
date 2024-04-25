import random

i = 0
# Función para generar un cartón de bingo
def generar_carton():
    numeros = random.sample(range(1, 91), 15)
    numeros.sort()
    return numeros

# Función para generar los 500 cartones de bingo
def generar_cartones(num_cartones):
    cartones = [generar_carton() for _ in range(num_cartones)]
    return cartones

# Función para simular la extracción de números durante el juego
def jugar_bingo(cartones):
    numeros_llamados = set()
    while True:
        numero = random.randint(1, 90)
        numeros_llamados.add(numero)
        print("Número llamado:", numero)
        for i, carton in enumerate(cartones):
            if all(num in numeros_llamados for num in carton):
                print("¡Bingo! El cartón {} ha ganado.".format(i+1))
                return
        print(cartones[0])
        print(cartones[1])
        print(cartones[2])
        print(cartones[3])
        print(cartones[4])
        input("Presiona Enter para llamar al siguiente número...")

# Generar los 500 cartones de bingo
cartones = generar_cartones(500)

# Iniciar el juego de bingo
print("¡Comienza el juego de bingo!")
jugar_bingo(cartones)
