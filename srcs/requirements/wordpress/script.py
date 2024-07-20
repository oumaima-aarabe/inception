#!/usr/bin/env python3

import os
import subprocess

# Modify php-fpm configuration
subprocess.run(['sed', '-i', 's|listen = /run/php/php7.4-fpm.sock|listen = 9000|g', '/etc/php/7.4/fpm/pool.d/www.conf'])

# Create /run/php directory if it doesn't exist
os.makedirs('/run/php', exist_ok=True)

# Navigate to WordPress directory
os.chdir('/var/www/html')

# Check if wp-config.php exists
# if os.path.isfile("wp-config-sample.php"):
subprocess.run(['mv',  '/var/www/html/wp-config-sample.php', '/var/www/html/wp-config.php'])

with open('/var/www/html/wp-config.php', 'r') as file:
    config_lines = file.readlines()

for i, line in enumerate(config_lines):
    if line.startswith("define( 'DB_NAME'"):
        config_lines[i] = (f"define( 'DB_NAME', '{os.getenv('MYSQL_DATABASE_NAME')}');")
    elif line.startswith("define( 'DB_USER'"):
        config_lines[i] = (f"define( 'DB_NAME', '{os.getenv('MYSQL_USER')}');")
    elif line.startswith("define( 'DB_PASSWORD'"):
        config_lines[i] = (f"define( 'DB_NAME', '{os.getenv('MYSQL_PASSWORD')}');")

# Write modified content back to wp-config.php
with open('/var/www/html/wp-config.php', 'w') as file:
    file.writelines(config_lines)

    # Install WordPress with administrative credentials
subprocess.run(['wp', 'core', 'install', '--url=' + os.getenv('WP_URL'), '--title=Inception',
                '--admin_user=' + os.getenv('WP_ADMIN_USER'), '--admin_password=' + os.getenv('WP_ADMIN_PASSWORD'),
                '--admin_email=' + os.getenv('WP_ADMIN_MAIL'), '--path=/var/www/html', '--allow-root'])
subprocess.run(['wp', 'user', 'create', os.getenv('WP_USER'), os.getenv('WP_USER_MAIL'),
                '--user_pass=' + os.getenv('WP_USER_PSWD'), '--path=/var/www/html', '--allow-root'])

# Set ownership of WordPress directory
subprocess.run(['chown', '-R', 'www-data:www-data', '/var/www/html'])

    # Start php-fpm
subprocess.run(['php-fpm7.4', '-F'])
