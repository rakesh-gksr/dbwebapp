FROM python:3

ADD my_script.py /

RUN pip install cx_Oracle==6.3.1
RUN pip freeze

CMD [ "python", "./my_script.py" ]