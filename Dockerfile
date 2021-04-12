# DO NOT run print_badge.service when this container is running
FROM tiangolo/uwsgi-nginx-flask:python3.8 AS print_badge

RUN apt update -y && \
    apt install -y python3-pip && \
    # *** No need to install fonts if provided in Python code
    # apt install -y ttf-mscorefonts-installer && \
    apt install -y uwsgi-plugin-python3

COPY ./app /app

WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt

ENV RUNNING_IN_DOCKER=True
EXPOSE 8080
CMD ["uwsgi", "--http-socket", "0.0.0.0:8080", \
              "--plugin", "python3", \
              "--module", "main:app"]
