# Instrucciones

utilizar este comando tanto en Linux como en Windows:

```bash
<local_remote_machine>@<username>:~$ git clone "https://github.com/Bellothornus2/Proyecto"
<local_remote_machine>@<username>:~$ cd Proyecto
```

## Linux:

### Entorno Virtual

para activar el entorno virtual:

````bash
<local_remote_machine>@<username>:~/Proyecto$ source ./venv/scripts/activate
````

### Instalar dependencias

para descargar e instalar todas las dependencias en el entorno sin afectar al equipo local o remoto:

````bash
(venv) <local_remote_machine>@<username>:~/Proyecto$ pip install -r requirements.txt
````

### Lanzar servicio Web

vamos al directorio donde se encuentra la pagina web y lanzamos un servicio web desde ahí:

````bash
(venv) <local_remote_machine>@<username>:~/Proyecto$ cd pagina
(venv) <local_remote_machine>@<username>:~/Proyecto/pagina$ python -m htpp.server
````

### Probar los casos test

Abrimos otra terminal ya que la anterior se encargará de las peticiones web

````bash
(venv) <local_remote_machine>@<username>:~/Proyecto$ cd test
````

Ejecutamos los tests que queramos con el framework para hacer pruebas "Pytest"

````bash
(venv) <local_remote_machine>@<username>:~/Proyecto/test$ pytest -vv 
````

### Ejecutar el código

Nos debería salir todos los tests acertados y fallados, los puedes cambiar para hacer pruebas con src:

````bash
(venv) <local_remote_machine>@<username>:~/Proyecto/test$ cd ../src
(venv) <local_remote_machine>@<username>:~/Proyecto/src$ py main.py
````

### Comprobar datos guardados

Deberíamos ejecutar el archivo main.py para que se nos descargue un json en "/database":

````bash
(venv) <local_remote_machine>@<username>:~/Proyecto/src$ cd ../database
(venv) <local_remote_machine>@<username>:~/Proyecto/database$ ./<file_name>.json
````

## Windows:

### Entorno virtual

````cmd
%usernamepath%\Proyecto> .\venv\sscripts\activate
````

### Instalar dependencias

para descargar e instalar todas las dependencias en el entorno sin afectar al equipo local o remoto:

````cmd
(venv) %usernamepath%\Proyecto> pip install -r requirements.txt
````

### Lanzar servicio Web

vamos al directorio donde se encuentra la pagina web y lanzamos un servicio web desde ahí:

````cmd
(venv) %usernamepath%\Proyecto> cd pagina
(venv) %usernamepath%\Proyecto\pagina> python -m htpp.server
````

### Probar los casos test

Abrimos otra terminal ya que la anterior se encargará de las peticiones web

````cmd
(venv) %usernamepath%\Proyecto> cd test
````

Ejecutamos los tests que queramos con el framework para hacer pruebas "Pytest"

````cmd
(venv) %usernamepath%\Proyecto\test> pytest -vv
````

### Ejecutar el código

Nos debería salir todos los tests acertados y fallados, los puedes cambiar para hacer pruebas con src:

````cmd
(venv) %usernamepath%\Proyecto\test> cd ..\src
(venv) %usernamepath%\Proyecto\src> py main.py
````

### Comprobar datos guardados

Deberíamos ejecutar el archivo main.py para que se nos descargue un json en "/database":

````cmd
(venv) %usernamepath%\Proyecto\test> cd ..\database
(venv) %usernamepath%\Proyecto\database> .\<file_name>.json
````

## Interfaz Gráfica:

de momento hay un pequeño programa con interfaz gráfica para que sea mas a meno para el usuario estándar

### Ejecución

````bash
(venv) <local_remote_machine>@<username>:~/Proyecto/src$ py program.py
````

### Detalles

con este comando lanzaremos el programa para que funcione, solo tiene lo básico y quedan todavía muchísimas mejoras por añadirle, tanto estéticas como funcionales
