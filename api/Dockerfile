ARG PYTHON_VER=3.10.4-bullseye

#IMPORTA IMAGEN DE PYTHON
FROM python:$PYTHON_VER

EXPOSE 5001/tcp

#ESTABLECE EL WORKDIR
WORKDIR /usr/src/app

#COPIA EL REQUIREMENTS TXT
#COPY ./src/requirements.txt ./                                                                                                 

#INSTALA LOS REQUIREMENTS
#RUN ["pip", "install", "--no-cache-dir", "-r", "requirements.txt"]
RUN ["pip", "install", "--no-cache-dir", "fastapi", "uvicorn", "pydantic", "pymongo", "python-dotenv"]
#RUN ["echo", "Hola"]

#COPIA LA CARPETA SRC
COPY src /usr/src/app

#CMD [ "python", "app.py" ]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0","--port", "5001", "--reload"]
