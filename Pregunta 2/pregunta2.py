pip install pyfiglet

import pip

import random

from pyfiglet import Figlet # type: ignore

def main():
 
    figlet = Figlet()
    
  
    fuentes_disponibles = figlet.getFonts()
    
   
    fuente_usuario = input("Ingrese el nombre de una fuente (deje en blanco para una aleatoria): ")
    
  
    if fuente_usuario.strip() == "":
        fuente_seleccionada = random.choice(fuentes_disponibles)
    else:
        if fuente_usuario in fuentes_disponibles:
            fuente_seleccionada = fuente_usuario
        else:
            print("Fuente no encontrada. Se seleccionará una aleatoria.")
            fuente_seleccionada = random.choice(fuentes_disponibles)
    
   
    figlet.setFont(font=fuente_seleccionada)
    print(f"Fuente seleccionada: {fuente_seleccionada}")
    
    
    texto = input("Ingrese el texto a imprimir: ")
    
    
    print(figlet.renderText(texto))

if __name__ == "__main__":
    main()