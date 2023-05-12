import random
import string

def abrir_archivo(ruta):
    with open(ruta, "r") as archivo:
        return archivo.read()

def agregar_datos(ruta, datos):
    with open(ruta, "a") as archivo:
        archivo.write("\n" + datos)

def leer_archivo(ruta):
    with open(ruta, "r") as archivo:
        return archivo.read()

def crear_archivo(ruta, datos):
    with open(ruta, "w") as archivo:
        archivo.write(datos)

def generar_password(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    return password

# Ejemplo de uso
ruta_archivo = "data/nombres.txt"

# Leer el archivo
contenido = abrir_archivo(ruta_archivo)
print("Contenido del archivo:")
print(contenido)

# Agregar nuevos datos al archivo
nuevos_datos = "Juan"
agregar_datos(ruta_archivo, nuevos_datos)
print(f"Se agregaron los datos '{nuevos_datos}' al archivo.")

# Leer nuevamente el archivo
contenido_actualizado = leer_archivo(ruta_archivo)
print("Contenido actualizado del archivo:")
print(contenido_actualizado)

# Generar una contraseña
password = generar_password(8)
print("Contraseña generada:", password)


