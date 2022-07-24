from fastapi import FastAPI
from modulos import *
from pymongo import MongoClient
from pydantic import BaseModel, Extra
from typing import Optional, List
from hashlib import sha512
from datetime import datetime
from base64 import b64encode

#VARIABLES DE ENTORNO
vari = var("./modulos/.env")

#INSTANCIA FAST API
app = FastAPI()

#MODELOS
class User(BaseModel, extra=Extra.forbid):
    id_usuario: Optional[str] = ""
    nombre: Optional[str] = ""
    s_nombre: Optional[str] = ""
    apellido_p: Optional[str] = ""
    apellido_m: Optional[str] = ""
    ciudad: Optional[str] = ""
    activo: Optional[bool] = True
    categoria_usuario: Optional[int] = 0
    fecha_modificacion: Optional[str] = ""
    contrasenia: Optional[str] = ""
    sha_code: Optional[str] = ""

class UserList(BaseModel, extra=Extra.forbid):
    users: Optional[List['User']] = []



#INSTANCIAS DE CONEXION MONGO (DETRAS DEL PROXY)
lectura = mongo_client(
        client_object = MongoClient,
        user = vari['MONGO_USER'],
        passwd = vari['MONGO_PASS'],
        port = vari['PORT_TCP_INT'],
        host = "nginx_proxi",
        database = vari['DATABASE']
    )

lect_db = lectura[vari['DATABASE']]
lect_usr_coll = lect_db['usuarios']



@app.get("/verum_backend/get_users")
async def get_users():
    users = []
    for user in lect_usr_coll.find():
        print(user.get("_id"))
        users.append(
            User(
                id_usuario= str(user.get("_id")),
                nombre = user['nombre'],
                s_nombre = user['seg_nombre'],
                apellido_p = user['a_paterno'],
                apellido_m = user['a_materno'],
                ciudad = user['ciudad'],
                activo = user['activo'],
                categoria_usuario = user['user_type'],
                fecha_modificacion = str(user['fecha_modificacion']),
                contrasenia = user['contrasenia'],
                sha_code = user['sha_code']
            )
        )

    return {
        "users": UserList(
            users = users
        )
    }

@app.post("/verum_backend/post_user")
async def post_user(user: User):
    #NOW DATETIME
    now = datetime.now()
    #THE SHA CODE OF EACH USER
    sha_code = user.nombre + user.s_nombre + user.apellido_p + user.apellido_m + \
        user.ciudad + str(user.activo) + str(user.categoria_usuario) + str(now)
    #POST THE RESULT AND GET THE ID
    new_user = {
            "nombre": user.nombre,
            "seg_nombre": user.s_nombre,
            "a_paterno": user.apellido_p,
            "a_materno": user.apellido_m,
            "ciudad": user.ciudad,
            "activo": user.activo,
            "user_type": user.categoria_usuario,
            "fecha_modificacion": now,
            "contrasenia": sha512(b"{user.contrasenia}").hexdigest(),
        }
    new_user_id = lect_usr_coll.insert_one(new_user).inserted_id
    sha_code = sha512(b"{str(new_user_id) + sha_code}").digest()
    sha_code = b64encode(sha_code).decode()
    #UPDATE THE RECORD WITH SHA CODE
    lect_usr_coll.update_one(
        {
            "_id": new_user_id
        },
        {
            "$set":{
                "sha_code": sha_code
            }
        }
    )


    return None
