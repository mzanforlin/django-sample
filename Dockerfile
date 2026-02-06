FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o projeto
COPY . .

# Coleta arquivos estáticos (importante!)
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# O comando aponta para a pasta demo_django que vi no seu print
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "demo_django.wsgi:application"]