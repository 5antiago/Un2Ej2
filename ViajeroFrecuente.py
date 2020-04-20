class ViajeroFrecuente:
    __NumViajero = int
    __DNI = str
    __Nombre = str
    __Apellido = str
    __Millas = int

    def __init__(self, Num, Dni, nom, apellido, millas):
        self.__NumViajero = Num
        self.__DNI = Dni
        self.__Nombre = nom
        self.__Apellido = apellido
        self.__Millas = millas
    def CantidadTotaldeMilla(self):
        return self.__Millas
    def acumularMillas(self, millas):
        if type(millas) == int:  
            self.__Millas += millas
    def CanjerMillas(self, millascanjear):
        if type(millascanjear) == int:  
            if self.__Millas < millascanjear:
                return False
            else:
                self.__Millas -= millascanjear
                return True
    def getnum(self):
        return self.__NumViajero

