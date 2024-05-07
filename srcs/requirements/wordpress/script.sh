#!/bin/bash

sed -i 's|listen = /run/php/php7.4-fpm.sock|listen = 9000|g' /etc/php/7.4/fpm/pool.d/www.conf 


mkdir -p /run/php

cd /var/www/html

if [ ! -f "/var/www/html/wp-config.php" ]; then
    echo "Creating wp-config.php"
    wp core download --path=/var/www/html --allow-root
    wp config create	--allow-root \
        --dbname=$MYSQL_DATABASE \
        --dbuser=$SQL_USER \
        --dbpass=$SQL_PASSWORD \
        --dbhost=mariadb:3306 --path='/var/www/html'

    wp core install --url=$WP_URL --title=Inception --path='/var/www/html' --admin_user=$WP_ADMIN_USER --admin_password=$WP_ADMIN_PASSWORD --admin_email=$WP_ADMIN_MAIL --allow-root
    wp user create $WP_USER $WP_USER_MAIL --user_pass=$WP_USER_PSWD --path='/var/www/html' --allow-root

    chown -R www-data:www-data /var/www/html

fi

php-fpm7.4 -F
