import os

# Solicitar al usuario el nombre del directorio
nombre_directorio = input("Ingrese el nombre del directorio a crear: ")

try:
    # Intentar crear el directorio
    os.mkdir(nombre_directorio)
    print(f"Directorio '{nombre_directorio}' creado con éxito.")
except FileExistsError:
    print(f"El directorio '{nombre_directorio}' ya existe.")
except OSError as e:
    print(f"Error al crear el directorio: {e}")
