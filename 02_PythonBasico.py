#==============================
#   Alvin NOli Lemus 
#==============================
#
#  Matemática Algoritmica
#  Paradigmas de programacion 
#  ESFM IPN Septiembre 2023
#
#=====================================================
# Input permite obtener datos del usario en prompter
#=====================================================
nombre = input("Dame tu nombre: ")
print("Hola como estás",nombre)

#========================================
# Los enteros son de precisión ilimitada
#========================================
y = 500000000000000000000000000000000
print(y)

#===============================================================
# La función delimitar números con guión bajo pero no con coma
#===============================================================
y = 5_000_000
print(y)

#====================================================
# La funcion int() cambia strings y floats a enteros
#====================================================
numero = int(input("Dame tu edad: "))
type(numero)

#======================================================
# La notación científica de flotantes utiliza e o E
#======================================================
# 1.2 x 10^{-9}
#================
y = 1.2E-9
print(y)

#==========================================================
# La unción float() convierte strgins y enteros a floats
#==========================================================
y = float("14.3")
print(y)

#===========================================================
# Los complejos se escriben con la raíz de menos uno 
# j siempre con n número como prefijo 
# no acepta la j suelta
#===========================================================
z = 1+1j

# suma + 
# resta - 
# multiplicación *
# division / 
# módulo % 
# exponente **
# // funcion piso
# Funciones para transormar números int() float() complex()
# Operaciones abs() round() pow() 

print(round(3.14159,4))

#==========================
# Strings de varias líneas
#==========================
parrafo = """ En el bosque de la china
 la chinita se perdió"""
print(parrafo)

#==============================================
# La función len() obtiene el tamaño del string
#==============================================
n=len(parrafo)
print(n)

#=============================================================
# Las letras en un string ocupan lugares como en un arreglo 
# (también de atrás para adelante comenzando en -1 el último)
#=============================================================
palabra = "hola"
print(palabra[0])
print(palabra[-4])
