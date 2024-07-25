FROM debian:bullseye

# Update and Install Redis
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y redis-server  && \
    apt-get install -y python3

# # Expose Redis port
EXPOSE 6379

COPY ./conf.py /
ENTRYPOINT [ "python3",  "/conf.py"]


#docker exec -it redis redis-cli monitor
# Bind Address: Set to 127.0.0.1 to ensure Redis only listens on the localhost, enhancing security.
# Max Memory: Limited to 20mb to control Redis's memory usage and prevent it from consuming excessive system resources.
# Max Memory Policy: Set to allkeys-lru to specify the eviction strategy when the memory limit is reached, favoring the removal of less recently used keys.