FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependências de sistema
RUN apt-get update && apt-get install -y libpq-dev build-essential --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Forçamos o Docker a ignorar o cache para o pip
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Este comando só vai rodar se o passo anterior (pip install) realmente instalou o Django
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "demo_django.wsgi:application"]