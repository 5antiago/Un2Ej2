import ViajeroFrecuente

class manejadorviajeros:
    __array = list

    def __init__(self):
        self.__array = []
    def agregarviajero(self, viajero):
        if type(viajero) == ViajeroFrecuente.ViajeroFrecuente:
            self.__array.append(viajero)
            return True
        else:
            return False
    def buscaviajero(self, id):
        if type(id)==int:
            i=0
            tamanolista = len(self.__array)
            while i < tamanolista and self.__array[i].getnum() != id:
                i+=1
            if i == tamanolista:
                return -1
            else:
                return i
    def cantmillas(self, id):
        if type(id)==int:
            return self.__array[id].CantidadTotaldeMilla()
    def acummillas(self, id, millas):
        if type(id) == int and type(millas) == int:
            self.__array[id].acumularMillas(millas)
    def CanjearMillas(self, id, millas):
        if type(id) == int and type(millas) == int:
            return self.__array[id].CanjerMillas(millas)
    def testing(self):
        self.__array.append(ViajeroFrecuente.ViajeroFrecuente(1, "11122233", "Test", "Test", 4000))
        print(self.__array[-1].CantidadTotaldeMilla())
        print(self.__array[-1].getnum())
        self.__array[-1].acumularMillas("1560") #No acumula por ser str y no int
        print(self.__array[-1].CantidadTotaldeMilla())
        self.__array[-1].acumularMillas(1560)
        print(self.__array[-1].CantidadTotaldeMilla())