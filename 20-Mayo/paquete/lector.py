import pandas as pd

class Lector:
    def __init__(self, ruta, sheet_name=0):
        self.ruta = ruta
        self.sheet_name = sheet_name

    def leer_excel(self):
        try:
            return pd.read_excel(self.ruta, sheet_name=self.sheet_name)
        except FileNotFoundError:
            print(f"El archivo {self.ruta} no se encontró.")
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")

    def leer_encabezados(self):
        try:
            return self.leer_excel().columns
        except AttributeError:
            print("Ocurrió un error al obtener los encabezados. Asegúrate de que el archivo se haya leído correctamente.")

    def leer_datos(self):
        try:
            return self.leer_excel().values
        except AttributeError:
            print("Ocurrió un error al obtener los datos. Asegúrate de que el archivo se haya leído correctamente.")

reader= Lector("data/precios.xlsx")
print(reader.leer_encabezados())