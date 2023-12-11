FROM python:3.8
ENV PYTHONBUFFERED 1

ENV APP_HOME=/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles

WORKDIR $APP_HOME
COPY . $APP_HOME

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python manage.py collectstatic --no-input; gunicorn frobshop.wsgi --workers 8 -b 0.0.0.0:8000 --threads=2 --worker-class=gthread --timeout 90 --worker-tmp-dir /dev/shm