FROM python:3.11.3-slim-bullseye

ENV PYTHONUNBUFFERED 1
ARG APP_DIR="/var/www/drf-sample-api"

RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}

ADD . ${APP_DIR}
RUN apt-get update && \
    apt-get -y install gcc libmariadb-dev
RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 8000

CMD [ \
  "gunicorn", \
  "-w",                     "3", \
  "-b",                     "127.0.0.1:8080", \
  "--max-requests",         "20", \
  "--max-requests-jitter",  "5", \
  "--timeout",              "3600", \
  "--access-logfile",       "-", \
  "--error-logfile",        "-", \
  "--capture-output", \
  "--statsd-host",          "127.0.0.1:8125", \
  "drf-sample-api.wsgi" \
]
