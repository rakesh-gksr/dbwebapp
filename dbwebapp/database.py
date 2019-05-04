import os

from django.conf import settings


engines = {
    'sqlite': 'django.db.backends.sqlite3',
    'postgresql': 'django.db.backends.postgresql_psycopg2',
    'oracle': 'django.db.backends.oracle',
}

a=10
A= 10 if a==10 else 20

def config(cfg_type="default"):
    service_name = os.getenv('DATABASE_SERVICE_NAME', '').upper().\
        replace('-', '_')
    if service_name:
        engine = engines.get(os.getenv('DATABASE_ENGINE'), engines['sqlite'])
    else:
        engine = engines['sqlite']
    name = os.getenv('DATABASE_NAME')
    if not name and engine == engines['sqlite']:
        name = os.path.join(settings.BASE_DIR, 'db.sqlite3')

    if cfg_type=="admin":
        user = os.getenv('DATABASE_ADMIN_NAME')
        password = os.getenv('DATABASE_ADMIN_PASSWORD')
    else:
        user = os.getenv('DATABASE_USER')
        password = os.getenv('DATABASE_PASSWORD')

    return {
        'ENGINE': engine,
        'NAME': name,
        'USER': user,
        'PASSWORD': password,
        'HOST': os.getenv('{}_SERVICE_HOST'.format(service_name)),
        'PORT': os.getenv('{}_SERVICE_PORT'.format(service_name)),
    }