FROM openjdk:slim
COPY --from=python:3.6-slim / /
RUN apt update && \
    apt install -y git build-essential wget 
RUN git clone https://github.com/jax79sg/artyins-monitor
RUN cd artyins-monitor && \
    ./setup_prerequisites.sh
WORKDIR artyins-monitor
ENTRYPOINT ["python3","monitor.py","&"]

