#Instanciar los Objetos para posteriormente implementarlos.
from coches import *
import os
os.system("cls")

def borrarPantalla():
    os.system("cls")

def espereTecla():
    input("\n\t...Oprima una tecla para continuar...")

def imprimir_datos_vehiculos(marca,color,modelo,velocidad,potencia,plazas):
    print(f"Datos del Vehiculo \n Marca: {marca} \n Color: {color} \n Modelo: {modelo} \n Velocidad Maxima: {velocidad} \n Caballaje: {potencia} \n Numero de Plazas: {plazas}")

def datos_autos(tipo):
    borrarPantalla()
    print(f"\n\t...Ingresar los datos del Vehiculo de tipo {tipo}...")
    marca=input("Marca: ").upper()
    color=input("Color: ").upper()
    modelo=input("Modelo: ").upper()
    velocidad=int(input("Velocidad: "))
    potencia=int(input("Potencia: "))
    plazas=int(input("Numero de plazas: "))
    return marca,color,modelo,velocidad,potencia,plazas
    
def autos():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Auto")
    coche=Coches(marca,color,modelo,velocidad,potencia,plazas)
    imprimir_datos_vehiculos(coche.marca(),coche.color(),coche.modelo(),coche.velocidad(),coche.potencia(),coche.plazas())
    
def camionetas():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camioneta")
    traccion=input("Traccion: ").upper()
    cerrada=bool(input("¿Cerrada (Si/No)?: ")).upper().strip()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False
    camioneta=Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
    imprimir_datos_vehiculos(camioneta.marca(),camioneta.color(),camioneta.modelo(),camioneta.velocidad(),camioneta.potencia(),camioneta.plazas())
    print(f"Traccion: {camioneta.traccion()} \n Cerrada: {camioneta.cerrada()}")

def camiones():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camion")
    eje=int(input("Numero de Ejes: "))
    capacidadCarga=int(input("Capacidad de carga (Kg): "))
    camion=Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
    imprimir_datos_vehiculos(camion.marca(),camion.color(),camion.modelo(),camion.velocidad(),camion.potencia(),camion.plazas())
    print(f"Ejes: {camion.eje()} \n Capacidad de carga: {camion.capacidadCarga()} Kg")
    
def main():
    opcion=True
    while opcion:
        borrarPantalla()
        opcion=input("\n\t\t .::Menu Principal::.\n\t 1.-Autos\n\t 2.-Camionetas\n\t 3.-Camiones\n\t 4.-Salir\n\n\t Elige una opcion:")
        match opcion:
            case "1":
                borrarPantalla()
                autos()
                espereTecla()
            case "2":
                borrarPantalla()
                camionetas()
                espereTecla()
            case "3":
                borrarPantalla()
                camiones()
                espereTecla()
            case "4":
                borrarPantalla()
                input("\n\t\tSalir del Programa")
                opcion=False
            case _:
                borrarPantalla()
                print("\n\t...Opcion no valida, vuelva a itentarlo...")
                espereTecla()

if __name__=="__main__":
    main()