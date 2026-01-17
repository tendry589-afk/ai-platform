FROM python:3.11-slim

WORKDIR /app

# Copier le fichier requirements.txt depuis backend
COPY backend/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le backend
COPY backend .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
