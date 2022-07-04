#-----------------------------------------------
#IMPORTACION MODULOS
from flask import Flask
from flask_pymongo import PyMongo
from modulos import *

#-----------------------------------------------
#VARIABLES DE ENTORNO
vari = var("./modulos/.env")

#-----------------------------------------------
#APP FLASK
app = Flask(__name__)
"""
app.config["MONGO_URI"] = f"mongodb://{vari['PUBLIC_DNS']}:{ vari['PORT_SERV'] }/{vari['DATABASE']}"

mongo = PyMongo(app)
"""
#------------------------------------------------
#RUTAS
@app.route("/")
def ret():
    return "Hola mundo"
#----------------
#@app.route("/post_representante/", methods=["POST"])
@app.route("/post_representante")
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
    app.run(debug=True, host='0.0.0.0', port=5001)
