#!/usr/bin/zsh

#ESTABLECE VARIABLES DE ENTORNO
source .env

#CREA Y PON EN OPERACION EL CONTROLADOR
docker run \
 -p ${PORT_SERV}:${PORT_CONT} \
 --name ${PYTHON_NAME} \
 -w ${WORKDIR} \
 -d python:${PYTHON_VER}

#COPIA TODO EL SCRIPT DEL PROYECTO HACIA EL WORKDIRECTORY
docker cp \
 "./src" \
 ${PYTHON_NAME}:${WORKDIR}

#EJECUTA PIP PARA INSTALAR LOS REQUERIMIENTOS
docker exec -it verum-db \
 pip install -r /app/src/requirements.txt