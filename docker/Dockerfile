#FROM openjdk:slim
#COPY --from=python:3.6-slim / /
FROM python:3.6-slim
RUN apt update && \
    apt install -y git build-essential wget  libyaml-dev 
RUN mkdir /logs && \
    mkdir /shareddata && \
    git clone https://github.com/jax79sg/artyins-monitor && \
    cd artyins-monitor && \
    pip install -r requirements.txt && \
    ./setup_prerequisites.sh
WORKDIR artyins-monitor
ENTRYPOINT ["python3","monitor.py"]
