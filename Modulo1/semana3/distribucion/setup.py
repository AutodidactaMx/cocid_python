"""Instalador para el paquete "operaciones_basicas"."""

from setuptools import setup

long_description = (
    open('README.txt').read()
    + '\n' +
    open('LICENSE').read()
    + '\n')

setup(
    name="cocid_operaciones",
    version="1.0.0",
    description="Calculo de operaiones matematicas basicas",
    long_description=long_description,
    url="https://github.com/AutodidactaMx/cocid_python",        
    author="Jesus Gutierrez Lopez.",
    author_email="jesus.gutierrez@autodidactamx.com",    
    download_url="https://github.com/AutodidactaMx/cocid_python",
    license="MIT",    
    packages=["operaciones"],
    include_package_data=True,
    keywords="Ejmeplo de operaciones basicas suma, rest, multiplicacion",
    classifiers=[        
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
)