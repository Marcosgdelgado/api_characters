# api_characters
***
## Descripción
***
Esta API nos permitira realizar la carga, eliminación y lectura de personajes en nuestra base de datos.
## Estuctura del proyecto
***
~~~
├── compose.yaml  
├── Dockerfile  
├── requirements.txt  
├── app  
    ├── main.py  
    ├── database.py  
    ├── character  
         ├── crud.py  
         ├── models.py  
         ├── routes.py  
         ├── schemas.py  
~~~
## Instalación y uso
***
Para poder utilizar esta api en Windows debemos tener instalado WSL2 y Docker Desktop. En caso de querer utilizarla en macOS o distros Linux, no hace falta instalar nada ya que se puede ejecutar nativamente.  
Una vez instalados los requisitos anteriores debemos clonar el repositorio con el siguiente comando:  
~~~
git clone https://github.com/Marcosgdelgado/api_characters.git --config core.autocrlf=input
~~~
Luego, debemos abrir el proyecto en nuestro IDE o acceder a la ruta principal mediante nuestra terminar e ingresar por consola el siguiente comando:
~~~
docker-compose up --build
~~~  
Esto construirá e iniciará nuestra API, la cual podemos acceder a través de:  
http://localhost:8000/docs


## Tecnogías utilizadas
***
- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- Docker
