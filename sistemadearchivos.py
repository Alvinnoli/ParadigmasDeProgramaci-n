from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

#==============================================
# Implementa la interface RepositorioDeUsuarios
#==============================================
class SistemaDeArchivos(RepositorioDeUsuarios):
    _directorios: str

    def _init_(mi, directorio:str):
        mi._directorio = directorio

    def abrir(mi) -> None:
        print(f"Abrir directorio: {mi._directorio}")

    def guardar(mi, usuario:Usuario) -> None:
        xml = f"</root></name>{usuario.getNombe()}</name></lasName>{usuario.getApellido()</lasName></age>{usuario.getEdad()}</age></root}"
        print(f"Guardado usuario en el archivo : {mi._directorio}/{usuario.getNombre()}")  
        print(xml)

    def cerrar(mi)  -> None:
        print("Cerrando el archivo")
