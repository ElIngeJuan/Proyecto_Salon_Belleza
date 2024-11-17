# 🔥Guardar archivo e imagen en Django & Python 🐍

###### 1. Crear un entorno virtual, hay muchas formas

    Opción 1: Crear entorno virtual con el paquete virtualenv,
    puedes instalarlo de forma global en el sistema atraves de https://pypi.org/project/virtualenv/

    pip install virtualenv #Instalar paquete virtualenv
    virtualenv --version #Version
    virtualenv env #Crear entorno con el paquete virtualenv

    Opción 2: Crear un entorno virtual con el paquete que ya viene por defecto en las ultimas versiones de Python
    python -m venv env o python3 -m venv env

###### 2. Activar ambiente virtual

    . env/Script/activate #Activar ambiente desde Windows
    . env/bin/activate  #Activar desde la Mac
    deactivate #Desactivar mi entorno virtual

###### 3. Instalar Djando desde el manejador de paquete de Python Pip

    pip install Django
    Nota: para instalar Django en una version especifica
    pip install Django==4.2.4
    python3 -m django --version  #Vrsion instalada de Django

###### 4. Instalar el paquete (biblioteca) Pillow

    Pillow es la librería que nos permite usar el campo ImageField y FileField en el modelo para poder guardar tanto imágenes como archivos

    https://pypi.org/project/Pillow/
    pip install Pillow



#### 8. Corriendo el proyecto

    python3 manage.py runserver # Corriendo el proyecto
    python3 manage.py runserver 8500 #Corriendo el proyecto en un puerto diferente

