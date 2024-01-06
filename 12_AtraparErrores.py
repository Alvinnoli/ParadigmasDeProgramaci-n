#=========================================
#  Alvin Noli Lemus 
#=========================================
# Paradigmas de Programacion 
# Matematica Algoritmica 
# ESFM IPN Enero 2024
#=========================================

#===============================================================
# La clase ClienteBancario está en el dubdirectorio 
# aplicación/banco/
#===============================================================
from aplicacion.banco.cliente_bancario import ClienteBancario

#======================================================
# try: intenta (correr kas instrucciones)
# except: atrapar el error en una variable e
# e se puede convertir a string
#======================================================

#==================================================
# Error por sacar más dinero del que tiene
#==================================================
try:
  cliente = ClienteBancario("Jaime Andrade", "Hernández Sánchez", 28, 0.0)
  cliente.guardarDinero(300)
  print(cliente.imprimirInfo())
  cliente.retirarDinero(400)
  print(cliente.imprimirInfo())
#===============================================================
# Exception es el objeto más general de error 
#===============================================================
except Exception as e:
  print("Error: " + str(e))

#=======================================================
# Exception por usar un atributo privado
#=======================================================
try:
  print(cliente._nombres)
except Exception as ex:
  print("Error: " + str(ex))

#======================
# Forma correcta
#======================
print(cliente.nombres)

