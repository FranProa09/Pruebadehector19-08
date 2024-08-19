from PIL import Image
import os

directory = "images"
output_dir = "recortes"

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

print("Ingrese la ruta de una imagen:")
nombre = input()

image_path = os.path.join(directory, nombre)

if not os.path.exists(image_path):
    print("El archivo de imagen no existe. por favor verifica el nombre.")
else:
    img = Image.open(image_path)
    img_width, img_height = img.size
    
    print("Ingrese las coordenadas iniciales para empezar el corte:")
    x = int(input("Coordenada X inicial: "))
    y = int(input("Coordenada Y inicial: "))
        
    print("Ingrese el ancho y alto del recorte:")
    width = int(input("Ancho: "))
    height = int(input("Alto: "))
        
    if x < 0 or y < 0 or (x + width) > img_width or (y + height) > img_height:
        print("Error: Las coordenadas o dimensiones exceden los límites de la imagen.")
    else:
        img_crop = img.crop((x, y, x + width, y + height))
        num_recortes = len([f for f in os.listdir(output_dir) if f.startswith("recorte") and f.endswith(".png")])
        nuevo_nombre = f"recorte{num_recortes + 1}.png"
        nueva_ruta = os.path.join(output_dir, nuevo_nombre)
        img_crop.save(nueva_ruta)
        print(f"Recorte guardado como {nuevo_nombre} en el directorio 'recortes'.")
        img_crop.show()
