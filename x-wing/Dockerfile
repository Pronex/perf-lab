# Jesko Mueller (c) 2021
# ZHAW CCP1-PERF | Performance Analysis Example Lab
# dockerfile for x-wing that sends memcached requests

FROM python:alpine3.12

RUN pip install python-binary-memcached \
    && mkdir /app
WORKDIR /app
COPY x-wing/x-wing.py .

# entrypoint and starting command
ENTRYPOINT ["python", "/app/x-wing.py"]