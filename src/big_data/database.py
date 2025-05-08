import sqlite3
import pandas as pd


class DataBase:
    def __init__(self, db_name):
        self.db_name = db_name  # Ruta de la base de datos SQLite

    # C = Create (Insertar datos en la tabla)
    def insert_data(self, df=pd.DataFrame(), table_name="datos_analiticos"):
        try:
            conn = sqlite3.connect(self.db_name)
            df.to_sql(name=table_name, con=conn, if_exists='replace', index=False)  # Sobrescribe la tabla si ya existe
            conn.close()
            print(f"Datos insertados exitosamente en la tabla '{table_name}'.")
        except Exception as errores:
            print(f"Error al guardar los datos: {errores}")

    # R = Read (Leer datos de la tabla)
    def read_data(self, table_name="datos_analiticos"):
        df = pd.DataFrame()
        try:
            conn = sqlite3.connect(self.db_name)
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql_query(sql=query, con=conn)
            conn.close()
            print(f"Datos leídos exitosamente de la tabla '{table_name}'.")
            return df
        except Exception as errores:
            print(f"Error al obtener los datos: {errores}")
            return df

    # U = Update (Actualizar datos en la tabla)
    def update_data(self, table_name="datos_analiticos", set_clause="", where_clause=""):
        try:
            conn = sqlite3.connect(self.db_name)
            query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            conn.close()
            print(f"Datos actualizados exitosamente en la tabla '{table_name}'.")
        except Exception as errores:
            print(f"Error al actualizar los datos: {errores}")

    # D = Delete (Eliminar datos de la tabla)
    def delete_data(self, table_name="datos_analiticos", where_clause=""):
        try:
            conn = sqlite3.connect(self.db_name)
            query = f"DELETE FROM {table_name} WHERE {where_clause}"
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            conn.close()
            print(f"Datos eliminados exitosamente de la tabla '{table_name}'.")
        except Exception as errores:
            print(f"Error al eliminar los datos: {errores}")


# Ejemplo de uso
if __name__ == "__main__":
    from dataexcel import DataExcel  # Importar la clase DataExcel para obtener los datos

    # Enlace público del archivo Excel en Google Drive
    url = "https://docs.google.com/spreadsheets/d/1NG6FOPgf1KJa33MbDnQKys1FGIehkuoJ/edit?usp=sharing&ouid=104595497373497694052&rtpof=true&sd=true"

    # Crear una instancia de DataExcel para obtener los datos
    data_excel = DataExcel(url)
    df = data_excel.obtener_datos()

    # Crear una instancia de la clase DataBase
    db = DataBase("src/big_data/static/db/datos_analiticos.db")

    # Insertar datos en la base de datos
    db.insert_data(df)

    # Leer datos de la base de datos
    df_leidos = db.read_data()
    print(df_leidos.head())

    # Actualizar datos en la base de datos (ejemplo: cambiar el estado de un caso)
    db.update_data(
        table_name="datos_analiticos",
        set_clause="estado = 'Recuperado'",
        where_clause="estado = 'Activo'"
    )

    # Eliminar datos de la base de datos (ejemplo: eliminar registros con edad < 18)
    db.delete_data(
        table_name="datos_analiticos",
        where_clause="edad < 18"
    )