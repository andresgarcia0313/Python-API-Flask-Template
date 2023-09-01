# Proyecto API

## Descripción
Este proyecto es una impresionante aplicación en Python que resuelve problemas complejos de manera eficiente.

## Instrucciones de instalación
Para utilizar este proyecto en tu entorno local, sigue los siguientes pasos:

### Clona este repositorio en tu máquina local:

git clone <URL_DEL_REPOSITORIO_ACTUAL>

### Crear y activar un entorno virtual:

En Windows:


Crear el entorno:
python -m venv env

Activar el entorno:
.\env\Scripts\activate


En Unix (Linux, macOS):


python -m venv env
source env/bin/activate


### Actualiza el gestor de dependencias:

python -m pip install --upgrade pip


### Instala las dependencias necesarias según el archivo requirements.txt:

pip install -r requirements.txt

### Al instalar una dependencia adicional, ejecuta:

pip install nombreDependencia
pip freeze > requirements.txt


Ejemplo en PowerShell:
pip install colorama; pip freeze > requirements.txt

Ejemplo en Símbolo de sistema y Bash
pip install colorama&&pip freeze > requirements.txt

### Ejecuta el proyecto con
python .\src\app.py

### Actualizar Dependencias

Es importante mantener tus dependencias actualizadas para beneficiarte de las últimas mejoras y correcciones de seguridad. Agrega esta sección para mostrar cómo actualizar las dependencias en tu entorno virtual:

## Actualizar todas las dependencias a las últimas versiones
pip install -U -r requirements.txt

### Desactivar el entorno virtual
## Para desactivar el entorno virtual y volver al entorno base de Python:
deactivate

### Estructura del proyecto
La estructura de archivos y directorios del proyecto es la siguiente:

├── .gitignore
├── app.py
├── README.md
├── requirements.txt
└── .vscode
    └── launch.json


- `.gitignore`: Archivo que especifica los archivos y directorios que deben ignorarse en el control de versiones Git.
- `app.py`: Archivo principal de la aplicación.
- `README.md`: Archivo que proporciona información detallada sobre el proyecto.
- `requirements.txt`: Archivo que enumera las dependencias principales del proyecto.
- `.vscode/launch.json`: Archivo de configuración de depuración para archivos activo y abierto

## Contribución
Si deseas contribuir a este proyecto, sigue estas directrices:

- Realiza un fork del repositorio y clona tu propio fork en tu máquina local.
- Crea una rama nueva para tu contribución: git checkout -b nombre-de-la-rama-para-la-funcionalidad.
- Realiza tus cambios y asegúrate de seguir las pautas de estilo y buenas prácticas.
- Envía una solicitud de extracción (pull request) a la rama principal del repositorio original para revisar tus cambios.
## Construir imagen docker 
Ejecuta el siguiente comando para construir la imagen Docker:

docker build -f Containerfile -t app:1.0 .

-t app:1.0 le da un nombre y una etiqueta a tu imagen. Puedes cambiar mi-aplicacion al nombre que prefieras y 1.0 a la versión que desees.
El último punto . indica que Docker debe buscar el Dockerfile en el directorio actual.

## Ejecuta el contenedor 

Puedes hacer a partir de la imagen construida usando el siguiente.
docker run --rm app:1.0

## Ejecutar compose para no instalar la carpeta env y que solo este dentro de los contenedores
docker-compose up -d
Con esto lo ejecutarias siempre y cuando el contenedor se llame app
docker-compose exec app python src/app.py


## Docker swarm
Iniciar docker swarm
    docker swarm init
y almacena el token en algún lado seguro

Ejecutalo con 
docker stack deploy -c docker-compose.yml mi-aplicacion


Verificar estado de la app

docker service ls

Escalar 

docker service scale mi-aplicacion_miservicio=3

Para realizar actualizaciones o cambios en tu aplicación, modifica tu archivo docker-compose.yml y luego actualiza la pila de servicios con:

docker stack deploy -c docker-compose.yml mi-aplicacion

## Monitoreo y mantenimiento:

Puedes utilizar herramientas de monitoreo como Prometheus y Grafana para supervisar el rendimiento de tu aplicación en el clúster Swarm y realizar mantenimiento cuando sea necesario.

## Ver repositorio de codigo git remoto actual

git remote -v

## Licencia
Este proyecto se distribuye bajo licencias. Solicita una licencia para obtener más detalles.

## Contacto y enlaces adicionales
Si desea obtener más información sobre este proyecto, no dude en ponerse en contacto con nosotros a través de WhatsApp al número +573012456984. Estaremos encantados de atender sus consultas y necesidades. ¡Esperamos escuchar de usted pronto!
