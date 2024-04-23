# Usa la imagen base de Python 3.11
FROM python:3.11

# Establece el directorio de trabajo en /app
WORKDIR /code

# Copia el archivo requirements.txt al contenedor
COPY ./requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt
# Copia el contenido de la aplicación al contenedor
COPY ./app code/app

EXPOSE 8000

# Comando para ejecutar la aplicación FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
