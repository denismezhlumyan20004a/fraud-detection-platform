FROM python:3.10-slim

WORKDIR /app

# Copiamos la lista de librerías e instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de los archivos
COPY . .

# Exponemos el puerto de FastAPI
EXPOSE 8000

# Comando para iniciar el API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
