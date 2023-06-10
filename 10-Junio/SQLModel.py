from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    apellido: str
    edad: int
    email: str

class BaseDatos:
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        SQLModel.metadata.create_all(self.engine)
    
    def crear_usuario(self, nombre: str, apellido: str, edad: int, email: str):
        usuario = Usuario(nombre=nombre, apellido=apellido, edad=edad, email=email)
        with Session(self.engine) as session:
            session.add(usuario)
            session.commit()
    
    def obtener_usuarios(self):
        with Session(self.engine) as session:
            statement = select(Usuario)
            results = session.exec(statement)
            return results
    
    def actualizar_usuario(self, usuario_id: int, nombre: str):
        with Session(self.engine) as session:
            statement = select(Usuario).where(Usuario.id == usuario_id)
            results = session.exec(statement)
            usuario = results.one()
            usuario.nombre = nombre
            session.add(usuario)
            session.commit()
    
    def eliminar_usuario(self, usuario_id: int):
        with Session(self.engine) as session:
            statement = select(Usuario).where(Usuario.id == usuario_id)
            results = session.exec(statement)
            usuario = results.one()
            session.delete(usuario)
            session.commit()

def main():
    database_url = "sqlite:///database.db"
    bd = BaseDatos(database_url)
    
    bd.crear_usuario("Juan", "Perez", 25, "juan@example.com")
    bd.crear_usuario("Maria", "Gomez", 35, "maria@example.com")
    
    usuarios = bd.obtener_usuarios()
    for usuario in usuarios:
        print(usuario)
    
    bd.actualizar_usuario(1, "Juan Carlos")
    
    bd.eliminar_usuario(2)
    
    usuarios = bd.obtener_usuarios()
    for usuario in usuarios:
        print(usuario)

if __name__ == "__main__":
    main()
