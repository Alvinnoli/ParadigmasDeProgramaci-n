#=========================================
#  Alvin Noli Lemus 
#=========================================
#
# Paradigmas de Programacion 
# Matematica Algoritmica 
# ESFM IPN Septiembre 2023
#
#=========================================


#=========================================
# Programacion Orientada a Objetos
#=========================================


#=========================================
# Una clase para un objeto vacio 
# No estaba tan vacio, necesita
# la palabra pass=pasar
#=========================================
class ObjetoVacio:
    pass

#=========================================
# La clase llanta
#=========================================
class Llanta:
    #=====================================
    # VAriable cuenta es de toda la clase
    #=====================================
    cuenta = 0
    #=====================================
    # Funcion constructora de identidad 
    # ___init__ es una funcion reservada 
    # comienza con uno mismo: self
    # pero puede ser otro nombre (mi)
    # parametros de entrada = default 
    #=====================================
    def __init__(mi,radio=50, ancho=30, presión=1.5):
        # variable de la estructura completa llanta 
        Llanta.cuenta += 1
        # variables exclusivas de cada objeto
        mi.radio =radio 
        mi.ancho = ancho 
        mi.presión =presión 

#========================================
# Objetos (instanciados)
#========================================
llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(presión=1.2)
llanta3 = Llanta()
llanta4 = Llanta(40,30,1.6)

#========================================
# OBjeto de contiene otros objetos 
#========================================
class Coche:
    def __init__(mi,ll1,ll2,ll3,ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3
        mi.llanta4 = ll4

micoche = Coche(llanta1, llanta2, llanta3, llanta4)

print("Total de llantas: ", Llanta.cuenta) #Variable global de la clase 
print("Presion de la llanta 4 = ", llanta4.presión)  # Presión de la llanta 4
print("Radio de la llanta 4 = ", llanta4.radio)
print("Radio de la llanta 3 = ", llanta3.radio)
print("Presion de la llanta 1 de mi coche = ", micoche.llanta1.presión)

#========================================
# Encapsulamiento 
#========================================

#========================================
# Uso de la funcion de python property para poner y obtener atributos
#========================================
class Estudiante: 
    def __init__(mi):
        mi.__nombre = ' '
    def ponerme_nombre(mi, nombre): 
        print('se llamó a ponerme_nombre')
        mi.__nombre= nombre
    def obtener_nombre(mi):
        print ('se llamó a obtener_nombre')
        return mi.__nombre 
    nombre=property(obtener_nombre,ponerme_nombre)

#========================================
# Crear objeto estudiante sin nombre 
#========================================
estudiante = Estudiante()

#========================================
# Ponerle nombre usando la propiedad nombre y el metodo ponerme_nombre 
# (sin tener que llamar explicitamente a la función)
#========================================
estudiante.nombre = "Diego" 

#========================================
# Obtener el nombre con el metodo obtener nombre 
# __nombre es una variable encapsulada (no visible desde afuera) 
# (sin tener que llamar explícitamente a la funcion obtener_nombre)
#=======================================
print(estudiante. nombre)

# Esto no funciona 
#print(estudiante.__nombre 

#=======================================
# Herencia de clases
#=======================================
class Cuadrilatero:
    def __init__ (mi,a,b,c,d):
        mi.lado1=a 
        mi.lado2=b
        mi.lado3=c
        mi.lado4=d

    def perimetro(mi):
        p=mi.lado1 + mi.lado2 + mi.lado3 + mi.lado4
        print ("perimetro=", p)
        return p 
#=======================================
# Su hijo  rectangulo 
# Rectangulo es hijo de cuadrilatero
# Rectangulo(cuadrilatero)
#=======================================
class Rectangulo (Cuadrilatero): 
    def __init__ (self, a, b):
        #====================================
        # Constructor de su madre
        #====================================
        super().__init__(a,b,a,b)
#====================================
# Su nieto cuadrado 
# Hijo de rectangulo 
#====================================
class Cuadrado(Rectangulo):
    def __init__(self, a):
        super().__init__(a,a)

    def area(self):
        area = self.lado1**2
        return area 

    #def perimetro(self):
    #   p=4.0*self.lado1 
    #   print("perimetro =",p)
    #   return p

#======================================
# Crear un cuadrado 
#======================================
cuadrado1 = Cuadrado(5)

#=========================================================
# Llamar al método perímetro de su abuelo cuadrilatero
#=========================================================
perimetro1 = cuadrado1.perimetro() 

#=======================================
# Llamar a su propio método área
#=======================================
area1 = cuadrado1.area()

print("Perímetro =", perimetro1)
print("Area = ", area1)

#==============================================================
# Sobre-escribir un método de su madre o abuela o tatarabuela.....
# Es volver a definir una función ya existente
#==============================================================
