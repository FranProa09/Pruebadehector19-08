from PIL import Image
import pprint, os

directory = 'images'

print("Ingresa la ruta del archivo de imagen (dentro de la carpeta 'images'):")
ruta = input()

newruta = os.path.join(ruta)
img = Image.open(ruta)

width, height = img.size
ruta_Aux= os.path.splitext(ruta)
root=ruta_Aux[0]
ext=ruta_Aux[1]

Lista=root.split("/")
nomArch=(f"{Lista[6]}{ext}")

matriz = [
    ["Nombre", nomArch],
    ["Tamaño", f"{width}x{height}"],
    ["Extension", img.format],
    ["Cantidad de pixeles", width * height],
    ["Ubicacion de la imagen", os.path.dirname(ruta)]
    
]

for fila in matriz:
    pprint.pprint(f"{fila[0]}: {fila[1]}")

