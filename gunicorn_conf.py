import multiprocessing
#gunicorn dbwebapp.wsgi --config gunicorn_conf.py
bind = "0.0.0.0:8000"
print("cpu_count",multiprocessing.cpu_count())
workers = multiprocessing.cpu_count()
logfile = "gunicorn.log"