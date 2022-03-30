from operator import truediv
import xml.etree.ElementTree as ET
from lista import lista
from casilla import casilla
from ciudad import ciudad
from robot import robot


robots = lista()
ciudades = lista()

def cargarArchivo(ruta):

    tree = ET.parse(ruta)
    raiz = tree.getroot()

    #robots = lista()
    #ciudades = lista()
    for obj in raiz[0]:
        filas=int(obj[0].get("filas"))
        col = int(obj[0].get("columnas"))
        nombre = obj[0].text
        entradas = lista()
        civiles= lista()
        recursos=lista()
        unidadesMilitares = lista()
        tablero = lista()
        for i in range(filas+1):
            column = 1
            stringFila = obj[i+1].text
            row=lista()
            for j in stringFila:
                if j == 'E':
                    
                    entradas.agregar_Final(casilla("entrada",i+1,column,0))
                elif j=='R':
                    recursos.agregar_Final(casilla("recurso",i+1,column,0))
                elif j == 'C':
                    civiles.agregar_Final(casilla("civil",i+1,column,0))
                elif j =="\"":
                    continue
                row.agregar_Final(j)
                column+=1
            tablero.agregar_Final(row)
            
        for dato in obj:
            if dato.tag =='unidadMilitar':
                unidadesMilitares.agregar_Final(casilla("militar",int(dato.get("fila")),int(dato.get("columna")),int(dato.text)))
        ciudades.agregar_Final(ciudad(nombre,filas,col,tablero,unidadesMilitares,entradas,recursos,civiles))

    for obj in raiz[1]:
        nombre= obj[0].text
        tipo = obj[0].get("tipo")
        if tipo == "ChapinFighter":
            capacidad = int(obj[0].get("capacidad"))
            robots.agregar_Final(robot(nombre,tipo,capacidad))
        else:
            robots.agregar_Final(robot(nombre,tipo,0))

def menu():
    while True:
        pass

    pass

cargarArchivo("Entrada0.xml")
    
#print("Ciudades cargadas")
#print("----------------------------------------------")
#for i in range(ciudades.cant):
#    ciudades.getPos(i).imprimirTablero()
#    print("-----------------------------------------------")
#    print(ciudades.getPos(i).nombre)
#    print(ciudades.getPos(i).filas)
#    print(ciudades.getPos(i).columnas)
#    print("-----------------------------------------------")
#    for j in range(ciudades.getPos(i).unidadesMilitares.cant):
#        print("Fila: " + str(ciudades.getPos(i).unidadesMilitares.getPos(j).fila)  + " columna: " + str(ciudades.getPos(i).unidadesMilitares.getPos(j).columna) + " poder: " + str(ciudades.getPos(i).unidadesMilitares.getPos(j).poder))
#    print("-_-_-_---_-_-_-_----_--_-_----_-_-_-_-_--------_----_-_-_-------_--")


#print("-_-_----_----_-_---_---------_-_-_-------_-_------_-_--_-_---_--_-_--_-_")
#for i in range(robots.cant):
#    if robots.getPos(i).tipo == "ChapinFighter":
#
#        print("robot : " + robots.getPos(i).nombre + " tipo: " + robots.getPos(i).tipo + " capacidad: " + str(robots.getPos(i).capacidad))
#    else:
#        print("robot : " + robots.getPos(i).nombre + " tipo: " + robots.getPos(i).tipo)
#
#    print("_*_**_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")

    




#Eu