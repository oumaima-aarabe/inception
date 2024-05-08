FROM debian:bullseye

FROM debian:bullseye

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y mariadb-server python3

COPY script.py /

RUN chmod +x /script.py

COPY 50-server.cnf /etc/mysql/mariadb.conf.d/

CMD ["python3", "/script.py"]
