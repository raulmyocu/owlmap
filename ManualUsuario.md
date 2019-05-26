# Owlmap - Manual de Usuario

## Proyecto elaborado para la materia de Ingeniería de Software I

### 1.- Información General
El propósito de la aplicación web es contar con un buscador especializado para la Universidad de Sonora, con el cuál poder encontrar lugares y puntos de interés dentro del campus

### 2.- Guía de Inicio
#### 2.1.- Visualizar mapa
Owlmap permite al usuario ver un mapa del campus de la Universidad de Sonora (campus Hermosillo); para poder visualizarlo, basta con ingresar a la página principal.

![](/Capturas/CU2.1.png "Visualizar mapa")

#### 2.2.- Usar buscador
La aplicación permite al usuario buscar algún punto de interés (sea un edificio, servicio, salón, cubículo, maestro); para ello es necesario posicionarse en la barra de busqueda situada en la parte superior derecha.

![](/Capturas/CU3.1.png "Usar buscador")

Una vez aquí, basta con escribir el lugar a buscar y dar clic en la lupa que se encuentra a la derecha. Esto permitira desplegar los resultados de la busqueda y es suficiente seleccionar uno de éstos para ver su ubicación en el mapa.

![](/Capturas/CU3.2.png "Usar buscador")

#### 2.3.- Visualizar ruta
#### 2.4.- Iniciar sesión
Owlmap permite a un usuario identificarse como administrador por medio del inicio de sesión.
Para iniciar sesión dentro de la aplicación basta con desplegar el menú situado en la esquina superior izquierda, y seleccionar la opción "Iniciar sesión".  

![](/Capturas/CU1.1.png "Iniciar sesión 1")

Una vez en la página, se deberá identificar por medio del correo proporcionado en la instalación, así como por la contraseña.

![](/Capturas/CU1.2.png "Iniciar sesión 2")

Al dar clic sobre el botón "Iniciar sesión" se redirigirá a home, pero puede corroborarse el inicio de sesión volviendo a desplegar el menú y observando que ahora las demás opciones están activas y ahora aparece una opción para cerrar sesión.

![](/Capturas/CU1.3.png "Iniciar sesión 3")


#### 2.5.- Información de lugares

Owlmap permite al administrador manejar la información de la base de datos; a continuación se muestran las posibles opciones disponibles:
* ##### 2.5.1.- Agregar

Para agregar información de un lugar no existente dentro de la base de datos, es necesario desplegar el menú de la parte superior izquierda, donde aparecerá la opción "Agregar información".

![](/Capturas/CU7.1.png "Agregar información lugares 1")

Una vez seleccionada esta opción, será redirigido a la siguiente página, donde podrá seleccionar el tipo de información a agregar:

![](/Capturas/CU5.1.png "Agregar información lugares 2")
Al seleccionar el tipo de lugar a agregar, será redirigido a un formulario con los campos de la información necesaria. Para llenar los campos de latitud y longitud basta con dar clic en el mapa  en donde se encuentra el lugar a agregar.

![](/Capturas/CU5.2.png "Agregar información lugares 3")

_(De tratarse de un cubículo o salón, puede seleccionarse un edificio al cual pertenezcan (si ya está registrado en la base de datos), lo que llenará automaticamente los espacios de latitud y longitud.)_

![](/Capturas/CU5.4.png "Agregar información lugares 4")

Al dar clic en "Guardar información" se redireccionará a una página donde se puede ver toda la información contenida en la base de datos (en las tablas de lugares); se puede corroborar que se agregó correctamente con el mensaje que aparecerá debajo de la barra superior.

![](/Capturas/CU5.3.png "Agregar información lugares 5")

* ##### 2.5.2.- Ver

Para ver la información existente, basta con desplegar el menú superior izquierdo y seleccionar la opción "Ver información de lugares".

![](/Capturas/CU1.3.png "Agregar información lugares 5")

De esta forma, se verá redireccionado y podrá visualizar los lugares existentes en la base de datos por medio de una tabla.

![](/Capturas/CU5.5.png "Agregar información lugares 6")

* ##### 2.5.3.- Editar

Para editar información de lugares existente dentro de la base de datos, es necesario _visualizar la información (ver 2.5.2)_.

![](/Capturas/CU5.6.png "Agregar información lugares 7")

Al presionar sobre el ícono de "lápíz" del registro a editar, aparecerá el formulario con los campos del registro:

