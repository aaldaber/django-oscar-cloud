FROM python:3.8
ENV PYTHONUNBUFFERED 1

ENV APP_HOME=/app
RUN mkdir $APP_HOME

WORKDIR $APP_HOME
COPY . $APP_HOME

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD gunicorn wsgi:app --workers 8 -b 0.0.0.0:8000 --threads=2 --worker-class=gthread --timeout 90 --worker-tmp-dir /dev/shm