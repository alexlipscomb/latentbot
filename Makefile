COMPOSE=docker compose

init:
	pdm install

build:
	${COMPOSE} build

up:
	${COMPOSE} up -d

stop:
	${COMPOSE} stop

down:
	${COMPOSE} down

local:
	pdm run python -m latentbot
