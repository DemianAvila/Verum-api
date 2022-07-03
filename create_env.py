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
PORT_CONT=27017"""

    open(".env", 'w').write(env_string)

if __name__ == '__main__':
    main()
