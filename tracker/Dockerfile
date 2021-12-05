# Jesko Mueller (c) 2021
# ZHAW CCP1-PERF | Performance Analysis Example Lab
# dockerfile for tracker that fetches memcached items

FROM python:alpine3.12

RUN pip install python-binary-memcached \
    && mkdir /app
WORKDIR /app
COPY tracker/tracker.py .

# entrypoint and starting command
ENTRYPOINT ["python", "/app/tracker.py"]