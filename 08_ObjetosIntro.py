#=========================================
#  Alvin NOli Lemus 
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
class Llanta
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
    del ___init__(mi,radio=50, ancho=30, presión=1.5):
        # variable de la estructura completa llanta 
        Llanta.cuenta += 1
        # variables exclusivas de cada objeto
        mi.radio =radio 
        mi.ancho = ancho 
        mi.presión =presión 

#========================================
# Objetos (instanciados)
#========================================
llanta1 = llanta(50,30,1.5)
llanta2 = llanta(presion=1.2)
llanta3 = llanta ()
llanta4 = lLanta(40,30,1.6)

#========================================
# OBjeto de contiene otros objetos 
#========================================
class Coche:
    def __init__(mi.ll1,ll2,ll3,ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3
        mi.llanta4 = ll4

micoche = Coche(llanta1, llanta2, llanta3, llanta4)

print("Total de llantas: ", Llanta.cuenta) #Variable global de la clase 
print("Presion de la llanta 4 = ", llanta4.presion)
print("Radio de la llanta 4 = ", llanta4.radio)
print("Radio de la llanta 3 = ", llanta3.radio)
print("Presion de la llanta 1 de mi coche = ", micoche, llanta1, presion)

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
