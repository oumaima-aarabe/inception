FROM debian:bullseye

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y php php-fpm \
php-cgi php-cli php-mysql wget

WORKDIR /var/www/html

RUN wget https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar

RUN chmod +x wp-cli.phar
RUN mv wp-cli.phar /usr/local/bin/wp


COPY ./script.sh /usr/local/bin/script.sh
RUN chmod +x /usr/local/bin/script.sh

CMD ["script.sh"]