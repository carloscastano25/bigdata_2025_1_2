from setuptools import setup


setup(
    name="bigdata",
    author="Carlos Dueiner",
    author_email="carlos.castano@est.iudigital.edu.co",
    description="Base de datos de COVID-19 en Antioquia",
    version="0.1",
    packages=["src/big_data", "src/big_data.static"],
    package_dir={"": "src"},
    package_data={
        "src/big_data": ["static/db/*.db", "static/csv/*.csv"],
        "src/big_data.static": ["dataexcel.py", "database.py", "main.py"]
    },
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "BeautifulSoup4"
    ] 
)