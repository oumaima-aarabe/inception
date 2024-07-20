FROM debian:bullseye

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y nginx openssl

COPY conf/nginx.conf /etc/nginx/sites-enabled/default

RUN mkdir /etc/nginx/certs
RUN openssl req -newkey rsa:4096 -sha256 -x509 -days 100 -nodes -out /etc/nginx/certs/ssl.crt -keyout /etc/nginx/certs/ssl.key -subj "/C=ma/L=Khouribga/O=42/OU=1337kh/CN=ouaarabe/"

ENTRYPOINT ["nginx", "-g" ,"daemon off;"]

#daemon off; permet de lancer nginx en mode foreground to become the main process for the C PID=1
