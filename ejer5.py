from PIL import Image
import os

directory = 'images'

print("Ingresa la ruta del archivo de la imagen:")
nombre = input()
print("Ingresa el nombre del archivo de marca de agua:")
marca_de = input()

print("¿Dónde quieres colocar la marca de agua?")
print("1 - Parte Superior izquierda\n2 - Parte Superior derecha\n3 - Parte Inferior izquierda\n4 - Parte Inferior derecha")
resp = int(input())

part_sup_iz = 1
part_sup_der = 2
part_inf_iz = 3
part_inf_der = 4

ruta_img = os.path.join(directory, nombre)
if not os.path.exists(ruta_img):
    print("Error: La imagen especificada no existe.")
    exit()

img = Image.open(ruta_img)

marca = os.path.join(directory, marca_de)
if not os.path.exists(marca):
    print("Error: La imagen de marca de agua especificada no existe.")
    exit()

marca_Agua = Image.open(marca)

img_width, img_height = img.size
marca_Agua_width, marca_Agua_height = marca_Agua.size

nuevo_ancho = int(marca_Agua_width * 0.25)
nuevo_alto = int(marca_Agua_height * 0.25)
marca_Agua = marca_Agua.resize((nuevo_ancho, nuevo_alto))

margen = 50

if resp == 1:
    x = margen
    y = margen
elif resp == 2:
    x = img_width - nuevo_ancho - margen
    y = margen
elif resp == 3:
    x = margen
    y = img_height - nuevo_alto - margen
elif resp == 4:
    x = img_width - nuevo_ancho - margen
    y = img_height - nuevo_alto - margen
else:
    print("Error: Opción no válida.")
    
if marca_Agua.mode != 'RGBA':
    marca_Agua = marca_Agua.convert('RGBA')

img.paste(marca_Agua, (x, y), marca_Agua)

nuevo_nombre = f"{os.path.splitext(nombre)[0]}nueva{os.path.splitext(nombre)[1]}"
ruta_guardado = os.path.join(directory, nuevo_nombre)
img.save(ruta_guardado)

print(f"Imagen guardada como: {nuevo_nombre}")
img.show()
