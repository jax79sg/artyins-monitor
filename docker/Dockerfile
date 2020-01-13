FROM openjdk:slim
COPY --from=python:3.6-slim / /
RUN apt update && \
    apt install -y git build-essential wget  libyaml-dev 
RUN git clone https://github.com/jax79sg/artyins-monitor
WORKDIR artyins-monitor
ENTRYPOINT ["python3","monitor.py","&"]

