DOCKER_COMPOSE = docker compose

###################### General #####################
.PHONY: all up build_up down build_only rm_vol fclean re

all: up

up:
	${DOCKER_COMPOSE} up

down:
	${DOCKER_COMPOSE} down

build:
	${DOCKER_COMPOSE} build

build-nc:
	${DOCKER_COMPOSE} build --no-cache

rm_vol:
	docker volume prune -af

clean: down
	docker system prune -f

fclean: down rm_vol 
	docker system prune -af

re: down rm_vol build_up



