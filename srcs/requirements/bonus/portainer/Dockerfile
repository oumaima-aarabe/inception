FROM debian:bullseye

RUN apt-get update && apt-get install -y curl

RUN curl -L https://github.com/portainer/portainer/releases/download/2.19.5/portainer-2.19.5-linux-amd64.tar.gz -o portainer.tar.gz && tar -xzvf portainer.tar.gz && rm portainer.tar.gz

CMD ["/portainer/portainer"]