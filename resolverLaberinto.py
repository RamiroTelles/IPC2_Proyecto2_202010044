
from pila import pila
from lista import lista

def crearCopiaTablero(tablero):
    row=""
    copiaTablero = lista()
    fila = lista()

    for i in range(tablero.cant):
        row=""
        fila=lista()
        for j in range(tablero.getPos(0).cant):
            row+=tablero.getPos(i).getPos(j)
        for c in row:
            fila.agregar_Final(c)
        
        copiaTablero.agregar_Final(fila)
    
    return copiaTablero

        

def resolverElLaberinto(xInicial,yInicial,xFinal,yFinal,poderRobot,casillasMilitares,tabla):
    x= xInicial
    y= yInicial
    recorrido=pila()
    poder=0
    #Se crea una copia del tablero
    tablero = crearCopiaTablero(tabla)
    txt=""
    print("+}+}+}+}+}+}++}+}+}+}++}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+")
    for i in range(tablero.cant):
        for j in range(tablero.getPos(i).cant):
            txt+=tablero.getPos(i).getPos(j)
            
        txt+="\n"

    print(txt)
    print("+}+}+}+}+}+}++}+}+}+}++}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+")
    while True:
        posActual= lista()
        #if x==xFinal and y==yFinal:
        #    print("Se halló un camino")
        #    return recorrido
        poderIzquierda = obtenerPoder(casillasMilitares,x-1,y)
        poderDerecha = obtenerPoder(casillasMilitares,x+1,y)
        poderArriba = obtenerPoder(casillasMilitares,x,y+1)
        poderAbajo= obtenerPoder(casillasMilitares,x,y-1)
        if x+1==xFinal and y==yFinal:
            print("Se halló un camino")
            posActual.agregar_Final(x)
            posActual.agregar_Final(y)
            posActual.agregar_Final(poder)
            recorrido.append(posActual)
            tablero.getPos(x).remplazar('P',y)
            poder = poderDerecha
            x= x+1
            #poderRobot-=poder
            return recorrido
        elif x-1==xFinal and y==yFinal:
            print("Se halló un camino")
            posActual.agregar_Final(x)
            posActual.agregar_Final(y)
            posActual.agregar_Final(poder)
            recorrido.append(posActual)
            tablero.getPos(x).remplazar('P',y)
            poder = poderIzquierda
            x= x-1
            #poderRobot-=poder
            return recorrido
        elif x==xFinal and y+1==yFinal:
            print("Se halló un camino")
            posActual.agregar_Final(x)
            posActual.agregar_Final(y)
            posActual.agregar_Final(poder)
            recorrido.append(posActual)
            tablero.getPos(x).remplazar('P',y)
            poder = poderArriba
            y= y+1
            #poderRobot-=poder
            
            return recorrido
        elif x==xFinal and y-1==yFinal:
            print("Se halló un camino")
            posActual.agregar_Final(x)
            posActual.agregar_Final(y)
            posActual.agregar_Final(poder)
            recorrido.append(posActual)
            tablero.getPos(x).remplazar('P',y)
            poder = poderAbajo
            y= y-1
            #poderRobot-=poder
            return recorrido
        else:
            #Busca si las casillas adyacentes son de militares y cuanto poder tienen
            
            #Comprueba si puede transitar por la izquierda
            if (x-1>=0 and x-1<tablero.cant and tablero.getPos(x-1).getPos(y)!='R' and tablero.getPos(x-1).getPos(y)!='*' and tablero.getPos(x-1).getPos(y)!='X' and tablero.getPos(x-1).getPos(y)!='P' and poderIzquierda<poderRobot):
               
                posActual.agregar_Final(x)
                posActual.agregar_Final(y)
                posActual.agregar_Final(poder)
                recorrido.append(posActual)
                tablero.getPos(x).remplazar('P',y)
                poder = poderIzquierda
                x= x-1
                poderRobot-=poder
                continue
                  
            #comprueba si puede transitar por la derecha
            elif(x+1>=0 and x+1<tablero.cant and tablero.getPos(x+1).getPos(y)!='R' and tablero.getPos(x+1).getPos(y)!='*' and tablero.getPos(x+1).getPos(y)!='X' and tablero.getPos(x+1).getPos(y)!='P' and poderDerecha<poderRobot):
                posActual.agregar_Final(x)
                posActual.agregar_Final(y)
                posActual.agregar_Final(poder)
                recorrido.append(posActual)
                tablero.getPos(x).remplazar('P',y)
                poder = poderDerecha
                x= x+1
                poderRobot-=poder
                continue
                
            #comprueba si puede transitar por abajo
            elif(y-1>=0 and y-1<tablero.getPos(0).cant and tablero.getPos(x).getPos(y-1)!='R' and tablero.getPos(x).getPos(y-1)!='*' and tablero.getPos(x).getPos(y-1)!='X' and tablero.getPos(x).getPos(y-1)!='P' and poderAbajo<poderRobot):
                posActual.agregar_Final(x)
                posActual.agregar_Final(y)
                posActual.agregar_Final(poder)
                recorrido.append(posActual)
                tablero.getPos(x).remplazar('P',y)
                poder = poderAbajo
                y= y-1
                poderRobot-=poder
                continue 
                
            #comprueba si puede transitar por arriba
            elif(y+1>=0 and y+1<tablero.getPos(0).cant and tablero.getPos(x).getPos(y+1)!='R' and tablero.getPos(x).getPos(y+1)!='*' and tablero.getPos(x).getPos(y+1)!='X' and tablero.getPos(x).getPos(y+1)!='P' and poderArriba<poderRobot):
                posActual.agregar_Final(x)
                posActual.agregar_Final(y)
                posActual.agregar_Final(poder)
                recorrido.append(posActual)
                tablero.getPos(x).remplazar('P',y)
                poder = poderArriba
                y= y+1
                poderRobot-=poder
                continue
            elif recorrido.vacio:
                print("Mision imposible, no existe un camino")
                return recorrido
            else:
                tablero.getPos(x).remplazar('X',y)
                poderRobot+=poder
                pasoAnterior = recorrido.pop()
                x=pasoAnterior.getPos(0)
                y = pasoAnterior.getPos(1)
                poder = pasoAnterior.getPos(2)
                continue
                

            


    




def obtenerPoder(casillasMilitares,x,y):
    poder=0

    for i in range(casillasMilitares.cant):
        if (casillasMilitares.getPos(i).fila-1) == x:
            if (casillasMilitares.getPos(i).columna-1) == y:
                poder= casillasMilitares.getPos(i).poder

    return poder

def colocarRecorrido(laberinto,recorrido):
    for i in range(recorrido.cant):
        laberinto.getPos(recorrido.getPos(i).getPos(0)).remplazar('P',recorrido.getPos(i).getPos(1))

    return laberinto