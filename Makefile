up:
	@mkdir -p /tmp/wordpress
	@mkdir -p /tmp/mariadb
	docker compose -f ./requirements/docker-compose.yml up --build 

down:
	docker compose -f ./requirements/docker-compose.yml down --rmi all 

re: down
	docker compose -f ./requirements/docker-compose.yml down -v
	rm -rf /tmp/mariadb/*
	rm -rf /tmp/wordpress/*
	$(MAKE) up