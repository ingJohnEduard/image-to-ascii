from PIL import Image
import cv2
import numpy as np
import easygui as eg

formato = '.bmp'
ascii_caracter = ['@','#','%','&','$','+','*',';',':','.',' ']

factor = 255/(len(ascii_caracter)-1)


#interfaz grafica para abrir la imagen a convertir
def open_file():
	archivo = eg.fileopenbox(msg="",title="Seleccione foto a transformar.",default='',filetypes='')
	return archivo

def save_file():
    output_path = eg.filesavebox(msg="",title="Guardar archivo .txt",default='',filetypes='*.txt')
    return output_path

def to_ascii(frame):
  string = ""
  for i in range(width):  
    for j in range(height):
      pixel=frame[i][j]
      position=pixel/factor
      caracter=ascii_caracter[int(position)]
      string += caracter
    string += "\n"
  ouput_file(string)


#funcion para escribir el archivo de salida
#ENTRADA: array
#SALIDA: archivo de texto 
def ouput_file(string):
    name = save_file()
    file= open(name,'w')
    file.write(string)
    file.close()

    file = open(name,'r')
    if (file):
       print(file.read())
       print('se a creado el archivo de texto con exito...')
    else:
       print('Error al crear el archivo')

################################
########BLOQUE PRINCIPAL########
################################

path = open_file()
image = cv2.imread(path)
height_full,width_full = image.shape[:2]
scale_factor = 10 #porcentaje de escala
width = 66#int((width_full*scale_factor)/100)
height = 112#int((height_full*(scale_factor+10))/100)
print(height_full,"\t", width_full, "\t", height, "\t", width)
dsize = (height, width)
img_resize = cv2.resize(image, dsize)
img_gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
to_ascii(img_gray)

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    input("presione enter para salir...")
    sys.exit(main(sys.argv))