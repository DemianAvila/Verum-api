//CREA LA BASE DE DATOS DE VERUM
db = db.getSiblingDB("verum_administracion");
//INSERTA UN DATO PARA HACER EXISTIR ESA BASE DE DATOS
db.representantes.insert({
    nombre: "Luis Wenceslao De Ignacio Hernández",
    ciudad: "Ecatepec, Estado de México",
    activo: true,
    user_type: 1,
    fecha_modificacion: null,
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
          resource: { db: "verum_administracion",
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
          resource: { db: "verum_administracion",
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
          resource: { db: "verum_administracion",
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
        pwd: "d2UsuPRILO4n7KasPrAagESILYLZhP0J8WzWi46kUbg=",
        roles: ["lectura"] 
    }
);
db.createUser (
    {
        user: "escrituras",
        pwd: "n2yYhKlvVrk4qNkvDn0MOBR1VZ8EoTzSfKrp0JlNzV0=",
        roles: ["escritura"]
    }
);
db.createUser (
    {
        user: "actualizaciones",
        pwd: "tyyKhzHcff2zQwUuM+i+mS0OVvnRbXB7cO6oa4byKEA=",
        roles: ["actualizacion"]
    }
);
