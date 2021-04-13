# DO NOT run print_badge.service when this container is running
FROM python:3.8-slim-buster AS print_badge

RUN apt update -y && \
    apt install -y uwsgi uwsgi-plugin-python3 && \
    apt install -y python3-pip
    # *** No need to install fonts if provided in Python code
    # apt install -y ttf-mscorefonts-installer && \

RUN mkdir /app
COPY ./requirements.txt /app
WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./*.py /app
RUN mkdir /app/.fonts
COPY ./.fonts/* /app/.fonts
RUN mkdir /app/images
COPY ./images/* /app/images

ENV RUNNING_IN_DOCKER=True
EXPOSE 7070
ENTRYPOINT ["uwsgi", "--http-socket", "0.0.0.0:7070", "--plugin", \
            "python3", "--module", "main:app"]
# CMD ["python3", "-m" , "main:app", "--host=0.0.0.0", "--port=8080"]
