#!/usr/bin/env python3
import os
from os import system
import subprocess
import shutil
# start the MariaDB service
subprocess.run(["service", "mariadb", "start"])

# SQL commands
create_db_cmd = f"CREATE DATABASE IF NOT EXISTS {os.environ.get('MYSQL_DATABASE')};"
create_user_cmd = f"CREATE USER IF NOT EXISTS '{os.environ.get('SQL_USER')}'@'%' IDENTIFIED BY '{os.environ.get('SQL_PASSWORD')}';"
grant_privileges_cmd = f"GRANT ALL PRIVILEGES ON {os.environ.get('MYSQL_DATABASE')}.* TO '{os.environ.get('SQL_USER')}'@'%';"
#reload table and update the user privileges in memory
flush_privileges_cmd = "FLUSH PRIVILEGES;"

# execute SQL commands with the option to excute sql statement provided and then exit 
for cmd in [create_db_cmd, create_user_cmd, grant_privileges_cmd, flush_privileges_cmd]:
    subprocess.run(["mysql", "-e", cmd])
while True:
    pass

# modify the MariaDB configuration file
# mariadb_conf = "/etc/mysql/mariadb.conf.d/50-server.cnf"
# with open(mariadb_conf, "r") as f:
#     lines = f.readlines()
# with open(mariadb_conf, "w") as f:
#     for line in lines:
#         if line.startswith("bind-address"):
#             f.write("bind-address = 0.0.0.0\n")
#         else:
#             f.write(line)