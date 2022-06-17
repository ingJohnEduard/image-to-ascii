from turtle import back
from PIL import Image
import cv2
import numpy as np
import easygui as eg

formato = '.bmp'
ascii_caracter = ['@','#','%','&','$','+','*',';',':','.',' ']

factor = 255/(len(ascii_caracter)-1)
#Tamaño de los caracteres ascii en la imagen
font_size = 0.4
color_font = (0, 255, 0)
#Valor de separacion horizontal y vertical de los caracteres
vertical_factor = 9
horizontal_factor = 6

#interfaz grafica para abrir la imagen a convertir
def open_file():
	archivo = eg.fileopenbox(msg="",title="Seleccione foto a transformar.",default='',filetypes='')
	return archivo

def save_file():
    output_path = eg.filesavebox(msg="",title="Guardar archivo",default='',filetypes='')
    return output_path

def create_canvas(width, height):
  canvas = np.zeros((height, width, 3))
  color_canvas = (0, 0, 0)
  for value in range(3):
    canvas[:,:, value] += color_canvas[value]
  cv2.imwrite("lienzo.bmp", canvas)

def to_ascii(frame):
  string = ""
  for row in range(int(frame.shape[0])):  
    for column in range(int(frame.shape[1])):
      pixel=frame[row][column]
      position=pixel/factor
      caracter=ascii_caracter[int(position)]
      string += caracter
      to_image(caracter,(column,row))
    string += "\n"
  return string
  

def to_image(string_ascii, position):
  cv2.putText(background, string_ascii, (position[0]*horizontal_factor, position[1]*vertical_factor+1), cv2.FONT_HERSHEY_PLAIN, font_size,  
              (color_font[0], color_font[1], color_font[2]), 1)


#funcion para escribir el archivo de salida
#ENTRADA: array
#SALIDA: archivo de texto 
def ouput_file(string, name):
    name += ".txt"
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
save_path = save_file()
image = cv2.imread(path)
#img_factor = int(image.shape[0])/int(image.shape[1])
width = int(input("Ingrese el número de caracteres por línea:  "))
height = int(width*0.8)
dsize = (width, height)
width_canvas, height_canvas = int(width*6), int(height*9)
create_canvas(width_canvas, height_canvas)
background = cv2.imread("lienzo.bmp")
img_resize = cv2.resize(image, dsize)
img_gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
ascii_string = to_ascii(img_gray)

ouput_file(ascii_string, save_path)
cv2.imwrite(save_path+".bmp", background)

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    input("presione enter para salir...")
    sys.exit(main(sys.argv))