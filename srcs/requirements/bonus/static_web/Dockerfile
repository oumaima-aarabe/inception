FROM debian:bullseye

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y nginx

COPY ./conf/nginx.conf /etc/nginx/sites-enabled/default

COPY ./tools/ /var/www/html/

CMD ["nginx", "-g", "daemon off;"]

