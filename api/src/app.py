from fastapi import FastAPI, Depends, Request, Response, status
from modulos import *
from pymongo import MongoClient
from pydantic import BaseModel, Extra, ValidationError, validator
from typing import Optional, List
from hashlib import sha512
from datetime import datetime
from base64 import b64encode

#VARIABLES DE ENTORNO
vari = var("./modulos/.env")

#INSTANCIA FAST API
app = FastAPI(docs_url = "/verum_backend/")

#MODELOS

class Mail (BaseModel, extra=Extra.forbid):
    mail: str = ""
    @validator('mail')
    def validate_mail(cls, v):
        #SPLIT THE VALUE WITH @, ONLY 2 PARTS ACCEPTED
        if len(v.split('@')) != 2:
            raise ValueError("There can only be an @ in an email address")
        else:
            name, domain = v.split('@')
            #THE DOMAIN MUST SPLITED BY DOT
            if len(domain.split('.')) < 2:
                raise ValueError("Domain has no extention")

        return v


class UserGet(BaseModel, extra=Extra.forbid):
    id_usuario: Optional[str] = ""
    nombre: Optional[str] = ""
    s_nombre: Optional[str] = ""
    apellido_p: Optional[str] = ""
    apellido_m: Optional[str] = ""
    ciudad: Optional[str] = ""
    activo: Optional[bool] = True
    categoria_usuario: Optional[int] = 0
    fecha_modificacion: Optional[str] = ""
    fecha_creacion: Optional[str] = ""
    correos: Optional[List["Mail"]] = []
    contrasenia: Optional[str] = ""
    sha_code: Optional[str] = ""

class UserGetList(BaseModel, extra=Extra.forbid):
    users: Optional[List['UserGet']] = []

class UserPost(BaseModel, extra=Extra.forbid):
    nombre: Optional[str] = ""
    s_nombre: Optional[str] = ""
    apellido_p: Optional[str] = ""
    apellido_m: Optional[str] = ""
    ciudad: Optional[str] = ""
    categoria_usuario: Optional[int] = 0
    correos: Optional[List["Mail"]] = []
    contrasenia: Optional[str] = ""



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
lect_mail_coll = lect_db['correos']



@app.get("/verum_backend/get_users")
async def get_users(request: Request,
        response: Response,
        commons: UserGet = Depends()):
    #LIST TO STORE USERS 
    users = []
    #FOR EACH ONE OF THE USERS
    for user in lect_usr_coll.find():
        #GET THE MAILS OF THE USER ACCORDIND TO ID
        mails = []
        for mail_id in user['correos']:
            #print(mail_id ,flush=True)
            #print((lect_mail_coll.find_one({"_id": str(mail_id)})), flush=True)
            mail = lect_mail_coll.find_one({"_id": str(mail_id)})
            mails.append(
                Mail(
                    mail = mail['correo']
                )
            )
        print(user.get("_id"))
        users.append(
            UserGet(
                id_usuario= str(user.get("_id")),
                nombre = user['nombre'],
                s_nombre = user['seg_nombre'],
                apellido_p = user['a_paterno'],
                apellido_m = user['a_materno'],
                ciudad = user['ciudad'],
                activo = user['activo'],
                categoria_usuario = user['user_type'],
                fecha_modificacion = str(user['fecha_modificacion']),
                fecha_creacion = str(user['fecha_creacion']),
                correos = mails,
                contrasenia = user['contrasenia'],
                sha_code = user['sha_code']
            )
        )

    return {
        "users": UserGetList(
            users = users
        )
    }

@app.post("/verum_backend/post_user")
async def post_user(request: Request,
        response: Response):
        #commons: UserPost = Depends()):
    try:
        req = await request.json()
    except:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "DESCRIPTION": "Couldn't get request"
        }
    #FOR EACH MAIL, CHECK IF NOT IN DB
    mails = []
    for mail in req['correos']:
        repeated_mail = lect_mail_coll.find_one({"correo": mail})
        # IF MAIL IN DB SEND ALERT
        if repeated_mail != None:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {
                "DESCRIPTION": f"E-mail {mail} already registred"
            }
        #EMPTY THE MAILS IN AN ARRAY OF OBJECTS
        else:
            try:
                mails.append(
                    Mail(mail = mail)
                )
            #CHECK FOR THE VALIDATIONS OF THE CLASS
            except ValueError as e:
                response.status_code = status.HTTP_400_BAD_REQUEST
                return {
                        "DESCRIPTION": str(e)
                }
    #REMOVE MAILS FROM THE REQUEST
    del req['correos']
    try:
        user = UserPost(**req)
        user.correos = mails
    except ValidationError as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        print(str(e))
        return {
            "DESCRIPTION": "Something went wrong with the request",
            "TRACEBACK": str(e)
        }
    #NOW DATETIME
    now = datetime.now()
    #THE SHA CODE OF EACH USER
    sha_code = user.nombre + user.s_nombre + user.apellido_p + user.apellido_m + \
        user.ciudad + str(user.categoria_usuario) + str(now)
    #FOR EACH ONE OF THE MAILS
    mail_id = []
    for mail in user.correos:
        #INSERT IN DATABASE AND APPEND TO ID
    #POST THE RESULT AND GET THE ID
    new_user = {
            "nombre": user.nombre,
            "seg_nombre": user.s_nombre,
            "a_paterno": user.apellido_p,
            "a_materno": user.apellido_m,
            "ciudad": user.ciudad,
            "activo": True,
            "user_type": user.categoria_usuario,
            "fecha_modificacion": now,
            "fecha_creacion": now,
            "correos": user.correos,
            "contrasenia": sha512(b"{user.contrasenia}").hexdigest(),
        }
    new_user_id = lect_usr_coll.insert_one(new_user).inserted_id
    sha_code = bytes(f"{str(new_user_id) + sha_code}", 'utf-8')
    sha_code = sha512(sha_code).digest()
    print(sha_code)
    sha_code = b64encode(sha_code).decode()
    print(sha_code)
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

    """
    response.status_code = status.HTTP_201_CREATED
    return {
        "created_usr": new_user_id
    }
    """
