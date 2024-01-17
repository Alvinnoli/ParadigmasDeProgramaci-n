#===================
# Clase Usuario
#===================
class Usuario:
    _nombre: str
    _apellido: str 
    _edad:int

    #=====================
    # Constructor
    #=====================
    def __init__(mi,nombre:str, apellido:str, edad:int):
        mi._nombre = nombre 
        mi._apellido = apellido
        mi._edad = edad
    
    #=================
    # Getters
    #=================
    def getNombre(mi) ->str:
        return mi._nombre

    def getApellido(mi) ->str:
        return mi._apellido

    def getEdad(mi) -> int:
        return mi._edad 
