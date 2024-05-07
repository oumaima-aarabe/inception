FROM debian:bullseye

RUN apt-get update -y && apt-get upgrade -y && apt-get install mariadb-server -y

RUN mkdir -p /var/run/mysqld \
    && chown -R mysql:mysql /var/run/mysqld && chmod 755 /var/run/mysqld

RUN mkdir -p /var/lib/mysql \
    && chown -R mysql:mysql /var/lib/mysql && chmod 755 /var/lib/mysql

ARG SQL_PASSWORD
ENV SQL_PASSWORD=$SQL_PASSWORD

ARG SQL_USER
ENV SQL_USER=$SQL_USER

ARG MYSQL_DATABASE
ENV MYSQL_DATABASE=$MYSQL_DATABASE

COPY script.sh /usr/local/bin/config.sh
RUN chmod +x /usr/local/bin/config.sh
RUN config.sh


ENTRYPOINT [ "mysqld" ] 
