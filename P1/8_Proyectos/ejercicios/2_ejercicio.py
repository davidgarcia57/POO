'''
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__
Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados.
Llammar a la clase Calculadora
'''

'''
num1=input("Ingrese numero 1")
num2=input("Ingrese numero 2")

class Calculadora():
    def __init__(self):
        self.result=0

    def suma(self,numero,numero2):
        self.resultado=numero+numero2

    def resta(self,numero,numero2):
        self.resultado=numero-numero2

    def multiplicacion(self,numero,numero2):
        self.resultado=numero*numero2

    def division(self,numero,numero2):
        self.resultado=numero/numero2

calcular=Calculadora()
calcular.suma((num1,num2))
print(self.result)
calcular.resta((num1,num2))
print(self.result)
calcular.multiplicacion((num1,num2))
print(self.result)
calcular.division(int(num1,num2))
print(self.result)
'''

class Calculadora():
    def __init__(self):
        self._numero1=int(input("Ingrese numero 1: "))
        self._numero2=int(input("Ingrese numero 2: "))

    @property
    def numero1(self):
        return self._numero1
    @numero1.setter
    def numero1(self, valor):
        self._numero1=valor
    @property
    def numero2(self):
        return self._numero2
    @numero2.setter
    def numero2(self, valor):
        self._numero2=valor

    def sumar(self):
        return self._numero1+self._numero2
    
    def restar(self):
        return self._numero1-self._numero2
    
    def multiplicar(self):
        return self._numero1*self._numero2
    
    def dividir(self):
        return self._numero1/self._numero2


operacion=Calculadora()

print(f"{operacion.numero1}+{operacion.numero2} = {operacion.sumar()}")
print(f"{operacion.numero1}-{operacion.numero2} = {operacion.restar()}")
print(f"{operacion.numero1}*{operacion.numero2} = {operacion.multiplicar()}")
print(f"{operacion.numero1}/{operacion.numero2} = {operacion.dividir()}")