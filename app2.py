import random
import pandas as pd
import xlwings as xw

bingo_model = pd.read_excel("bingo_model.xlsx")

# Función para generar un cartón de bingo
def generar_carton():
    numeros = random.sample(range(1, 91), 15)
    numeros.sort()
    return numeros

# Función para generar los 500 cartones de bingo
def generar_cartones(num_cartones):
    cartones = [generar_carton() for _ in range(num_cartones)]
    return cartones

# Generar los 500 cartones de bingo
cartones = generar_cartones(600)

def agregar_valores(un_carton, index):
    try:
        df = pd.DataFrame(bingo_model)
        # un_carton = generar_carton()

        columnas = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
        
        for i, value in enumerate(columnas, start=0):
            df.iat[2, value] = un_carton[i]
        
        df.columns.values[-1] = 300 + index

        with pd.ExcelWriter(f"./bingos/Bingo{index}.xlsx") as writer:
            df.to_excel(writer, sheet_name="Bingo", index=False)
    except Exception as e:
        print(e)

wb_original = xw.Book('bingo_model.xlsx')

for i in range(1, 601):
    agregar_valores(cartones[i - 1], i)
    wb_nuevo = xw.Book(f'./bingos/Bingo{i}.xlsx')

    wb_original.sheets[0].api.Cells.Copy()
    wb_nuevo.sheets[0].api.Cells.PasteSpecial(Paste=-4122)

    wb_nuevo.save()
    wb_nuevo.close()
wb_original.close()

def hay_repetidos(cs):
    for i in range(len(cs)):
        for j in range(i + 1, len(cs)):
            if cs[i] == cs[j]:
                return True  # Se encontró un cartón repetido
    return False  # No se encontraron cartones repetidos

# Utiliza la función para verificar si hay cartones repetidos
if hay_repetidos(cartones):
    print("Se encontraron cartones repetidos.")
else:
    print("No hay cartones repetidos.")

