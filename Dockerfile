# DO NOT run print_badge.service concurrently with the same port number
FROM python:3.8-slim-buster AS print_badge

RUN apt update -y && \
    apt install -y libusb-1.0-0-dev usbutils
    # (optional) No need to install pip if python3 image is used
    # apt install -y python3-pip
    # (optional) No need to install fonts if provided in Python code
    # apt install -y ttf-mscorefonts-installer

COPY ./requirements.txt /
WORKDIR /
RUN pip3 install --no-cache-dir -r requirements.txt
# Use gunicorn, not uwsgi, to avoid Python plugin issues in Docker
RUN pip3 install gunicorn

COPY ./app/ .
ENV RUNNING_IN_DOCKER=True
EXPOSE 7070
ENTRYPOINT ["gunicorn", "--workers=1", "--bind=0.0.0.0:7070", "main:app"]
