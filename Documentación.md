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
Se trata de un intermediario entre la interfaz visual y la base de datos; define rutas especificas para la consulta, inserción y actualización de datos.
#### Rutas - Endpoints
- ./get_representante_by_id/<id_del_representante>

IMPORTANTE, NECESARIA PARA LA IDENTIFICACIÓN POR QR
La redirección QR esta pensada para mandar a una pagina con el siguiente formato
##### verum.com/?representante=<id_del_representante>

Dicho parametro se extrae de la URL, se para como argumento para la api y regresa todos los datos del representante
