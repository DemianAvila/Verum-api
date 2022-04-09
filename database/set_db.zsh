#!/usr/bin/zsh

#ESTABLECE VARIABLES DE ENTORNO
source .env


#CREA Y PON EN OPERACION LA BASE DE DATOS
docker run \
 -p ${PORT_SERV}:${PORT_CONT} \
 -v ${INTERNAL_STORAGE}:${EXTERNAL_STORAGE} \
 --name ${MONGO_NAME} \
 -w ${WORKDIR} \
 -e MONGO_INITDB_ROOT_USERNAME=${MONGO_USER} \
 -e MONGO_INITDB_ROOT_PASSWORD=${MONGO_PASS} \
 -e MONGO_INITDB_DATABASE=${DATABASE} \
 -d mongo:${MONGOD_VER}


#COPIA EL SCRIPT DE MONGO HACIA EL CONTENEDOR
docker cp \
 "./set_internal_cont.js" \
 ${MONGO_NAME}:${WORKDIR}

#EJECUTA EL ARCHIVO DE INICIALIZACION
docker exec -it verum-db \
 mongo --host localhost -u ${MONGO_USER} -p ${MONGO_PASS} set_internal_cont.js 
