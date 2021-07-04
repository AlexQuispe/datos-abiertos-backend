# Instalación

## 1. Instalación de Python 3.9.6 en Debian 10

```bash
# actualiza el índice de paquetes
sudo apt update

# instalación de paquetes básicos
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev

# descargamos la versión 3.9.6 de python
cd ~/
sudo wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz

# descomprimimos el archivo
sudo tar xzf Python-3.9.6.tgz

# instalación
cd Python-3.9.6
sudo ./configure --enable-optimizations
sudo make altinstall
```

Verificamos la versión

```bash
python3.9 --version

    Python 3.9.6
```

**Nota.-** Para conocer la ubicacion de los binarios ejecutar el comando `which`, por ejecmplo:

```bash
which python3

    /usr/bin/python3
```

```bash
which python3.9

    /usr/local/bin/python3.9
```

## 2. Clonación del proyecto y creación de un entorno virtual

```bash
git clone git@github.com:AlexQuispe/datos-abiertos-backend.git
```

Ahora creamos un entorno virtual para el proyecto.

**NOTA.-** Esto solo será necesario cada vez que se clone el proyecto.

```bash
# dentro de la carpeta del proyecto
cd datos-abiertos-backend

# creamos un entorno virtual
python3.9 -m venv env
```

Se creará la carpeta `env`.

Para activar y desactivar el entorno virtual.

```bash
# Activa el entorno virtual
source env/bin/activate

# Desactiva el entorno virtual
deactivate
```

Una vez esté activado el entorno virtual, instalar las dependencias.

```bash
pip install -r requirements.txt
```

## 3. Levanta el servicio en modo desarrollo

```bash
# Sincroniza la base de datos (SQLite)
python manage.py migrate
```

```bash
# Crea un usuario por defecto
python manage.py createsuperuser --email admin@example.com --username admin
```

```bash
# Inicia el servicio
python manage.py runserver
```

## 4. Comandos útiles

```bash
# Para actualizar el archivo requirements.txt
pip freeze > requirements.txt
```

## Referencias externas

- [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)
- [https://hackersandslackers.com/multiple-versions-python-ubuntu/](https://hackersandslackers.com/multiple-versions-python-ubuntu/)
