from lista import lista

class pila(lista):

    def __init__(self) -> None:
        super().__init__()

    def append(self,dato):
        super().agregar_Final(dato)

    def pop(self):
        dato =super().eliminarPos(self.cant-1)
        return dato