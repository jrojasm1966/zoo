'''
Asignatura: Zoo
Objetivos:
Practica la utilización de la herencia
Más práctica con asociaciones entre clases.
Practica métodos primordiales
Mira el polimorfismo en acción
Imagina un juego donde puedes crear un zoológico y comenzar a criar diferentes tipos de animales. Digamos que por cada zoológico 
que crees puede haber varios animales diferentes. Comience creando una clase Animal y luego al menos 3 clases específicas de 
animales que hereden de Animal. (Tal vez leones, tigres y osos, ¡Dios mío!) Cada animal debe tener al menos un nombre, una edad, 
un nivel de salud y un nivel de felicidad. La clase Animal debe tener un método display_info que muestre el nombre, la salud y la 
felicidad del animal. También debe tener un método de alimentación que aumente la salud y la felicidad en 10.

En al menos una de las clases de Animal child que ha creado, agregue al menos un atributo único. Dele a cada animal diferentes 
niveles predeterminados de salud y felicidad. Los animales también deben responder al método de alimentación con diferentes 
niveles de cambios en la salud y la felicidad.

Una vez que haya probado sus diferentes animales y se sienta más cómodo con la herencia, cree una clase de zoológico para ayudar 
a manejar a todos sus animales.

Una forma de armar este zoológico es haciendo lo siguiente:
'''
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
        return None
        
    def add_lion(self):
        self.animals.append(Leon(0))
        return self
        
    def add_tiger(self):
        self.animals.append(Tigre(0))
        return self
        
    def add_bear(self):
        self.animals.append(Oso(0))
        return self
        
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for a in range(0,len(self.animals)):
            self.animals[a].display_info()
        return self

class Animal:
    def __init__(self):
        self.nombre = input("Ingrese nombre: ")
        self.edad = input("Ingrese Edad: ")
        self.peso = input("Ingrese Peso: ")
        self.nivsalud = 100
        self.nivfeliz = 50
        self.nivferoz = 75
            
    def display_info(self):
        print("******************************")
        print("****** Datos Animales ********")
        print("******************************")
        print("Nombre : ", self.nombre)
        print("Edad : ", self.edad)
        print("Peso : ", self.peso)
        print("Nivel Salud : ", self.nivsalud)
        print("Nivel Felicidad : ", self.nivfeliz)
        print("******************************")
        return self

    
class Leon(Animal):
    def __init__(self, num):
        super().__init__()
        self.tipo = "León"
        num = alimentaHoy(num)
        
        if num == 1:
            self.nivsalud += 10
            self.nivfeliz += 4
            self.nivferoz += 5
        else:
            self.nivsalud -= 20
            self.nivfeliz -= 8
            self.nivferoz -= 10
            
    def display_info(self):
        super().display_info()
        print("Tipo Animal : ", self.tipo)
        print("Nivel Ferocidad : ", self.nivferoz)
        print("******************************")
        return self
            
class Tigre(Animal):
    def __init__(self, num):
        super().__init__()
        self.tipo = "Tigre"
        num = alimentaHoy(num)
        
        if num == 1:
            self.nivsalud += 8
            self.nivfeliz += 3
            self.nivferoz += 4
        else:
            self.nivsalud -= 16
            self.nivfeliz -= 6
            self.nivferoz -= 8

    def display_info(self):
        super().display_info()
        print("Tipo Animal : ", self.tipo)
        print("Nivel Ferocidad : ", self.nivferoz)
        print("******************************")
        return self
                        
class Oso(Animal):
    def __init__(self, num):
        super().__init__()
        self.tipo = "Oso"
        num = alimentaHoy(num)
        
        if num == 1:
            self.nivsalud += 6
            self.nivfeliz += 2
            self.nivferoz += 3
        else:
            self.nivsalud -= 12
            self.nivfeliz -= 4
            self.nivferoz -= 6
            
    def display_info(self):
        super().display_info()
        print("Tipo Animal : ", self.tipo)
        print("Nivel Ferocidad : ", self.nivferoz)
        print("******************************")
        return self


# ***************************************************************************************
# Función ingresaAnimal(num) 
# ***************************************************************************************
def ingresaAnimal(num):
    print('')
    print("***************************************")
    print("* Menú de Animales a Ingresar a Zoo   *")
    print("***************************************")
    print('')
    print("1.- Agregar León")
    print("2.- Agregar Tigre")
    print("3.- Agregar Oso")
    print("0.- Para SALIR ingrese 0 ( Cero )")
    print('')   
    num = int(input("Ingrese Opción : "))
    print('')   

    return num

# ***************************************************************************************
# Función si alimenta animal hoy 
# ***************************************************************************************
def alimentaHoy(num):
    num = 0
    respuesta = True
    
    while respuesta:
            num = int(input("Alimenta Hoy 1 ó 2 veces al Animal? : "))
            if num > 0 and num < 3:
                respuesta = False
            else: 
                print("")
                print("********************************************")
                print("ERROR : ¡¡¡¡ Opción ingresada NO EXISTE !!!!")
                print("----------¡¡ Ingresa nuevamente !!----------")
                print("********************************************")
                print("")
    return num

# ***************************************************************************************
# Función Principal cicloIngresaAnimalesZoo() que controla mantener usuario en programa
# ***************************************************************************************
def cicloIngresaAnimalesZoo():
    num = 0
    respuesta = True
    
    while respuesta:
            num = ingresaAnimal(num)
            if num == 0:
                respuesta = False
            else:
                if num > 0 and num < 4:
                    if num == 1:
                        zoo1.add_lion()
                    elif num == 2:
                        zoo1.add_tiger()
                    elif num == 3:
                        zoo1.add_bear()
                    
                    print("")
                else: 
                    print("")
                    print("********************************************")
                    print("ERROR : ¡¡¡¡ Opción ingresada NO EXISTE !!!!")
                    print("----------¡¡ Ingresa nuevamente !!----------")
                    print("********************************************")
                    print("")

# **************************************************
# Funciones Principales y Término de Programa
# **************************************************


# Zoologico Creado
zoo1 = Zoo("Mi Zoo de Animales")
cicloIngresaAnimalesZoo()

zoo1.print_all_info()

print("*************************")
input("Presione ENTER para salir")
print("*************************")
print(" ¡¡¡¡ Hasta Pronto !!!!  ")
print("*************************")

