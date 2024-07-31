up: dir
	docker compose -f ./srcs/docker-compose.yml up --build

upd: dir
	docker compose -f ./srcs/docker-compose.yml up --build -d

dir:
	@mkdir -p /home/ouaarabe/data
	@mkdir -p /home/ouaarabe/data/wordpress
	@mkdir -p /home/ouaarabe/data/mariadb


down: stop
	docker compose -f ./srcs/docker-compose.yml down --rmi all  --volumes
	sudo rm -rf /home/ouaarabe/data/*

stop: 
	docker compose -f ./srcs/docker-compose.yml stop

prune: down
	docker system prune -af

re: prune up

network:
	docker network inspect inception


exec:
	docker exec -it ${c} /bin/bash

logs:
	docker compose logs ${c}

volumes:
    docker volume ls

volumes_rm:
    docker volume rm ${v}

volume_inspect:
    docker volume inspect ${v}