import subprocess

subprocess.run(['sed', '-i', 's|# maxmemory <bytes>|maxmemory 20mb|g', '/etc/redis/redis.conf'])

line = 'maxmemory-policy allkeys-lru'
with open('/etc/redis/redis.conf', 'r') as file:
    lines = file.readlines()
    if line not in lines:
        with open('/etc/redis/redis.conf', 'a') as file:
            file.write(line + '\n')
subprocess.run(["redis-server", "--protected-mode", "no"])
