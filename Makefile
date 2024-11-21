DOCKER_COMPOSE = docker compose
IMAGE_NAME = sport_calendar:latest
CONTAINER_NAME = sport_calendar
VOLUME_NAME = sport_calendar_volume_database

###################### General #####################
.PHONY: all up build_up down build_only rm_vol clean fclean re

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
	docker volume rm $(VOLUME_NAME)

clean: down
	docker rmi $(IMAGE_NAME)

fclean: clean rm_vol 
	
re: down rm_vol build_up

