import os
os.system("cls")

class Coches:

    #Atributos o propiedades(variables)
    #Caracteristicas del coche
    #Valores Iniciales
    #Metodo constructor, Con este metodo se inicializan los atributos o propiedades de la clase
    def __init__(self,__marca, __color, __modelo, __velocidad, __caballaje, __plazas):
        self.__marca=""
        self.__color=""
        self.__modelo=""
        self.__velocidad=0
        self.__caballaje=0
        self.__plazas=0

    #Crear los metodos setters y getters, estos modelos son importantes y necesarios
    # en todas las clases que el programador interactue con los valores de los atributos a traves
    # de estos metodos digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar
    # un valor (set) a un atributo en particular de a clase a traves de un objeto
    # Los metodos get siepre regresan valor, es decir el valor de la propiedad a traves del return
    # Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

    def getMarca(self):
        return self.__marca
    
    def setMarca(self,__marca):
        self.__marca=__marca

    def getColor(self):
        return self.__color
    
    def setColor(self,__color):
        self.__color=__color

    def getModelo(self):
        return self.__modelo
    
    def setModelo(self,__modelo):
        self.__modelo=__modelo
    
    def getVelocidad(self):
        return self.__velocidad
    
    def setVelocidad(self,__velocidad):
        self.__velocidad=__velocidad
    
    def getCaballaje(self):
        return self.__caballaje
    
    def setCaballaje(self,__caballaje):
        self.__caballaje=__caballaje
    
    def getPlazas(self):
        return self.__plazas

    def setPlazas(self,__plazas):
        self.__plazas=__plazas

    #Metodos o acciobes o funciones que hace el objeto
    def acelerar(self):
        pass

    def frenar(self):
        pass


    #Crea un objeto o instancia de la clase Coches

#Mulltiples objetos
coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda","","",0,0,0)

#Utiliza los metodos get para obtener los valores de las propiedades o atributos del objeto coche1
print(f'''
Marca: {coche1.getMarca()}
Color: {coche1.getColor()}
Modelo: {coche1.getModelo()}
Velocidad: {coche1.getVelocidad()}
Caballaje: {coche1.getCaballaje()}
Plazas: {coche1.getPlazas()}
''')

print(f'''
Marca: {coche2.getMarca()}  
Color: {coche2.getColor()}
Modelo: {coche2.getModelo()}
Velocidad: {coche2.getVelocidad()}
Caballaje: {coche2.getCaballaje()}
Plazas: {coche2.getPlazas()}
''')

print(f'''
Marca: {coche3.getMarca()}
''')


