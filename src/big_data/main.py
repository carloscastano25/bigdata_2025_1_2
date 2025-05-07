from big_data.dataexcel import DataExcel
from big_data.database import DataBase
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

    # Crear una instancia de DataBase para almacenar los datos en SQLite
    table_name = "datos_analiticos"
    database = DataBase("src/big_data/static/db/datos_analiticos.db", table_name, df)

    # Cerrar la base de datos
    database.close_database()


if __name__ == "__main__":
    main()