from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositorio de usuarios import RepositorioDeUsuarios

#==============================
# Clase ManejoDeInscripciones
# NO TIENE VARIABLES!!!!
#==============================
class ManejoDeIncripciones:
    #================================================================
    # Decorador staticmethod
    # El objeto sólo tiene la función inscribirUsuario
    # ENVUELVE LA FUNCION SIN LLAMAR VARIABLES LOCALES
    # el objeto ManejoDeInscripciones es la interface intercambiable
    #================================================================
    @staticmethod
    def inscribirUsuario(usuario: Usuario, repostiorioDeUsuarios: RepositorioDeUsuarios) -> None:
        print("---------> Guardando usuario ... \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()
