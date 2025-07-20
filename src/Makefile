APP_NAME := flurl

build-oci:
	docker build -t .

build:

dev:
	python3 -m flask --app $(APP_NAME) \
		run \
		--host=0.0.0.0 \
		--port 9090 \
		--debugger \
		--reload \
		--with-threads

generate-dependencies:
	python3 -m pip freeze > requirements.txt

network:
	ip -br address show
