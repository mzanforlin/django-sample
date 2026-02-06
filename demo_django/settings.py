import os
from pathlib import Path

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Segurança: Em produção, o ideal é usar variáveis de ambiente
SECRET_KEY = 'django-insecure-v^vhjz8rsgpjri38qiv=)m02w_662fu&tj7%xgp*()uh_#oq3l'

# Debug desligado para produção
DEBUG = False

# Permitir o domínio do Easypanel
ALLOWED_HOSTS = ['*']

# Configuração essencial para HTTPS no Easypanel
CSRF_TRUSTED_ORIGINS = [
    'https://crm-my-app.dejq6v.easypanel.host',
    'https://*.easypanel.host'
]

# Apps instalados
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic', # Opcional: melhora o dev local com whitenoise
]

# Middleware com WhiteNoise na posição correta (logo após SecurityMiddleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demo_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'demo_django.wsgi.application'

# Banco de dados SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validação de senhas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internacionalização
LANGUAGE_CODE = 'pt-br' # Mudei para português
TIME_ZONE = 'America/Sao_Paulo' # Mudei para seu fuso
USE_I18N = True
USE_TZ = True

# Arquivos Estáticos (Configuração Robusta para Docker)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Armazenamento do WhiteNoise com compressão (evita erro 500 se faltar arquivo)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'