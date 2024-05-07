#!/bin/bash

service mariadb start

if [ ! -d "/var/lib/mysql/${MYSQL_DATABASE}" ]; then
    echo "CREATE DATABASE IF NOT EXISTS $MYSQL_DATABASE ;" > database.sql
    echo "CREATE USER IF NOT EXISTS '$SQL_USER'@'%' IDENTIFIED BY '$SQL_PASSWORD' ;" >> database.sql
    echo "GRANT ALL PRIVILEGES ON $MYSQL_DATABASE.* TO '$SQL_USER'@'%' ;" >> database.sql
    echo "FLUSH PRIVILEGES;" >> database.sql
fi

sed -i "s/bind-address.*/bind-address = 0.0.0.0/" /etc/mysql/mariadb.conf.d/50-server.cnf

mysql < database.sql
