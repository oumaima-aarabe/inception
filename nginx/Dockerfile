# FROM debian:bullseye

# RUN apt-get update && apt-get upgrade -y  \
#     && apt-get install -y nginx openssl

# COPY /certs /etc/
# COPY /conf/ /etc/nginx/sites-available/

# # RUN openssl req -newkey rsa:2307 -sha512 -x509 -days 356 -nodes -out /etc/nginx/ssl/ssl.crt -keyout /etc/nginx/ssl/ssl.key -subject"/L=Khouribga/O=42/OU=1337kh/CN=ouaarabe"
# # COPY ./nginx.conf /etc/nginx/conf.d/default.conf
# # #default config fil dyal nginx
# # #available sites 

# ENTRYPOINT ["nginx", "-g", "daemon off;"]
# # ENTRYPOINT ["tail","-f","/dev/null" ]
# # CMD tail -f /dev/null

FROM debian:bullseye

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y nginx openssl


RUN mkdir /etc/nginx/ssl

COPY conf/nginx.conf /etc/nginx/sites-available/default
RUN openssl req -newkey rsa:4096 -sha256 -x509 -days 100 -nodes -out /etc/nginx/ssl/ssl.crt -keyout /etc/nginx/ssl/ssl.key -subj "/C=ma/L=Khouribga/O=42/OU=1337kh/CN=ouaarabe/"

ENTRYPOINT ["nginx", "-g" ,"daemon off;"]


