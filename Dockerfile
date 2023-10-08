FROM python 

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt --default-timeout=1000

EXPOSE 8000

CMD python /app/manage.py runserver 0.0.0.0:800
