"""Instalador para el paquete "color_terminal_glj"."""

from setuptools import setup

long_description = (
    open('README.txt').read()
    + '\n' +
    open('LICENSE').read()
    + '\n')

setup(
    name="color_terminal_glj",
    version="2.2.38",
    description="Paquete ayuda cambio de colores de texto de terminal",
    long_description=long_description,
    url="https://github.com/AutodidactaMx/cocid_python",        
    author="Jesus Gutierrez Lopez.",
    author_email="jesus.gutierrez@autodidactamx.com",    
    download_url="https://github.com/AutodidactaMx/cocid_python",
    license="MIT",    
    packages=["utileria"],
    include_package_data=True,
    keywords="Utileria para camino de colores de texto en terminal",
    classifiers=[        
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8"
    ],
)