//CREA LA BASE DE DATOS DE VERUM
db = db.getSiblingDB("verum_administration");
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
        pwd: "szxpxjcxhz",
        roles: ["lectura"] 
    }
);
db.createUser (
    {
        user: "escrituras",
        pwd: "fatmxbjora",
        roles: ["escritura"]
    }
);
db.createUser (
    {
        user: "actualizaciones",
        pwd: "hqvkwqehwa",
        roles: ["actualizacion"]
    }
);
    