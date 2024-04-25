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
cartones = generar_cartones(10)

def agregar_valores():
    try:
        df = pd.DataFrame(bingo_model)
        un_carton = generar_carton()

        cord_serie = {"row": 0, "column": 31}
        columnas = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

        print(df.iat[0, 31])
        # df.iat[0, 31] = 301
        for i, value in enumerate(columnas, start=0):
            df.iat[2, value] = un_carton[i]
        # print(df.iat[0, 31])
        df.columns.values[-1] = 301

        with pd.ExcelWriter("./bingos/new_bingo_model.xlsx") as writer:
            df.to_excel(writer, sheet_name="Bingo", index=False)
    except Exception as e:
        print(e)

agregar_valores()

wb_original = xw.Book('bingo_model.xlsx')
wb_nuevo = xw.Book('./bingos/new_bingo_model.xlsx')

wb_original.sheets[0].api.Cells.Copy()
wb_nuevo.sheets[0].api.Cells.PasteSpecial(Paste=-4122)

wb_nuevo.save()
wb_nuevo.close()
wb_original.close()