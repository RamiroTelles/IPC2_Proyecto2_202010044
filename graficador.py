
def crearGrafica(tablero):
    inicio ="""
digraph cuadro{

    node[shape=box style=filled]
    subgraph laberinto{
        edge[color="white" ,fillcolor="white"]

    """
    cuerpo=""
    final=""

    #Crear todos los nodos
    for i in range(tablero.cant):
        for j in range(tablero.getPos(0).cant):
                cuerpo+="nodo" + str(i) +"_"+ str(j) + "[label=\"\", group=" + str(j) + ","
                if tablero.getPos(i).getPos(j) == '*':
                    cuerpo+=" fillcolor=black]\n"
                elif tablero.getPos(i).getPos(j) == 'C':
                    cuerpo+=" fillcolor=blue]\n"
                elif tablero.getPos(i).getPos(j) == 'R':
                    cuerpo+=" fillcolor=gray]\n"
                elif tablero.getPos(i).getPos(j) == 'E':
                    cuerpo+=" fillcolor=green]\n"
                elif tablero.getPos(i).getPos(j) == 'M':
                    cuerpo+=" fillcolor=red]\n"
                elif tablero.getPos(i).getPos(j) == 'P':
                    cuerpo+=" fillcolor=yellow]\n"
                elif tablero.getPos(i).getPos(j) == ' ':
                    cuerpo+=" fillcolor=white]\n"
                else:
                    cuerpo = cuerpo[:-1]
                    cuerpo+="]\n"
        cuerpo+="\n"
        cuerpo+="\n"        

    #Enlazar todas las filas

    #for i in range(tablero.cant):
    #    for j in range(tablero.getPos(0).cant-1):
    #        cuerpo+="nodo" +str(i) + str(j) + " -> nodo" + str(i)+ str(j+1)+"\n"
    #    cuerpo+="\n"
    #    cuerpo+="\n"
            

    #Enlazar todas las columnas
    for j in range(tablero.getPos(0).cant):
        for i in range(tablero.cant-1):
            cuerpo+="nodo"+ str(i) +"_"+ str(j) + " -> nodo"+ str(i+1) +"_"+ str(j)+"\n" 

        cuerpo+="\n"
        cuerpo+="\n"

    #Poner las filas en su lugar
    for i in range(tablero.cant):
        cuerpo+="{rank=same; "
        for j in range(tablero.getPos(0).cant):
            cuerpo+=" nodo"+ str(i) +"_"+ str(j)+ " ,"
            
        cuerpo = cuerpo[:-1]
        cuerpo+="}\n"
        cuerpo+="\n"

    final="""
    }

}"""
    doc = inicio + cuerpo + final

    try:
        myfile = open("grafica.dot","w")

        myfile.write(doc)
        myfile.close
        #"dot -Tpng grafica.dot -o grafica.png"
        

        #dot -Tpng C:\Users\ramir\Desktop\grafica.dot -o grafica.png
       
    except:
        print("error")