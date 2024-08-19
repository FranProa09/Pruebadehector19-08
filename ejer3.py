from PIL import Image
import os

#directory = "images"

print("Ingresa el nombre del archivo de imagen (dentro de la carpeta 'images'):")
ruta = input()

print("Ingresa el ángulo de rotación:")
angulo = int(input())

ruta = os.path.join(ruta)
img = Image.open(ruta)
newimg= img.rotate(angulo)

nombre_base, extension = os.path.splitext(ruta)
nuevo_nombre = f"{nombre_base}Rot{extension}"

newruta = os.path.join(nuevo_nombre)
newimg.save(newruta)

newimg.show()

print(f"Imagen guardada como: {newruta}")
