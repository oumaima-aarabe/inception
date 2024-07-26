#!/usr/bin/env python3

from  os import system
import os
import subprocess
import time
time.sleep(10)
subprocess.run(['service', 'php7.4-fpm', 'start'])
# Modify php-fpm configuration
subprocess.run(['sed', '-i', 's|listen = /run/php/php7.4-fpm.sock|listen = 9000|g', '/etc/php/7.4/fpm/pool.d/www.conf'])

# Check if wp-config.php exists
# if os.path.isfile("wp-config-sample.php"):
# subprocess.run(['mv',  '/var/www/html/wp-config-sample.php', '/var/www/html/wp-config.php'])
# subprocess.run(['cp', '/var/www/html/wp-config.php', '/var/www/html/wp-config.php.bak'])


    # Install WordPress with administrative credentials
subprocess.run(['wp', 'core', 'install', '--url=' + os.getenv('WP_URL'), '--title=Inception',
                '--admin_user=' + os.getenv('WP_ADMIN_USER'), '--admin_password=' + os.getenv('WP_ADMIN_PASSWORD'),
                '--admin_email=' + os.getenv('WP_ADMIN_MAIL'), '--path=/var/www/html', '--allow-root'])
subprocess.run(['wp', 'user', 'create', os.getenv('WP_USER'), os.getenv('WP_USER_MAIL'),
                '--user_pass=' + os.getenv('WP_USER_PSWD'), '--path=/var/www/html', '--allow-root'])
#plugins redis
subprocess.run(['wp', 'plugin', 'install', 'redis-cache', '--activate', '--path=/var/www/html', '--allow-root'])
subprocess.run(['wp', 'plugin', 'update', '--all', '--path=/var/www/html', '--allow-root'])
subprocess.run(['wp', 'redis', 'enable',  '--path=/var/www/html', '--allow-root'])

# Set ownership of WordPress directory
subprocess.run(['chown', '-R', 'www-data:www-data', '/var/www/html'])
subprocess.run(['service', 'php7.4-fpm', 'stop'])
    # Start php-fpm
subprocess.run(['php-fpm7.4', '-F'])
