# Plataforma de administración de Verum
## Introducción

El presente desarrollo se realiza con miras a crear un entorno integral que ayude a automatizar el flujo de trabajo de la empresa Verum, ello mediante el la creación de una web-app que resuelva las necesidades plnteadas por los requerimientos de la empresa establecidos en las etapas del proyecto. Este documento funciona tanto como descripción como guia de uso o actualización.

## Etapas
Este proyecto se desenvuelve en 2 etapas de requerimientos:

- Una plataforma de identificación de representantes de la empresa a la hora de presentarse en algun punto, ello mostrando un documento acompañado de un código QR que acredite la procedencia redirigiendo hacia una visualización web profesional con los datos del representante.

- Una plataforma que permita la consulta de los reportes de clientes y avise al administrador de dichas consultas o descargas por via mail.

## Propuesta de solución
La propuesta para solucionar estos requerimientos, es crear una web-app (que puede ser consultada en cualuier navegador de internet, ya sea en dispositivos de escritorio o moviles como celulares y tabletas) que incorpore una plataforma integral de administración, ello con el objetivo de escalarla a mas requerimientos o propuestas; dicha plataforma estaría compuesta de:
- Una base de datos que almacene todo lo relacionado con la empresa
  - En el caso de la autenticación de personal almacenaría sus datos (nombre, plaza, codigo QR, etc.); Esta tambien contendría los datos de quien tiene permisos administrativos, en este caso, el director de Verum.
  - En el caso de los reportes de clientes, almacenaría sus datos de acceso, los reportes a consultar, etc.

- Una API de acceso de datos.
  - Regula el acceso de datos mediante peticiones HTTP  de consulta, escritura y actualización; el borrado no se haría desde la API, eso solo se haría desde el usuario administrador de datos.

- Una interfaz de usuario para estar en interacción con los datos de forma visual.

## Tecnologías utilizadas
Cada uno de los tres componentes (base de datos, API e interfaz gráfica) serán programados uno a uno de forma modular e independiente, esto con el objetivo de que la arquitectura no sea una limitante, es decir, todo se puede montar en el mismo servidor o servidores independientes, de acuerdo a lo que se defina en el futuro. Para ello se emplean contenedores de docker, personalizados y ejecutados desde un bash de linux.

### Base de datos
Se trata de un contenedor de docker que emplea MongoDB como motor de base de datos; en el proceso de construcción se copia adentro del contenedor un archivo JavaScript que define la base de datos y agrega una colección de preprsentantes, agregando por default al director de Verum como único administrador

### API (Application programming interface) 
Se trata de un intermediario entre la interfaz visual y la base de datos; define rutas especificas para la consulta, inserción y actualización de datos.Se elige el framework de Flask para alimentarla.

#### Rutas - Endpoints
```
./get_usuario_by_id/<id_del_representante>
```

IMPORTANTE, NECESARIA PARA LA IDENTIFICACIÓN POR QR
La redirección QR esta pensada para mandar a una pagina con el siguiente formato
##### verum.com/?usuario=<id_del_usuario>

Dicho parametro se extrae de la URL, se para como argumento para la api y regresa todos los datos del representante

---
```
./post_representante/
?nombre:<Nombre del usuario>&
seg_nombre:<Segundo nombre del usuario>&
a_paterno:<Apellido paterno del usuario>&
a_materno:<Apellido materno del usuario>&
ciudad:<Localización geografica del usuario>&
user_type:<privilegios del usuario>&
contrasenia:<contraseña del usuario>
```


Parametro de la API para dar de alta usuarios. 

Al dar de alta un usuario, por defecto, los valores en la base de datos de la fecha de modificación se establece automaticamente y se establece como usuario activo.

---
```
./update_representante_by_id/<id del usuario>/
?nombre:<Nombre del usuario>&
seg_nombre:<Segundo nombre del usuario>&
a_paterno:<Apellido paterno del usuario>&
a_materno:<Apellido materno del usuario>&
ciudad:<Localización geografica del usuario>&
user_type:<privilegios del usuario>&
contrasenia:<contraseña del usuario>&
activo:<status booleano del usuario>
```


Parametro de la API para actualizar usuarios. 

Es un patch para actualizar los parametros de forma unitaria y opcional

---
```
./login/?
nombre:<Nombre del usuario>&
contra:<Contraseña hasheada de usuario>
```


Devuelve en caso de ser correcto
```
{
	inicio_sesion: True
}
```

Devuelve en caso de ser incorrecto
```
{
	inicio_sesion: False
}
```

---
Nota: No existe el método para borrar, eso debe hacerlo el administrador de la base de datos, para evitar posibles ataques o errores que comprometan la integridad de los datos.

---
### Interfaz de usuario 

La interfaz visual representa la manipulación y visualización de datos, es enteramente gestionada por el consumo de la API; existe una vista por cada evento posible en la manipulación de la base de datos. Se elige el framework de Vue para consumir la api y mostrar las vistas

#### Rutas 

El mapa de navegación se define en una listración a continuación, mientras se listan las visualizaciones generales y los eventos dentro de cada vista

```
/login
	- Formulario de espera de datos
	- Datos incorrectos
```

```
/?usuario=<id_del_usuario>
	- Representante existe
	- Rpresentante no existe
```

```
/panel_administracion
	- Usuario tiene permiso de acceso 
		- Editar usuarios
	- Usuario no tiene permiso de acceso
```











































































