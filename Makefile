up: dir
	docker compose -f ./srcs/docker-compose.yml up --build

upd: dir
	docker compose -f ./srcs/docker-compose.yml up --build -d

dir:
	@mkdir -p /home/ouaarabe/data
	@mkdir -p /home/ouaarabe/data/wordpress
	@mkdir -p /home/ouaarabe/data/mariadb

stop: 
	docker compose -f ./srcs/docker-compose.yml stop

down:
	docker compose -f ./srcs/docker-compose.yml stop
	docker compose -f ./srcs/docker-compose.yml down --rmi all  --volumes
	sudo rm -rf /home/ouaarabe/data/*


prune: down
	docker system prune -af

re: down
	docker compose -f ./srcs/docker-compose.yml down -v
	$(MAKE) up


network:
	docker network inspect inception


exec:
	docker exec -it ${c} /bin/bash

logs:
	docker compose logs ${c}