from PIL import Image
import os

print("Ingresa la ruta de la imagen (incluye la extensión): ")
ruta = input()
img = Image.open(ruta)

img.show()

nombre_nueva_imagen = input("Ingresa el nombre de la nueva imagen (incluye la extensión, por ejemplo, .jpg o .png): ")
dir_destino = os.path.dirname(ruta) 
nueva_ruta = os.path.join(dir_destino, nombre_nueva_imagen)

img.save(nueva_ruta)
print(f"La imagen se ha guardado exitosamente como {nueva_ruta}")