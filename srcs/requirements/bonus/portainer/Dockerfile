FROM debian:bullseye

RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN curl -L https://github.com/portainer/portainer/releases/download/2.19.5/portainer-2.19.5-linux-amd64.tar.gz -o portainer.tar.gz tar -xzvf portainer.tar.gz rm portainer.tar.gz

EXPOSE 9000

CMD ["/portainer/portainer"]