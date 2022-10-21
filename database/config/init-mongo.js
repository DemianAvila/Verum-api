//CREA LA BASE DE DATOS DE VERUM
db = db.getSiblingDB("verum_administration");

//CREAR COLECCION DE CORREOS

db.correos.insert({
    _id: "0",
    correo: "luisvenzel@gmail.com"
})
db.correos.insert({
    _id: "1",
    correo: "direcciongeneral@verumexico.com"
})

//INSERTA UN DATO PARA HACER EXISTIR ESA BASE DE DATOS
db.usuarios.insert({
    nombre: "Luis",
    seg_nombre: "Wenceslao",
    a_paterno: "De Ignacio",
    a_materno: "Hernández",
    ciudad: "Ecatepec, Estado de México",
    activo: true,
    user_type: 1,
    fecha_modificacion: Date(),
    fecha_creacion: Date(),
    correos: ["0", "1"],
    contrasenia: null,
    sha_code:null
});
//CREA DENTRO DE ESA BASE DE DATOS UN ROL DE LECTURA
db.createRole(
    {
      role: "lectura", 
      privileges: [
        {
          actions: [ "find" ],
          resource: { db: "verum_administration",
          collection: ""}
        }
      ],
      roles: []
    }
)
//CREA DENTRO DE ESA BASE DE DATOS UN ROL DE ESCRITURA
db.createRole(
    {
      role: "escritura", 
      privileges: [
        {
          actions: [ "insert" ],
          resource: { db: "verum_administration",
          collection: ""}
        }
      ],
      roles: []
    }
)
//CREA DENTRO DE ESA BASE DE DATOS UN ROL DE ACTUALIZACION
db.createRole(
    {
      role: "actualizacion", 
      privileges: [
        {
          actions: [ "update" ],
          resource: { db: "verum_administration",
          collection: ""}
        }
      ],
      roles: []
    }
)
//---------------------------------------------------------
db.createUser (
    {
        user: "lecturas",
        pwd: "ofkvaszopi",
        roles: ["lectura"] 
    }
);
db.createUser (
    {
        user: "escrituras",
        pwd: "tvsouslklw",
        roles: ["escritura"]
    }
);
db.createUser (
    {
        user: "actualizaciones",
        pwd: "snnqaygwcy",
        roles: ["actualizacion"]
    }
);
    