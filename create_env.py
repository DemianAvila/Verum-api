import string
import random

def random_string():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10)) 


def main():
    env_string = f"""MONGO_NAME=Verum_db
MONGO_VER=4.2.21-bionic
MONGO_USER=verum_data_admin
MONGO_PASS={random_string()}
DATABASE=verum_administration
WORKDIR=/app
INTERNAL_STORAGE=./database/storage
EXTERNAL_STORAGE=/data/db
JS_CONFIG=./database/config
PORT_SERV=27017
PORT_CONT=27017
#################
PYTHON_NAME=Verum-controller
PYTHON_VER=3.10.4-bullseye
PORT_PY_SERVE=5001
PORT_PY_CONT=5001
WORKDIR_PY=/usr/src/app
INTERNAL_PY_STORAGE=./api/src
EXTERNAL_PY_STORAGE=/usr/src/app
#################
NGINX_VER=stable-perl
NGINX_NAME=verum_reverse_proxy
INTERNAL_NGINX_STORAGE=./rev_proxy/nginx.conf
EXTERNAL_NGINX_STORAGE=/etc/nginx/nginx.conf
PORT_NGINX_SERVE=80
PORT_NGINX_CONT=80"""



    open(".env", 'w').write(env_string)

if __name__ == '__main__':
    main()
