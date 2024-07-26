FROM debian:bullseye

RUN apt-get update  && apt-get install -y --no-install-recommends \
    wget php php-mysqli \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 

WORKDIR /var/www

RUN wget --no-check-certificate https://www.adminer.org/latest.php -O adminer.php 

RUN mv adminer.php index.php

CMD ["php", "-S", "0.0.0.0:80"]