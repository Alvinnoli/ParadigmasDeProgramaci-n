from aplicacion.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario 

#==================================================
# Para llenar la interface hay que heredar la clase
#==================================================
class BaseDeDatos(RepositorioDeUsuarios):
    _host: str 
    _user: str 
    _password: str 
    def _init_(mi,host:str, user:str, password:str): 
        mi._host = host 
        mi._user = user
        mi._password = password 

    def abrir(mi) -> None:
        print(f"Abriendo la conexión a la base de datos: {mi._host}:{mi._user}"@{mi._password})

    def guardar(mi, usuario:Usuario)  ->None:
        userElements = {"nombre": usuario.GetNombre(),
                        "apellido": usuario.GetApellido(),
                        "edad": usuario.GetEdad()}
        print(f"Guardando el usuario en la base de datos {usuario.getNombre()}\n")
        print(f"INSERTAR DATOS DEL USUARIO ('{userElements['nomnre']}','{userElements['Apellido']}',{userElements['edad']})")

    def cerrar(mi)  -> None:
        print("Cerrando la conexión")
