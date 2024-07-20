#!/usr/bin/env python3
import os
from os import system
import subprocess
import shutil
import time
# start the MariaDB service
system("service mariadb start")
time.sleep(5)
# subprocess.run(["chown",  "mysql:mysql", "/var/run/mysqld/"])
# subprocess.run(["chown",  "-R", "755", "/var/run/mysqld/"])
# subprocess.run(["service", "mariadb", "restart"])
user = f"""mysql_secure_installation << EOF > /dev/null 2>&1
n
{os.environ.get('MYSQL_PASSWORD')}
{os.environ.get('MYSQL_PASSWORD')}
y
n
n
n
n
EOF
"""
subprocess.run(user, shell=True, check=False)
# SQL commands
create_db_cmd = f"CREATE DATABASE IF NOT EXISTS {os.environ.get('MYSQL_DATABASE_NAME')};"
create_user_cmd = f"CREATE USER IF NOT EXISTS '{os.environ.get('MYSQL_USER')}'@'%' IDENTIFIED BY '{os.environ.get('MYSQL_PASSWORD')}';"
grant_privileges_cmd = f"GRANT ALL PRIVILEGES ON {os.environ.get('MYSQL_DATABASE_NAME')}.* TO '{os.environ.get('MYSQL_USER')}'@'%';"
alter_user_cmd = f"ALTER USER 'root'@'localhost' IDENTIFIED BY PASSWORD '{os.environ.get('MYSQL_PASSWORD')}';"
#reload table and update the user privileges in memory
flush_privileges_cmd = "FLUSH PRIVILEGES;"

# execute SQL commands with the option to excute sql statement provided and then exit 
for cmd in [create_db_cmd, create_user_cmd, grant_privileges_cmd, flush_privileges_cmd]:
    subprocess.run(["mysql", "-e", cmd])
system("mysqladmin shutdown -u root -p" + os.environ.get('MYSQL_PASSWORD'))
system("mariadb")
# while True:
#     pass