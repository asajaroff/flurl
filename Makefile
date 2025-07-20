APP_NAME := flurl

build-oci:
	docker build -t .

build:

dev:
	python3 -m flask --app $(APP_NAME) \
		run \
		--debug \
		--host 0.0.0.0 \
		--port 9090 \
		--reload \
		--debugger \
		--with-threads

db: init-db

init-db:
	python3 -m flask --app $(APP_NAME) \
		init-db


generate-dependencies:
	python3 -m pip freeze > requirements.txt

network:
	ip -br address show
