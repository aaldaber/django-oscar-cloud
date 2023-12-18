FROM python:3.8
ENV PYTHONUNBUFFERED 1

ENV APP_HOME=/app
RUN mkdir $APP_HOME

WORKDIR $APP_HOME
COPY . $APP_HOME

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8089

CMD locust