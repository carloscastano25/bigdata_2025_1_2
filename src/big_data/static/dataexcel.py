import pandas as pd

class DataExcel:
    def __init__(self, url):
        self.url = "https://docs.google.com/spreadsheets/d/1NG6FOPgf1KJa33MbDnQKys1FGIehkuoJ/edit?usp=sharing&ouid=104595497373497694052&rtpof=true&sd=true"

    def obtener_datos(self):
        try:
            # Convertir el enlace de Google Drive a un enlace de descarga directa
            file_id = self.url.split('/d/')[1].split('/')[0]
            download_url = f"https://drive.google.com/uc?id={file_id}"

            # Leer el archivo Excel desde el enlace
            df = pd.read_excel(download_url)

            # Renombrar columnas para estandarizarlas
            df = df.rename(columns={
                'fecha reporte web': 'fecha_reporte',
                'ID de caso': 'id_caso',
                'Fecha de notificación': 'fecha_notificacion',
                'Nombre departamento': 'departamento',
                'Código DIVIPOLA municipio': 'codigo_divipola',
                'Nombre municipio': 'municipio',
                'Edad': 'edad',
                'Sexo': 'sexo',
                'Tipo de contagio': 'tipo_contagio',
                'Ubicación del caso': 'ubicacion_caso',
                'Estado': 'estado',
                'Recuperado': 'recuperado',
                'Fecha de inicio de síntomas': 'fecha_inicio_sintomas',
                'Fecha de muerte': 'fecha_muerte',
                'Fecha de diagnóstico': 'fecha_diagnostico',
                'Fecha de recuperación': 'fecha_recuperacion',
                'Tipo de recuperación': 'tipo_recuperacion',
                'Pertenencia étnica': 'pertenencia_etnica'
            })

            # Convertir columnas a tipos de datos adecuados
            df = self.convertir_tipos(df)

            return df
        except Exception as err:
            print(f"Error al leer el archivo Excel: {err}")
            return pd.DataFrame()

    def convertir_tipos(self, df):
        df = df.copy()
        try:
            # Convertir columnas de fechas
            columnas_fecha = [
                'fecha_reporte', 'fecha_notificacion', 'fecha_inicio_sintomas',
                'fecha_muerte', 'fecha_diagnostico', 'fecha_recuperacion'
            ]
            for col in columnas_fecha:
                if col in df.columns:
                    df[col] = pd.to_datetime(df[col], errors='coerce')

            # Convertir columnas numéricas
            if 'edad' in df.columns:
                df['edad'] = pd.to_numeric(df['edad'], errors='coerce')
            if 'codigo_divipola' in df.columns:
                df['codigo_divipola'] = pd.to_numeric(df['codigo_divipola'], errors='coerce')

        except Exception as err:
            print(f"Error al convertir tipos de datos: {err}")

        return df


# Ejemplo de uso
if __name__ == "__main__":
    # Enlace público del archivo Excel en Google Drive
    url = "https://docs.google.com/spreadsheets/d/1NG6FOPgf1KJa33MbDnQKys1FGIehkuoJ/edit?usp=sharing&ouid=104595497373497694052&rtpof=true&sd=true"

    # Crear una instancia de DataExcel
    data_excel = DataExcel(url)

    # Obtener los datos procesados
    df = data_excel.obtener_datos()

    # Mostrar las primeras filas del DataFrame
    print(df.head())