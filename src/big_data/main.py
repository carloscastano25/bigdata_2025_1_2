from dataexcel import DataExcel
from database import DataBase
import pandas as pd


def main():
    # Enlace público del archivo Excel en Google Drive
    url = "https://docs.google.com/spreadsheets/d/1NG6FOPgf1KJa33MbDnQKys1FGIehkuoJ/edit?usp=sharing&ouid=104595497373497694052&rtpof=true&sd=true"

    # Crear una instancia de DataExcel para obtener los datos
    dataexcel = DataExcel(url)
    df = dataexcel.obtener_datos()

    # Verificar y mostrar los datos obtenidos
    print("*************** Impresión de los datos obtenidos ************************")
    print(df.shape)
    print(df.head())

    # Guardar los datos en un archivo CSV
    df.to_csv("src/big_data/static/csv/data_excel.csv", index=False)  # Ruta para guardar el CSV

    # Crear una instancia de DataBase para manejar la base de datos SQLite
    db_name = "src/big_data/static/db/datos_analiticos.db"
    table_name = "datos_analiticos"
    database = DataBase(db_name)

    # Insertar datos en la base de datos
    database.insert_data(df, table_name)
    print(f"*************** Insertar los datos obtenidos en la base de datos tabla: {table_name} ***************")
    print(df.shape)
    print(df.head())

    # Leer datos de la base de datos
    df_2 = database.read_data(table_name)
    print("*************** Datos leídos de la base de datos ***************")
    print(df_2.shape)
    print(df_2.head())

    # Actualizar datos en la base de datos (ejemplo: cambiar el estado de un caso)
    database.update_data(
        table_name=table_name,
        set_clause="estado = 'Recuperado'",
        where_clause="estado = 'Activo'"
    )
    print("*************** Datos actualizados en la base de datos ***************")
    df_actualizado = database.read_data(table_name)
    print(df_actualizado.shape)
    print(df_actualizado.head())

    # Eliminar datos de la base de datos (ejemplo: eliminar registros con edad < 18)
    database.delete_data(
        table_name=table_name,
        where_clause="edad < 18"
    )
    print("*************** Datos eliminados de la base de datos ***************")
    df_final = database.read_data(table_name)
    print(df_final.shape)
    print(df_final.head())


if __name__ == "__main__":
    main()