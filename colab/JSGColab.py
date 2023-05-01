import os
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from PIL import Image
from google.colab import drive

# Función para calcular el conjunto de Julia
def julia_set(z, c, max_iter):
    for i in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return i
    return max_iter - 1

# Parámetros de la imagen
width = 1500
height = 1500
x_min, x_max = -1.5, 1.5
y_min, y_max = -1.5, 1.5
max_iter = 100
quantum = 30

#Colores
cmaps_dict = cm.datad
cmaps_list = list(cmaps_dict.keys())
cmaps_list.sort()
random_cmap = random.choice(cmaps_list)
# random_cmap = 'plasma'
# Montar el Google Drive
drive.mount('/content/drive')

# Establecer la ruta a la carpeta principal de Google Drive
root_path = '/content/drive/My Drive/'

# Establecer la ruta a la carpeta 'Fractales'
fractales_folder_path = os.path.join(root_path, 'FractalesSorted')

# CMAPS
# Comprobar si la carpeta 'Fractales' existe
if not os.path.exists(fractales_folder_path):
    # Si la carpeta 'Fractales' no existe, crear la carpeta
    os.makedirs(fractales_folder_path)
    print(f'Carpeta "{fractales_folder_path}" creada con éxito.')
else:
    print(f'La carpeta "{fractales_folder_path}" ya existe.')

# Generar varias imágenes del conjunto de Julia
for i in range(quantum):
    # Generar número aleatorio para la parte real e imaginaria de la constante c
    real_part = np.random.uniform(-1, 1)
    imag_part = np.random.uniform(-1, 1)
    c = complex(real_part, imag_part)

    # Generar valores de coordenadas x e y
    x_vals = np.linspace(x_min, x_max, width)
    y_vals = np.linspace(y_min, y_max, height)

    # Generar valores de coordenadas complejas (z = x + iy)
    z_vals = x_vals[:, np.newaxis] + y_vals[np.newaxis, :]*1j

    # Calcular valores del conjunto de Julia para cada valor de z
    julia_vals = np.array([julia_set(z, c, max_iter) for z in z_vals.flatten()])
    julia_vals = julia_vals.reshape((height, width))

    # Crear imagen del conjunto de Julia
    plt.imshow(julia_vals, cmap=random_cmap)
    plt.axis('off')

    # Crear la carpeta con el nombre del cmap aleatorio si no existe
    cmap_folder_path = os.path.join(fractales_folder_path, random_cmap)
    if not os.path.exists(cmap_folder_path):
        os.makedirs(cmap_folder_path)
        print(f'Carpeta "{cmap_folder_path}" creada con éxito.')

    # Guardar imagen en la carpeta correspondiente al cmap aleatorio
    filename = f'julia_{random_cmap}_{real_part:.4f}_{imag_part:.4f}.png'
    filepath = os.path.join(cmap_folder_path, filename)
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f'Imagen {i+1} guardada en "{filepath}".')

