# OwlMap - Manual de Instalación

## Proyecto elaborado para la materia de Ingeniería de Software I

### Instalando requerimientos

Este proyecto ha sido desarrollado utilizando el framework Flask. Para correr el servidor hay que tener instalado Python 3, así como el manejador de librerías pip, con los paquetes:

* flask
* flask-wtf
* flask-sqlalchemy
* flask-login

Para instalar estas librerías en la versión utilizada para la elaboración de este proyecto:

```bash
pip3 install -r requirements.txt
```

---
### Inicializando la base de datos

En este paso, crearemos un archivo site.db para los archivos de la base de datos de SQLAlchemy.
En caso de que ya exista un archivo _site.db_, lo eliminaremos.

```bash
rm owlmap/site.db
```

- #### Configuración automática
  Para inicializar la base de datos y crear un administrador, correremos el archivo: _configdb.py_

  Y correremos con Python 3 el archivo de configuración.

  ```bash
  python3 configdb.py
  ```
  El usuario administrador será:

  ```python
  email = 'admin@owlmap.com'
  password = 'admin123'
  exp = 000000
  nombres = 'John'
  apellidos = 'Doe'
  ```

- #### Configuración manual
  Primero, entraremos a Python 3 desde la terminal.

  ```bash
  python3
  ```

  y la inicializaremos utilizando el método *create_all()*.

  ```python
  from owlmap import db
  db.create_all()
  ```

  Finalmente, podemos crear un administrador con los parámetros de nuestra preferencia.

  ```python
  from owlmap.models import User
  admin = User(exp=123456, email='admin@owlmap.com', password='admin123', nombres='John', apellidos='Doe')
  db.session.add(admin)
  db.session.commit()
  ```

  De esta forma tendremos registrado un usuario administrador.

---
### Correr servidor
Para correr desde la terminal, hay que situarse en el directorio raíz y correr el ejecutable _run.py_ utilizando Python 3 mediante:

```bash
python3 run.py
```

Dentro del archivo _run.py_, podemos considerar distintos parámetros para la función _app.run()_ al correr el servidor de desarrollo de Flask.

```Python
if __name__ == '__main__':
    app.run() #Añadir parámetros aquí
```

Añadir parámetro ```debug=True``` para activar el modo de depuración.  
Añadir parámetro ```host='0.0.0.0'``` para correr servidor en red local.  
Añadir parámetro ```ssl_context='adhoc'``` para correr mediante protocolo https.
Para este último es necesario instalar _pyopenssl_ mediante:
```bash
pip install pyopenssl
```

Para detener el servidor, basta con utilizar **CTRL-C**.

_En caso de que la aplicacioń web vaya a ser lanzada a producción, no es recomendable usar el servidor desarrollo de Flask, sino un servidor WSGI como Gunicorn, y un servidor web como Nginx._

[Haga clic aquí para ver el manual de usuario.](https://github.com/raulmyocu/owlmap/blob/master/Documentacion/ManualUsuario.md)
