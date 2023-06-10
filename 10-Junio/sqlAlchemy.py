from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker,relationship

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    edad = Column(Integer)
    vehiculos = relationship("Vehiculo", back_populates="dueño")

class Vehiculo(Base):
    __tablename__ = 'vehiculo'
    id = Column(Integer, primary_key=True)
    marca = Column(String)
    modelo = Column(String)
    anio = Column(Integer)
    dueño_id = Column(Integer, ForeignKey('usuario.id'))
    dueño = relationship("Usuario", back_populates="vehiculos")


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
    
    def insertar_vehiculo(self, marca, modelo, anio, dueño_id):
        vehiculo = Vehiculo(marca=marca, modelo=modelo, anio=anio, dueño_id=dueño_id)
        self.session.add(vehiculo)
        self.session.commit()
        print("Vehiculo insertado correctamente.")
    def obtener_vehiculos(self):
        vehiculos = self.session.query(Vehiculo).all()
        return vehiculos
    
        
if __name__ == "__main__":
    bd_manager = BaseDatos()
    bd_manager.conectar()
    bd_manager.insertar_usuario('Juan', 'Perez', 25)
    bd_manager.insertar_usuario('Maria', 'Gomez', 35)
    bd_manager.insertar_usuario('Pedro', 'Lopez', 45)
    bd_manager.insertar_usuario('Ana', 'Gutierrez', 30)
    bd_manager.insertar_usuario('Luis', 'Garcia', 40)
    bd_manager.actualizar_usuario(1, 'Juan', 'Perez', 26)
    bd_manager.eliminar_usuario(4)
    usuarios = bd_manager.obtener_usuarios()
    for usuario in usuarios:
        print(usuario.nombre, usuario.apellido, usuario.edad)
    bd_manager.actualizar_usuario(1, 'Juan', 'Perez', 26)
    bd_manager.insertar_vehiculo('Ford', 'Fiesta', 2019, 1)
    bd_manager.cerrar_conexion()
