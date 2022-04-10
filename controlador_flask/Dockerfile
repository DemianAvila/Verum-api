ARG PYTHON_VER=3.10.4-bullseye
ARG PYTHON_NAME=verum-controller
ARG PORT_CONT=5000
ARG PORT_SERV=5000

#IMPORTA IMAGEN DE PYTHON
FROM python:$PYTHON_VER

EXPOSE 5000/tcp

#ESTABLECE EL WORKDIR
WORKDIR /usr/src/app

#COPIA EL REQUIREMENTS TXT
COPY requirements.txt ./

#INSTALA LOS REQUIREMENTS
RUN pip install --no-cache-dir -r requirements.txt

#COPIA LA CARPETA SRC
COPY src /usr/src/app


CMD [ "python", "app.py" ]