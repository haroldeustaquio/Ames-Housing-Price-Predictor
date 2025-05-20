# docker/Dockerfile
FROM python:3.10

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer el puerto de FastAPI
EXPOSE 8080

# Comando para correr la API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
