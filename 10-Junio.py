import sqlite3  

class BaseDatos:    
    def __init__(self, nombre):
        self.nombre = "data/"+nombre
        self.conexion = None
    # Método para conectar a la base de datos
    def conectar(self):
        try:
            self.conexion = sqlite3.connect(self.nombre)
            print(f"Conexión exitosa a la base de datos {self.nombre}")
        except sqlite3.OperationalError as e:
            print(f"Ocurrió un error al conectar: {e}")
    
    def cerrar_conexion(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada")
            
    def crear_tabla(self, nombre, columnas):
        try:
            cursor = self.conexion.cursor()
            columnas_str = ', '.join(columnas)
            create_table_query = f"CREATE TABLE IF NOT EXISTS {nombre} ({columnas_str})"
            cursor.execute(create_table_query)
            self.conexion.commit()
            print("Tabla creada correctamente.")
        except sqlite3.Error as error:
            print("Error al crear la tabla:", error)
            
            
    def insertar(self, tabla, columnas, valores):
        try:
                cursor = self.conexion.cursor()
                columnas_str = ', '.join(columnas)
                valores_str = ', '.join(['?'] * len(valores))
                insert_query = f"INSERT INTO {tabla} ({columnas_str}) VALUES ({valores_str})"
                cursor.execute(insert_query, valores)
                self.conexion.commit()
                print("Datos insertados correctamente.")
            
        except sqlite3.Error as error:
            print("Error al insertar los datos:", error)
    
    def consultar(self, tabla, columnas=None, condicion=None):
        try:
            cursor = self.conexion.cursor()
            columnas_str = ', '.join(columnas) if columnas else '*'
            where_str = f" WHERE {condicion}" if condicion else ''
            select_query = f"SELECT {columnas_str} FROM {tabla}{where_str}"
            cursor.execute(select_query)
            return cursor.fetchall()
        except sqlite3.Error as error:
            print("Error al consultar los datos:", error)
    
    def actualizar(self, tabla, columnas, valores, condicion):
        try:
            cursor = self.conexion.cursor()
            set_str = ', '.join([f"{columna} = ?" for columna in columnas])
            where_str = f" WHERE {condicion}" if condicion else ''
            update_query = f"UPDATE {tabla} SET {set_str}{where_str}"
            cursor.execute(update_query, valores)
            self.conexion.commit()
            print("Datos actualizados correctamente.")
        except sqlite3.Error as error:
            print("Error al actualizar los datos:", error)
    
    def eliminar(self, tabla, condicion):
        try:
            cursor = self.conexion.cursor()
            where_str = f" WHERE {condicion}" if condicion else ''
            delete_query = f"DELETE FROM {tabla}{where_str}"
            cursor.execute(delete_query)
            self.conexion.commit()
            print("Datos eliminados correctamente.")
        except sqlite3.Error as error:
            print("Error al eliminar los datos:", error)
            
if __name__=='__main__':
    bd_manager = BaseDatos('ejemplo.db')
    bd_manager.conectar()
    bd_manager.crear_tabla('usuarios', ['id INTEGER PRIMARY KEY AUTOINCREMENT', 'nombre TEXT', 'apellido TEXT', 'edad INTEGER'])
    bd_manager.insertar('usuarios', ['nombre', 'apellido', 'edad'], ['Juan', 'Perez', 30])
    bd_manager.insertar('usuarios', ['nombre', 'apellido', 'edad'], ['Maria', 'Gomez', 25])
    bd_manager.insertar('usuarios', ['nombre', 'apellido', 'edad'], ['Pedro', 'Garcia', 40])
    bd_manager.insertar('usuarios', ['nombre', 'apellido', 'edad'], ['Ana', 'Gutierrez', 35])
    print(bd_manager.consultar('usuarios', ['nombre', 'apellido'], 'edad > 30'))
    bd_manager.actualizar('usuarios', ['nombre', 'apellido'], ['Jose', 'Perez'], 'id = 1')
    print(bd_manager.consultar('usuarios', ['nombre', 'apellido'], 'edad > 30'))
    bd_manager.eliminar('usuarios', 'id = 1')
    print(bd_manager.consultar('usuarios', ['nombre', 'apellido'], 'edad > 30'))
    bd_manager.cerrar_conexion()
