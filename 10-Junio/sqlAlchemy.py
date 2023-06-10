from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    edad = Column(Integer)

class BaseDatos:
    def __init__(self):
        self.engine = create_engine('sqlite:///data/10-Junio.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
    
    def conectar(self):
        self.session = self.Session()
    
    def cerrar_conexion(self):
        self.session.close()
    
    def insertar_usuario(self, nombre, apellido, edad):
        usuario = Usuario(nombre=nombre, apellido=apellido, edad=edad)
        self.session.add(usuario)
        self.session.commit()
        print("Usuario insertado correctamente.")
    def obtener_usuarios(self):
        usuarios = self.session.query(Usuario).all()
        return usuarios
    def actualizar_usuario(self, id, nombre, apellido, edad):
        usuario = self.session.query(Usuario).get(id)
        usuario.nombre = nombre
        usuario.apellido = apellido
        usuario.edad = edad
        self.session.commit()
        print("Usuario actualizado correctamente.")
    def eliminar_usuario(self, id):
        usuario = self.session.query(Usuario).get(id)
        self.session.delete(usuario)
        self.session.commit()
        print("Usuario eliminado correctamente.")
    def eliminar_usuarios(self):
        self.session.query(Usuario).delete()
        self.session.commit()
        print("Usuarios eliminados correctamente.")
    def consultar_usuario(self, id):
        usuario = self.session.query(Usuario).get(id)
        return usuario
        
if __name__ == "__main__":
    bd_manager = BaseDatos()
    bd_manager.conectar()
    bd_manager.insertar_usuario('Juan', 'Perez', 25)
    bd_manager.insertar_usuario('Maria', 'Gomez', 35)
    bd_manager.insertar_usuario('Pedro', 'Lopez', 45)
    bd_manager.insertar_usuario('Ana', 'Gutierrez', 30)
    bd_manager.insertar_usuario('Luis', 'Garcia', 40)
    bd_manager.actualizar_usuario(1, 'Juan', 'Perez', 26)
    bd_manager.eliminar_usuario(2)
    usuarios = bd_manager.obtener_usuarios()
    for usuario in usuarios:
        print(usuario.nombre, usuario.apellido, usuario.edad)
    bd_manager.actualizar_usuario(1, 'Juan', 'Perez', 26)
    bd_manager.cerrar_conexion()
