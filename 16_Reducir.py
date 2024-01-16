#================================
#  Alvin Noli Lemus 
#================================
# Matematica Algoritmica 
# Paradigmas de programacion 
# ESFM IPN   Octubre 
#================================

#=========================================
# Uso de reducciones (Colapsar resultados)
#=========================================

#================================================
# Multiplicación de todos los números en la lista
#================================================

from functools import reduce

bigdata = [2,3,5,7,11,13,19,23,29]

#================
# Función x * y 
#================
multiplicar = lambda x,y: x*y

#================
# Función x + y
#================
suma = lambda x, y: x + y

print(reduce(multiplicar,bigdata))
print(reduce(suma,bigdata))

#============================================================================
# Reduce le aplica la función por pares a los resultados y 
# el siguiente elemento comenzando con los dos primeros elementos
#============================================================================

