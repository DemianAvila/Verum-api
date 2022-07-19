#-----------------------------------------------
#IMPORTACION MODULOS
from flask import Flask
from flask_pymongo import PyMongo
from modulos import *
from flask import json
import logging

_logger = logging.getLogger(__name__)


#-----------------------------------------------
#VARIABLES DE ENTORNO
vari = var("./modulos/.env")

#-----------------------------------------------
#APP FLASK
app = Flask(__name__)
#app.config["MONGO_URI"] = f"mongodb://{vari['MONGO_USER']}:{vari['MONGO_PASS']}@172.18.0.2:{ vari['PORT_CONT'] }/{ vari['DATABASE'] }?authSource=admin"
app.config["MONGO_URI"] = f"mongodb://lecturas:d2UsuPRILO4n7KasPrAagESILYLZhP0J8WzWi46kUbg=@172.18.0.2:{ vari['PORT_CONT'] }/{ vari['DATABASE'] }?authSource=admin"
mongo = PyMongo(app)
#------------------------------------------------
#RUTAS
@app.route("/")
def ret():
    return "Hola mundo"
#----------------
#@app.route("/post_representante/", methods=["POST"])
@app.route("/post_representante")
def create_user():
    return {
        "STATUS":True,
        "app_database": str(app.config["MONGO_URI"])
    }
    """
    ?nombre:<Nombre del usuario>&
    seg_nombre:<Segundo nombre del usuario>&
    a_paterno:<Apellido paterno del usuario>&
    a_materno:<Apellido materno del usuario>&
    ciudad:<Localización geografica del usuario>&
    user_type:<privilegios del usuario>&
    contrasenia:<contraseña del usuario>
    """
#--------------------------------------------------
@app.route("/get_usuarios")
def get_usuarios():
    try:
        usuarios = mongo.db.representantes.find()
        print(mongo.db.list_collection_names(), flush=True)
    except Exception as error:
        print(str(error), flush = True)
        return app.response_class(
            response = json.dumps({
                'descripcion': "No se puede acceder a la base de datos en este momento"
                }
            ),
            status = 400,
            mimetype='application/json'
        )
            
    retorno_usuarios = []
    for usuario in usuarios:
        print("--------------------------------", flush=True)
        print(usuario, flush = True)
        print("--------------------------------", flush=True)
        nombre = [{usuario['nombre']},
            {usuario['seg_nombre']},
            {usuario['a_paterno']},
            {usuario['a_materno']}
        ]

        nombre = list(
            map(
                lambda x: x.strip(),
                nombre
            )
        )

        nombre = list(
            filter(
                lambda x: x!='',
                nombre
            )
        )

        nombre = ' '.join(nombre)

        retorno_usuarios.append(
            {
                'nombre': nombre
            }
        )

    return app.response_class(
        response = json.dumps(
            {
                'usuarios': retorno_usuarios,
            }
        ),
        status = 200,
        mimetype='application/json'
    )
#--------------------------------------------------
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
