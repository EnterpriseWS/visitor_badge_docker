# DO NOT run print_badge.service when this container is running
FROM python:3.8-slim-buster AS print_badge

RUN apt update -y && \
    apt install -y python3-pip && \
    # *** No need to install fonts if provided in Python code
    # apt install -y ttf-mscorefonts-installer && \
    apt install -y uwsgi-plugin-python3

COPY requirements.txt requirements.txt

WORKDIR /

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./ /
ENV RUNNING_IN_DOCKER=True
EXPOSE 8080
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0:8080"]