![](/Capturas/CU5.7.png "Agregar información lugares 7")

Una vez modificado el registro, se debe dar clic sobre "Guardar información" para guardar los cambios realizados.

![](/Capturas/CU5.3.png "Agregar información lugares 8")

* ##### 2.5.4.- Eliminar

Para eliminar información de lugares existente dentro de la base de datos, es necesario _visualizar la información (ver 2.5.2)_.

![](/Capturas/CU5.5.png "Agregar información lugares 9")

Basta con posicionarse sobre el ícono de "borrar" del registro a eliminar, o cual desplegará una ventana para confirmar la acción:

![](/Capturas/CU5.8.png "Agregar información lugares 10")

Al presionar en "Borrar registro", se confirmará el borrado y aparecerán los lugares restantes de la base de datos.

![](/Capturas/CU5.9.png "Agregar información lugares 11")

#### 2.6.- Información de maestros

Owlmap permite al administrador manejar la información de la base de datos; a continuación se muestran las posibles opciones disponibles:
* ##### 2.6.1.- Agregar

Para agregar información de un maestro no existente dentro de la base de datos, es necesario desplegar el menú de la parte superior izquierda, donde aparecerá la opción "Agregar información".

![](/Capturas/CU7.1.png "Agregar información maestros 1")

Para agregar la información de un maestro, es necesario seleccionar la opción "Agregar maestro".

![](/Capturas/CU6.1.png "Agregar información maestros 2")

Al seleccionar la opción "Agregar maestro", será redirigido a un formulario con los campos de la información necesaria.
_(Si existen cubículos, aparecerá una lista de estos, de los cuales le puede ser asignado uno a este nuevo registro de maestro)_

![](/Capturas/CU6.2.png "Agregar información maestros 3")

Una vez llenados los campos, al dar clic en "Guardar información" se redireccionará a una página donde se puede ver toda la información contenida en la base de datos (en la tabla maestros); se puede corroborar que se agregó correctamente con el mensaje que aparecerá debajo de la barra superior.

![](/Capturas/CU6.3.png "Agregar información maestros 5")

* ##### 2.6.2.- Ver

Para ver la información existente, basta con desplegar el menú superior izquierdo y seleccionar la opción "Ver información de maestros".

![](/Capturas/CU1.3.png "Agregar información maestros 5")

De esta forma, se verá redireccionado y podrá visualizar los maestros existentes en la base de datos por medio de una tabla.

![](/Capturas/CU6.4.png "Agregar información maestros 6")

* ##### 2.6.3.- Editar

Para editar información de maestros existente dentro de la base de datos, es necesario _visualizar la información (ver 2.6.2)_.

![](/Capturas/CU6.5.png "Agregar información maestros 7")

Al presionar sobre el ícono de "lápíz" del registro a editar, aparecerá el formulario con los campos del registro:

![](/Capturas/CU6.6.png "Agregar información maestros 7")

Una vez modificado el registro, se debe dar clic sobre "Guardar información" para guardar los cambios realizados.

![](/Capturas/CU6.3.png "Agregar información maestros 8")

* ##### 2.6.4.- Eliminar

Para eliminar información de un maestro existente dentro de la base de datos, es necesario _visualizar la información (ver 2.6.2)_.

![](/Capturas/CU6.4.png "Agregar información maestros 9")

Basta con posicionarse sobre el ícono de "borrar" del registro a eliminar, o cual desplegará una ventana para confirmar la acción:

![](/Capturas/CU6.7.png "Agregar información maestros 10")

Al presionar en "Borrar registro", se confirmará el borrado y aparecerán los maestros restantes de la base de datos.

![](/Capturas/CU6.8.png "Agregar información maestros 11")

#### 2.7.- Cerrar sesión
Si el usuario ha terminado de administrar los lugares y maestros que aparecen en los resultados del buscador, es posible cerrar sesión; para realizar esto es necesario desplegar el menú de la esquina superior izquierda, donde aparecerá la opción "Cerrar sesión".

![](/Capturas/CU7.1.png "Cerrar sesión 1")

Una vez seleccionada esta opción, será redirigido a la pantalla de inicio; se puede corroborar el cerrado de sesión volviendo a activar el menú desplegable y observando las opciones inactivas.

![](/Capturas/CU1.1.png "Cerrar sesión 2")
