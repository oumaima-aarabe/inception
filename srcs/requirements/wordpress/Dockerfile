FROM debian:bullseye

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y  python3 php php-fpm \
php-cgi php-cli php-mysql wget  php-redis

WORKDIR /var/www/html

RUN wget https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar

RUN chmod +x wp-cli.phar

RUN mv wp-cli.phar /usr/local/bin/wp
RUN wp core download --path=/var/www/html --allow-root

COPY ./script.py /
COPY ./wp-config.php /var/www/html/wp-config.php

ENTRYPOINT [ "python3",  "/script.py"]


#/etc/php- fpm. conf. 