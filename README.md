# OwlMap

## Proyecto OwlMap para la materia de Ingeniería de Software I

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
Posteriormente, es necesario inicializar la base de datos de SQLAlchemy.

Para esto, entraremos a Python 3 desde la terminal.

```bash
python3
```

y la inicializaremos

```python
from owlmap import db
db.create_all()
```

Finalmente, podemos crear un administrador

```python
from owlmap import User
admin = User(exp=123456, email='admin@demo.com', password='admin123', nombres='John', apellidos='Doe')
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

Para detener el servidor, basta con utilizar **CTRL-C**.

_En caso de que la aplicacioń web vaya a ser lanzada a producción, no es recomendable usar el servidor desarrollo de Flask, sino un servidor WSGI como Gunicorn, y un servidor web como Nginx._
