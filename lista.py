from re import I
#from numpy import true_divide


from nodo import nodo

class lista:

    def __init__(self) -> None:
        self.inicio = None
        self.cant = 0
        self.vacio = True

    def agregar_inicio(self,dato):
        nuevo = nodo(dato)
        if self.vacio:
            self.inicio = nuevo
            self.cant+=1
            self.vacio = False
        else:
            self.inicio.anterior = nuevo
            nuevo.siguiente = self.inicio
            self.inicio = nuevo
            self.cant +=1
        
    def agregar_Final(self,dato):
        nuevo = nodo(dato)
        if self.vacio:
            self.inicio = nuevo
            self.cant+=1
            self.vacio = False
        else:
            aux = self.inicio

            while(aux.siguiente != None):
                aux = aux.siguiente
            aux.siguiente = nuevo
            nuevo.anterior = aux
            self.cant +=1
        
    
    def remplazar(self,dato,pos):
        nuevo = nodo(dato)
       # if pos == 0:
       #     self.agregar_inicio(dato)

       #     pass
       # elif pos ==(self.cant-1):
        #    self.agregar_Final(dato)
       #     pass
        if self.vacio:
            print("Lista Vacia")
        elif pos==0:
            aux = self.inicio
            #nose porque esta el 0 en ese if, pero funciona     
            if aux.siguiente!=0:
                nuevo.siguiente = aux.siguiente
                aux.siguiente.anterior = nuevo
                self.inicio= nuevo
            else:
                self.inicio = nuevo
        elif pos == (self.cant-1):
            aux = self.inicio
            i=0
            while (i<pos):
                aux = aux.siguiente
                i+=1
            nuevo.anterior = aux.anterior
            aux.anterior.siguiente = nuevo
        elif (pos)<=(self.cant-1):

            aux = self.inicio
            i=0
            while (i<pos):
                aux = aux.siguiente
                i+=1
            aux.siguiente.anterior = nuevo
            nuevo.siguiente = aux.siguiente
            aux.anterior.siguiente = nuevo
            nuevo.anterior = aux.anterior
            self.vacio = False
            pass
        else:
            print("Posicion no existente")

    def buscar(self,dato):
        if self.vacio:
            print("Lista Vacia")
        else:
            aux = self.inicio
            i=0 
            if aux.dato == dato:
                return i
            else:
                while(aux.siguiente != None):
                    aux = aux.siguiente
                    i+=1
                    if aux.dato == dato:
                        return i
            return None

    def eliminarPos(self,pos):
        if pos<=(self.cant-1):
            aux = self.inicio
            i=0
            while(i<pos):
                aux = aux.siguiente
                i+=1
            if aux.anterior!= None:
                aux.anterior.siguiente = aux.siguiente
                if aux.siguiente != None:
                    aux.siguiente.anterior = aux.anterior
                else:
                    pass
            else:
                if self.cant==1:
                    self.inicio=None
                    self.vacio=True
                    
                    pass
                else:
                    aux.siguiente.anterior = aux.anterior
                    self.inicio = aux.siguiente
            self.cant-=1
            return aux.dato
        else:
            print("posicion no existente")
            return None

    def eliminarDato(self,dato):
        if self.vacio:
            print("Lista Vacia")
        else:
            aux = self.inicio
            i=0
            if aux.dato == dato:
                if aux.siguiente != None:
                    aux.siguiente.anterior = None
                    self.inicio = aux.siguiente
                    self.cant-=1
                    return True
                else:
                    self.cant-=1
                    self.vacio=True
                    self.inicio=None
                    pass
            else:
                while(aux.siguiente != None):
                    aux = aux.siguiente
                    i+=1
                    if aux.dato == dato:
                        aux.anterior.siguiente = aux.siguiente
                        if aux.siguiente != None:
                            aux.siguiente.anterior = aux.anterior
                        
                        self.cant-=1

                        return True
            return False
    
    def imprimir(self):
        if self.vacio:
            print("Lista Vacia")
        else:
            aux = self.inicio
            txt = "[ " + str(aux.dato)
            while(aux.siguiente!=None):
                aux = aux.siguiente
                txt+= ", " + str(aux.dato)
            txt+=" ]"
            print(txt)
        
    def getPos(self,pos):
        if self.vacio:
            print("Lista Vacia")
        elif pos<=(self.cant-1):
            aux = self.inicio
            i=0
            while(i<pos):
                aux = aux.siguiente
                i+=1
            return aux.dato
        else:
            #print("Posicion no válida")
            pass

    
