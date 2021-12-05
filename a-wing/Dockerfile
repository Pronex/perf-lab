# Jesko Mueller (c) 2021
# ZHAW CCP1-PERF | Performance Analysis Example Lab
# dockerfile for a-wing that sends memcached requests

FROM python:alpine3.12

RUN pip install python-binary-memcached \
    && mkdir /app
WORKDIR /app
COPY a-wing/a-wing.py .

# entrypoint and starting command
ENTRYPOINT ["python", "/app/a-wing.py"]