import csv

import ViajeroFrecuente

import manejaviajeros


if __name__ == "__main__":
    viajeros = manejaviajeros.manejadorviajeros()

    archivo = open("Viajeros.csv")
    reader = csv.reader(archivo, delimiter=",")
    next(reader)

    for linea in reader:
        viajeros.agregarviajero(ViajeroFrecuente.ViajeroFrecuente(int(linea[0]),linea[1],linea[2], linea[3], int(linea[4])))

    numviajero = int(input("Ingrese Numero de Viajero a Buscar: "))
    id = viajeros.buscaviajero(numviajero)
    if  id == -1:
        print("No se encotro el Viajero")

    else: 

        #----MENU----#
        op=input(" 1. Consultar millas \n 2. Acumular millas \n 3. Canjera millas \n 0. Salir \n Ingrese su opcion: ")
        
        while op !="0":
            if op =="1":
                print("El viajero posee {} millas".format(viajeros.cantmillas(id)))
            elif op =="2":
                viajeros.acummillas(id, int(input("Ingrese millas a acumular: ")))
            elif op =="3":
                if viajeros.CanjearMillas(id, int(input("Ingrese millas a canjear: "))):
                    print("Millas canjeadas exitosamente")
                else:
                    print("No posee suficiente millas")
            else:
                print("Opcion incorrecta")
            op=input("1. Consultar millas \n 2. Acumular millas \n 3. Canjera millas \n 0. Salir \n Ingrese su opcion: ")
        