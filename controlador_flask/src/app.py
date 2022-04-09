#-----------------------------------------------
#IMPORTACION MODULOS
from crypt import methods
from flask import Flask
from flask_pymongo import PyMongo
from modulos import *

#-----------------------------------------------
#VARIABLES DE ENTORNO
vari = var("../../database/.env")

#-----------------------------------------------
#APP FLASK
app = Flask(__name__)
app.config["MONGO_URI"] = f"mongodb://localhost:{ vari['PORT_SERV'] }/{vari['DATABASE']}"

mongo = PyMongo(app)

#------------------------------------------------
#RUTAS
@app.route("/post_representante/", methods=["POST"])
def create_user():
    return {"STATUS":True}
    """
    ?nombre:<Nombre del usuario>&
    seg_nombre:<Segundo nombre del usuario>&
    a_paterno:<Apellido paterno del usuario>&
    a_materno:<Apellido materno del usuario>&
    ciudad:<Localización geografica del usuario>&
    user_type:<privilegios del usuario>&
    contrasenia:<contraseña del usuario>
    """
if __name__=="__main__":
    app.run(debug=True)