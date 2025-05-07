from setuptools import setup


setup(
    name="bigdata",
    author="Carlos Dueiner",
    author_email="carlos.castano@est.iudigital.edu.co",
    description="Base de datos de COVID-19 en Antioquia",
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "BeautifulSoup4"
    ] 
)