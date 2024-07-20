up:
	@mkdir -p /home/ouaarab/data/wordpress
	@mkdir -p /home/ouaarab/data/mariadb
	docker compose -f ./srcs/docker-compose.yml up --build 

down:
	docker compose -f ./srcs/docker-compose.yml down --rmi all  --volumes
	docker system prune -af

re: down
	docker compose -f ./srcs/docker-compose.yml down -v
	sudo rm -rf /home/ouaarab/data/*
	$(MAKE) up

#docker exec mariadb bash   