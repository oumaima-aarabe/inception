import subprocess

# Define the commands as lists of arguments
commands = [
    ['sed', '-i', 's|# maxmemory <bytes>|maxmemory 20mb|g', '/etc/redis/redis.conf']
]

# Execute each command
# for command in commands:
# subprocess.run(['sed', '-i', 's|# bind 127.0.0.1|bind 127.0.0.1|g', '/etc/redis/redis.conf'])
subprocess.run(['sed', '-i', 's|# maxmemory <bytes>|maxmemory 20mb|g', '/etc/redis/redis.conf'])

line = 'maxmemory-policy allkeys-lru'
with open('/etc/redis/redis.conf', 'a') as file:
            file.write(line + '\n')
subprocess.run(["redis-server", "--protected-mode", "no"])
