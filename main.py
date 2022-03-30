from operator import truediv
from runpy import run_path
import xml.etree.ElementTree as ET
from lista import lista
from casilla import casilla
from ciudad import ciudad
from robot import robot


robotsFighters = lista()
ciudades = lista()
robotsRescue = lista()


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
            robotsFighters.agregar_Final(robot(nombre,tipo,capacidad))
            
        else:
            robotsRescue.agregar_Final(robot(nombre,tipo,0))
            

def menuCiudad():
    while True:
        i=0
        print("........................................................")
        print("Seleccione una ciudad")
        while(i<ciudades.cant):
            print(str(i) + ". " + ciudades.getPos(i).nombre)
            i+=1
        print(str(i) + ".volver")
        print("........................................................")
        x=input()

        if x.isdigit():
            x = int(x)
            if x< ciudades.cant and x>=0:
                
                return ciudades.getPos(int(x))
            elif x==i:
                print("Saliendo")
                return False
            else:
                print("Seleccione una opción válida")
                continue
        else:
            print("Seleccione una opción válida")
            continue
        
def menu():
    while True:
        print("........................................................")
        print("Seleccione el tipo de misión")
        print("1.Extracción de recursos")
        print("2.Misión de rescate")
        print("3.Salir")
        print("........................................................")
        x = input()
        if x=='1':
            #mision recursos
            if robotsFighters.cant==1:
                #mandar al unico chabon que hay
                fighter = robotsFighters.getPos(0)
                city = menuCiudad()
                if city==False:
                    continue
                #elegir recurso
                casilla = menuCasilla(city.recursos)
                if casilla==False:
                    continue
                #Elegir casilla de inicio
                Entrada = menuCasilla(city.entradas)
                if Entrada==False:
                    continue
                #Hacer mision
                print(".-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
                print("Mision con el dron " + fighter.nombre)
                print("en la ciudad " + city.nombre)
                print("en la casilla inicio Fila: " + str(Entrada.fila) + " columna: " + str(Entrada.columna))
                print("en la casilla Recurso Fila: " + str(casilla.fila) + " columna: " + str(casilla.columna))
                y = input()
                pass
            elif robotsFighters.cant<=0:
                print("No hay chapinFighters para hacer misiones de extracción de recursos")
                continue
            else:
                #hacer menu para elegir chabon
                fighter = menuRobot(robotsFighters)
                if fighter==False:
                    continue
                #elegir ciudad
                city = menuCiudad()
                if city==False:
                    continue
                #elegir recurso
                casilla = menuCasilla(city.recursos)
                if casilla==False:
                    continue
                #Elegir casilla de inicio
                Entrada = menuCasilla(city.entradas)
                if Entrada==False:
                    continue
                #Hacer mision
                print(".-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
                print("Mision con el dron " + fighter.nombre)
                print("en la ciudad " + city.nombre)
                print("en la casilla inicio Fila: " + str(Entrada.fila) + " columna: " + str(Entrada.columna))
                print("en la casilla Recurso Fila: " + str(casilla.fila) + " columna: " + str(casilla.columna))
                y = input()
                pass
        elif x=='2':
            #mision rescate
            if robotsRescue.cant==1:
                #mandar al unico chabon que hay
                rescue= robotsRescue.getPos(0)
                city = menuCiudad()
                if city==False:
                    continue
                #elegir civil
                casilla = menuCasilla(city.civiles)
                if casilla==False:
                    continue
                #Elegir casilla de inicio
                Entrada = menuCasilla(city.entradas)
                if Entrada==False:
                    continue
                #Hacer mision
                print(".-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
                print("Mision con el dron " + rescue.nombre)
                print("en la ciudad " + city.nombre)
                print("en la casilla inicio Fila: " + str(Entrada.fila) + " columna: " + str(Entrada.columna))
                print("en la casilla Civil Fila: " + str(casilla.fila) + " columna: " + str(casilla.columna))
                y = input()
                pass
            elif robotsRescue.cant<=0:
                print("No hay chapinRescue para hacer misiones Rescate")
                continue
            else:
                #hacer menu para elegir chabon
                rescue = menuRobot(robotsRescue)
                if rescue==False:
                    continue
                #elegir ciudad
                city = menuCiudad()
                if city==False:
                    continue
                #elegir civil
                casilla = menuCasilla(city.civiles)
                if casilla==False:
                    continue
                #Elegir casilla de inicio
                Entrada = menuCasilla(city.entradas)
                if Entrada==False:
                    continue
                #Hacer mision
                print(".-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
                print("Mision con el dron " + rescue.nombre)
                print("en la ciudad " + city.nombre)
                print("en la casilla inicio Fila: " + str(Entrada.fila) + " columna: " + str(Entrada.columna))
                print("en la casilla Civil Fila: " + str(casilla.fila) + " columna: " + str(casilla.columna))
                y = input()
                
                pass
            pass
        elif x=='3':
            print("Saliendo")
            break
        else:
            print("Seleccione una opción válida")
    pass
    
def menuRobot(robots):
    while True:
        i=0
        print("........................................................")
        print("Seleccione un robot par al mision")
        while(i<robots.cant):
            print(str(i) + ". " + robots.getPos(i).nombre)
            i+=1
        print(str(i) + ".volver")
        print("........................................................")
        x=input()

        if x.isdigit():
            x = int(x)
            if x< robots.cant and x>=0:
                #Mandar a seleccionar mision
                return robots.getPos(int(x))
                pass
            elif x==i:
                print("Saliendo")
                return False
            else:
                print("Seleccione una opción válida")
                continue
        else:
            print("Seleccione una opción válida")
            continue

def menuCasilla(casillas):
    if casillas.cant == 1:
            return casillas.getPos(0)
    elif casillas.vacio:
        print("No hay casillas para poder realizar la mision")
        return False
    while True:
        
        i=0
        print("........................................................")
        print("Seleccione una Casilla de tipo "+ casillas.getPos(0).tipo)
        while(i<casillas.cant):
            print(str(i) + ". Fila: " + str(casillas.getPos(i).fila) + " columna: " + str(casillas.getPos(i).columna))
            i+=1
        print(str(i) + ".volver")
        print("........................................................")
        x=input()

        if x.isdigit():
            x = int(x)
            if x< casillas.cant and x>=0:
                
                return casillas.getPos(int(x))
            elif x==i:
                print("Volviendo")
                return False
            else:
                print("Seleccione una opción válida")
                continue
        else:
            print("Seleccione una opción válida")
            continue
    pass




print("........................................................")
print("Ingrese la ruta del archivo")
print("........................................................")
ruta = input()
cargarArchivo("Entrada0.xml")

menu()
    
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