import string
import random

def random_string():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10)) 


def main():

    mongo_read_pass = random_string()
    mongo_write_pass = random_string()
    mongo_update_pass = random_string()
    mongo_read_usr = "lecturas"
    mongo_write_usr = "escrituras"
    mongo_update_usr = "actualizaciones"
    verum_database = "verum_administration"

    env_string = f"""MONGO_NAME=Verum_db
MONGO_VER=4.2.21-bionic
MONGO_USER=verum_data_admin
MONGO_PASS={random_string()}
DATABASE={verum_database}
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
PORT_NGINX_CONT=80
INTERNAL_CERTS_STORAGE=./rev_proxy/certs
EXTERNAL_CERTS_STORAGE=/app
PORT_TCP_EXT=81
PORT_TCP_INT=81
#############
DB_READ_USR={mongo_read_usr}
DB_READ_PASS={mongo_read_pass}
DB_WRITE_USR={mongo_write_usr}
DB_WRITE_PASS={mongo_write_pass}
DB_UPDATE_USR={mongo_update_usr}
DB_UPDATE_PASS={mongo_update_pass}"""
    
    db_init=f"""//CREA LA BASE DE DATOS DE VERUM
db = db.getSiblingDB("{verum_database}");
//INSERTA UN DATO PARA HACER EXISTIR ESA BASE DE DATOS
db.usuarios.insert({{
    nombre: "Luis",
    seg_nombre: "Wenceslao",
    a_paterno: "De Ignacio",
    a_materno: "Hernández",
    ciudad: "Ecatepec, Estado de México",
    activo: true,
    user_type: 1,
    fecha_modificacion: Date(),
    contrasenia: null,
    sha_code:null
}});
//CREA DENTRO DE ESA BASE DE DATOS UN ROL DE LECTURA
db.createRole(
    {{
      role: "lectura", 
      privileges: [
        {{
          actions: [ "find" ],
          resource: {{ db: "{verum_database}",
          collection: ""}}
        }}
      ],
      roles: []
    }}
)
//CREA DENTRO DE ESA BASE DE DATOS UN ROL DE ESCRITURA
db.createRole(
    {{
      role: "escritura", 
      privileges: [
        {{
          actions: [ "insert" ],
          resource: {{ db: "{verum_database}",
          collection: ""}}
        }}
      ],
      roles: []
    }}
)
//CREA DENTRO DE ESA BASE DE DATOS UN ROL DE ACTUALIZACION
db.createRole(
    {{
      role: "actualizacion", 
      privileges: [
        {{
          actions: [ "update" ],
          resource: {{ db: "{verum_database}",
          collection: ""}}
        }}
      ],
      roles: []
    }}
)
//---------------------------------------------------------
db.createUser (
    {{
        user: "{mongo_read_usr}",
        pwd: "{mongo_read_pass}",
        roles: ["lectura"] 
    }}
);
db.createUser (
    {{
        user: "{mongo_write_usr}",
        pwd: "{mongo_write_pass}",
        roles: ["escritura"]
    }}
);
db.createUser (
    {{
        user: "{mongo_update_usr}",
        pwd: "{mongo_update_pass}",
        roles: ["actualizacion"]
    }}
);
    """

    #WRITE IN ROOT DIRECTORY
    open(".env", 'w').write(env_string)
    #WRITE IN API DIRECTORY
    open("./api/src/modulos/.env", 'w').write(env_string)
    #WRITE IN DATABASE CONFIG DIRECTORY
    open("./database/config/init-mongo.js", 'w').write(db_init)

if __name__ == '__main__':
    main()
