#!/bin/bash

service mariadb start


echo "CREATE DATABASE IF NOT EXISTS $MYSQL_DATABASE ;" > database.sql
echo "CREATE USER IF NOT EXISTS '$WP_ADMIN_USER'@'%' IDENTIFIED BY '$WP_ADMIN_PASSWORD' ;" >> database.sql
echo "GRANT ALL PRIVILEGES ON $MYSQL_DATABASE.* TO '$WP_ADMIN_USER'@'%' ;" >> database.sql
echo "FLUSH PRIVILEGES;" >> database.sql 

sed -i "s/bind-address.*/bind-address = 0.0.0.0/" /etc/mysql/mariadb.conf.d/50-server.cnf

mysql < database.sql
