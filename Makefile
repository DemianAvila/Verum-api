prepare:
	python3 create_env.py


include .env
build:
	docker compose up -d
	sleep 10
	docker exec -it ${MONGO_NAME} mongo -u ${MONGO_USER} -p ${MONGO_PASS} --authenticationDatabase admin set_internal_cont.js

kill:
	docker rm ${MONGO_NAME} --force
