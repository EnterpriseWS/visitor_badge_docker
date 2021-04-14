# DO NOT run print_badge.service when this container is running
FROM python:3.8-slim-buster AS print_badge
# FROM ubuntu:20.04 AS print_badge

RUN apt update -y && \
    apt install -y libusb-1.0-0-dev usbutils
    # No need to install pip is python images is used
    # apt install -y python3-pip
    # *** No need to install fonts if provided in Python code
    # apt install -y ttf-mscorefonts-installer && \

COPY ./requirements.txt /
WORKDIR /
RUN pip3 install --no-cache-dir -r requirements.txt
# Use gunicorn, not uwsgi, to avoid Python plugin issues
RUN pip3 install gunicorn

COPY ./app/ .
ENV RUNNING_IN_DOCKER=True
EXPOSE 7070
ENTRYPOINT ["gunicorn", "--workers=1", "--bind=0.0.0.0:7070", "main:app"]
# CMD ["python3", "-m" , "main:app", "--host=0.0.0.0", "--port=8080"]
