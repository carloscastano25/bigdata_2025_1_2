import sqlite3
from dataexcel import DataExcel  # Importar la clase DataExcel para obtener los datos

class DataBase:
    def __init__(self, db_name, table_name, data):
        self.db_name = db_name  # Ruta de la base de datos SQLite
        self.table_name = table_name  # Nombre de la tabla en la base de datos
        self.data = data  # Datos a insertar en la base de datos

        self.create_database()
        self.load_data_to_database()

    def create_database(self):
        try:
            # Crear conexión a la base de datos
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print("Base de datos creada o conectada exitosamente.")
        except Exception as err:
            print(f"Error al crear la base de datos: {err}")

    def load_data_to_database(self):
        try:
            # Insertar los datos en la tabla de la base de datos
            self.data.to_sql(self.table_name, self.conn, if_exists='replace', index=False)
            print(f"Datos cargados exitosamente en la tabla '{self.table_name}'.")
        except Exception as err:
            print(f"Error al cargar los datos en la base de datos: {err}")

    def close_database(self):
        # Cerrar la conexión a la base de datos
        self.conn.close()
        print("Conexión a la base de datos cerrada.")


# Ejemplo de uso
if __name__ == "__main__":
    # Enlace público del archivo Excel en Google Drive
    url = "https://docs.google.com/spreadsheets/d/1NG6FOPgf1KJa33MbDnQKys1FGIehkuoJ/edit?usp=sharing&ouid=104595497373497694052&rtpof=true&sd=true"

    # Crear una instancia de DataExcel para obtener los datos
    data_excel = DataExcel(url)
    df = data_excel.obtener_datos()

    # Nombre de la tabla en la base de datos
    table_name = "datos_analiticos"

    # Crear una instancia de la clase DataBase
    db = DataBase("src/big_data/static/db/datos_analiticos.db", table_name, df)

    # Cerrar la base de datos
    db.close_database()