FROM debian:bullseye

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y nginx openssl


RUN mkdir /etc/nginx/certs

COPY conf/nginx.conf /etc/nginx/sites-available/default
RUN openssl req -newkey rsa:4096 -sha256 -x509 -days 100 -nodes -out /etc/nginx/certs/ssl.crt -keyout /etc/nginx/certs/ssl.key -subj "/C=ma/L=Khouribga/O=42/OU=1337kh/CN=ouaarabe/"

ENTRYPOINT ["nginx", "-g" ,"daemon off;"]
