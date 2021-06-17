USER_ID := $(shell id -u)
GROUP_ID := $(shell id -g)

export USER_ID
export GROUP_ID

build: 
	docker-compose build

up:
	docker-compose up

bash: 
	docker-compose run --rm web /bin/bash
