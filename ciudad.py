class ciudad():

    def __init__(self,nombre,filas,columnas,tablero,unidadesMilitares,entradas,recursos,civiles) -> None:
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.tablero = tablero
        self.unidadesMilitares = unidadesMilitares
        self.entradas = entradas
        self.recursos = recursos
        self.civiles = civiles
        self.colocarMilitares()

        pass

    def imprimirTablero(self):
        txt=""
        for i in range(self.filas):
            for j in range(self.tablero.getPos(i).cant):
                txt+=self.tablero.getPos(i).getPos(j)
            
            txt+="\n"

        print(txt)

    def colocarMilitares(self):
        for i in range(self.unidadesMilitares.cant):
            self.tablero.getPos(self.unidadesMilitares.getPos(i).fila-1).remplazar("M",self.unidadesMilitares.getPos(i).columna-1)

        