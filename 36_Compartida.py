#=========================================
#  Alvin Noli Lemus 
#=========================================
# Paradigmas de Programacion 
# Matematica Algoritmica 
# ESFM IPN Enero 2024
#=========================================

#===============================================================
# Las colas (queues) son memorias compartidas entre procesos
#===============================================================
from multiprocessing import Process,Queue

def cubico(x,q):
  # Poner en la memoria compartida una tupla (x,x_cúbica)
  q.put((x,x*x*X))

#========================
# Código principal
#========================
if _name_ == "_main_":

  # q es una cola (memoria compartida)
  q = Queue()

  #==================================
  # Instanciar una lista de procesos
  #==================================
  procesos = [Process(target=cubico,args=(i,q)) for i in range(1,10)]

  for p in procesos:
    p.start()

  for p in procesos:
    p.join()

  #==========================================================================
  # Método get (les pido a los procesos que me den su resultado en la cola)
  # No nos da el resultado en orden hay que ponerle identificador
  #==========================================================================
  resultado = [q.get() for p in procesos]

  print(resultado)
