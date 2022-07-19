#CREATE ENV FILE
prepare:
	touch .env
	python3 create_env.py

#CREATE SELF CERTIFICTES AND MOVE THEM INTO REVERSE PROXY DIR
certificates:
	openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout localhost.key -out localhost.crt
	mv localhost* ./rev_proxy/certs	

include .env
build:
	docker compose up -d

init:
	docker exec ${MONGO_NAME} mongo -u ${MONGO_USER} -p ${MONGO_PASS} --authenticationDatabase admin set_internal_cont.js

kill:
	#RUN AS SUDO
	docker rm ${MONGO_NAME} --force
	docker rm ${PYTHON_NAME} --force
	docker rm ${NGINX_NAME} --force
	rm -rf ./database/storage/*
