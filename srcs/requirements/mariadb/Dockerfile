FROM debian:bullseye

RUN apt-get update -y && apt-get install -y mariadb-server python3

COPY ./tools/script.py /
COPY ./conf/50-server.cnf /etc/mysql/mariadb.conf.d/

CMD ["python3", "script.py"]
