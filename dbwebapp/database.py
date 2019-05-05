import os
import sys

from django.conf import settings


engines = {
    'sqlite': 'django.db.backends.sqlite3',
    'postgresql': 'django.db.backends.postgresql_psycopg2',
    'oracle': 'django.db.backends.oracle',
}


def config():

    service_name = os.getenv('DATABASE_SERVICE_NAME', '').upper().\
        replace('-', '_')
    if service_name:
        engine = engines.get(os.getenv('DATABASE_ENGINE'), engines['oracle'])
    else:
        engine = engines['sqlite']
    name = os.getenv('DATABASE_NAME')
    if not name and engine == engines['sqlite']:
        name = os.path.join(settings.BASE_DIR, 'db.sqlite3')

    argv = sys.argv
    cmd = argv[1] if len(argv) > 1 else None
    if cmd in ['migrate', 'makemigrations']:
        user = os.getenv('DATABASE_ADMIN_NAME')
        password = os.getenv('DATABASE_ADMIN_PASSWORD')
    else:
        user = os.getenv('DATABASE_USER')
        password = os.getenv('DATABASE_PASSWORD')

    return {
        'ENGINE': "django.db.backends.oracle",
        'NAME': name,
        'USER': user,
        'PASSWORD': password,
        'HOST': os.getenv('{}_SERVICE_HOST'.format(service_name)),
        'PORT': os.getenv('{}_SERVICE_PORT'.format(service_name)),
    }