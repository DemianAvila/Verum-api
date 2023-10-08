//CREA LA BASE DE DATOS DE VERUM
db = db.getSiblingDB("verum_administration");

//CREAR COLECCION DE CORREOS

db.mails.insert({
    _id: "0",
    mail: "luisvenzel@gmail.com",
    active: true,
    user_owner: 1,
    entrprice_owner: 1
});
db.mails.insert({
    _id: "1",
    mail: "direcciongeneral@verumexico.com",
    active: true,
    user_owner: 1,
    entrprice_owner: 1
});

//INSERTA UN DATO PARA HACER EXISTIR ESA BASE DE DATOS
db.users.insert({
    _id: 1,
    name: "Luis",
    middle_name: "Wenceslao",
    f_last_name: "De Ignacio",
    s_last_name: "Hernández",
    city: "Ecatepec, Estado de México",
    active: true,
    user_type: 1,
    update_date: Date(),
    creation_date: Date(),
    mails: ["0", "1"],
    pass: null,
    sha_code:null,
    enterprice: 1,
    user_owner: 1,
    entrprice_owner: 1,
});

db.enterprices.insert({
  _id: 1,
  name: "Verum",
  user_owner: 1,
  entrprice_owner: 1
});

db.user_types.insertMany([
  {
    _id: 1,
    user_type: "admin_direction",
    active: true
  },
  {
    _id: 2,
    user_type: "employee",
    active: true
  },
  {
    _id: 3,
    user_type: "client",
    active: true
  }
]);

db.models.insertMany([
  {
    _id: 1,
    name: "users",
    access_menu: "Users"
  },
  {
    _id: 2,
    name: "user_types"
  },
  {
    _id: 3,
    name: "mails"
  },
  {
    _id: 4,
    name: "enterprices",
    access_menu: "Enterprices"
  },
  {
    _id: 5,
    name: "reports",
    access_menu: "Reports",
    sub_menus: [
      {
        name: "Create report"
      },
      {
        name: "Upload report"
      }
    ]
  },
  {
    _id: 6,
    name: "permissions"
  }
]);


//PERMISOS DE GRUPO SON SOBREESCRITOS POR
//PERMISOS DE USUARIO Y ESTOS SON SOBREESCRITOS POR 
//PERMISOS DE OWNER Y SUS EXEPCIONES
db.permissions.insertMany([
  {
    user_type:1,
    model: 1,
    create: true,
    read: true,
    update: true,
    delete: true
  },
  {
    user_type:1,
    model: 2,
    create: true,
    read: true,
    update: true,
    delete: true
  },
  {
    user_type:1,
    model: 3,
    create: true,
    read: true,
    update: true,
    delete: true
  },
  {
    user_type:1,
    model: 4,
    create: true,
    read: true,
    update: true,
    delete: true
  },
  {
    user_type:1,
    model: 5,
    create: true,
    read: true,
    update: true,
    delete: true
  },
  {
    user_type:1,
    model: 6,
    create: true,
    read: true,
    update: true,
    delete: true
  },
  {
    user_type:2,
    model: 1,
    create: false,
    read: false,
    update: false,
    delete: false
  },
  {
    user_type:2,
    model: 2,
    create: false,
    read: true,
    update: false,
    delete: false
  },
  {
    user_type:2,
    model: 3,
    create: true,
    read: true,
    update: false,
    delete: false
  },
  {
    user_type:2,
    model: 4,
    create: true,
    read: true,
    update: false,
    delete: false
  },
  {
    user_type:2,
    model: 5,
    create: true,
    read: true,
    update: true,
    delete: false
  },
  {
    user_type:2,
    model: 6,
    create: false,
    read: true,
    update: false,
    delete: false
  },
  {
    user_type:3,
    model: 1,
    create: false,
    read: false,
    update: false,
    delete: false
  },
  {
    user_type:3,
    model: 2,
    create: false,
    read: true,
    update: false,
    delete: false
  },
  {
    user_type:3,
    model: 3,
    create: true,
    read: true,
    update: false,
    delete: false
  },
  {
    user_type:3,
    model: 4,
    create: false,
    read: false,
    update: false,
    delete: false
  },
  {
    user_type:3,
    model: 5,
    create: false,
    read: true,
    update: true,
    delete: false
  },
  {
    user_type:3,
    model: 6,
    create: false,
    read: true,
    update: true,
    delete: false
  },
]);

db.multiowner_permissions_exceptions.insertMany([
  {
    user_type:1,
    external_user: true,
    external_enterprice: true
  }
]);