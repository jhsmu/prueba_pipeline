
FROM python:3.9

ENV DB_HOST=host.docker.internal\
    DB_PORT=8889\
    DB_NAME=prueba\
    DB_USER=root \
    DB_PASSWORD=root 

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY conexion.py .
    
CMD ["python", "conexion.py"]
