FROM debian:bullseye


RUN apt-get update -y && apt-get upgrade -y && apt-get install mariadb-server -y

RUN mkdir -p /var/run/mysqld \
    && chown -R mysql:mysql /var/run/mysqld \
    && chmod 755 /var/run/mysqld

RUN mkdir -p /var/lib/mysql \
    && chown -R mysql:mysql /var/lib/mysql \
    && chmod 755 /var/lib/mysql

ARG WP_ADMIN_PASSWORD
ENV WP_ADMIN_PASSWORD=$WP_ADMIN_PASSWORD

ARG WP_ADMIN_USER
ENV WP_ADMIN_USER=$WP_ADMIN_USER

ARG WP_USER
ENV WP_USER=$WP_USER

ARG WP_USER_PASSWORD
ENV WP_USER_PASSWORD=$WP_USER_PASSWORD

ARG MYSQL_DATABASE
ENV MYSQL_DATABASE=$MYSQL_DATABASE

COPY tools/config.sh /usr/local/bin/config.sh
RUN chmod +x /usr/local/bin/config.sh
RUN config.sh


ENTRYPOINT [ "mysqld" ] 

