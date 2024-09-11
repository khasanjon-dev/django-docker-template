FROM python:3.12-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

COPY ./requirements /app/requirements/

RUN pip install -r /app/requirements/local.txt

COPY ./compose/ /compose/

RUN mv /compose/local/django/start /start_
RUN cat start_ | sed 's/\r$//' > start
RUN rm start_
RUN chmod +x /start

RUN mv /compose/local/django/entrypoint /entrypoint_
RUN cat entrypoint_ | sed 's/\r$//' > entrypoint
RUN rm entrypoint_
RUN chmod +x /entrypoint

RUN rm -rf /compose/

COPY . /app

ENTRYPOINT ["/entrypoint" ]

