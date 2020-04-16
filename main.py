import csv

import ViajeroFrecuente



if __name__ == "__main__":
    
    archivo = open("Viajeros.csv")
    reader = csv.reader(archivo, delimiter=",")
    viajeros = []
    bandera = True
    for linea in reader:
        if bandera:
            bandera = False
        else:
            viajeros.append(ViajeroFrecuente.ViajeroFrecuente(int(linea[0]),linea[1],linea[2], linea[3], int(linea[4])))
    numviajero = int(input("Ingrese Numero de Viajero a Buscar: "))
    i=0
    tamanolista = len(viajeros)
    while i < tamanolista and viajeros[i].getnum() != numviajero:
        i+=1

    if i == len(viajeros):
        print("No se encotro el Viajero")
    else: 
        op=input(" 1. Consultar millas \n 2. Acumular millas \n 3. Canjera millas \n 0. Salir \n Ingrese su opcion: ")
        while op !="0":
            if op =="1":
                print("El viajero posee {} millas".format(viajeros[i].CantidadTotaldeMilla()))
            elif op =="2":
                viajeros[i].acumularMillas(int(input("Ingrese millas a acumular: ")))
            elif op =="3":
                if viajeros[i].CanjerMillas(int(input("Ingrese millas a canjear: "))):
                    print("Millas canjeadas exitosamente")
                else:
                    print("No posee suficiente millas")
            else:
                print("Opcion incorrecta")
            op=input("1. Consultar millas \n 2. Acumular millas \n 3. Canjera millas \n 0. Salir \n Ingrese su opcion: ")
        