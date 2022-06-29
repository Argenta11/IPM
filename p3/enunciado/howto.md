---
layout: generic
title: ¿ Cómo realizar la práctica ?
banner:
  src: "/img/pexels-startup-stock-photos-7376.jpg"
  copy_url: "https://www.pexels.com/es-es/foto/programar-empresa-emergente-lista-de-pendientes-concepto-7376/"
  copy: "Startup Stock Photos"
---

## Objetivo

En esta práctica tienes que desarrollar una aplicación web, aplicando
los conocimientos adquiridos sobre el desarrollo de interfaces
gráficas de usuaria.


## Metodología

La práctica se compone de una serie de tareas que tendrás que realizar
en la secuencia indicada.

Aunque la práctica está dividida en una secuencia de tareas, no hemos
entrado en una máquina del tiempo para viajar a la prehistoria de la
informática y usar una metodología _waterfall_. Durante la realización
de cada una de las tareas es más que probable que tengamos que
actualizar, corregir y/o mejorar algunos de los artefactos
desarrollados en tareas previas.


## Control de versiones

Usaremos un [control de
versiones](https://en.wikipedia.org/wiki/Version_control) durante todo
el desarrollo de la práctica.

Esto quiere decir que, en nuestro directorio de trabajo, de ninguna
manera puede haber distintos ficheros con distintas versiones del
mismo elemento.


## Repositorio

Si estas leyendo esta documentación debería ser porque has creado el
_assignment_ correspondiente en _github classroom_ y por tanto ya
tienes el repositorio necesario para realizar la práctica. Si no es
así, ve al campus virtual y, en la asignatura, sigue el enlace
correspondiente.


## Planificación

A _grosso modo_ la práctica consta de cuatro tareas y tiene estimada
una duración de cuatro semanas. Por tanto la primera aproximación es
de una tarea por semana.

Como parte de los aspectos que se valoran en la realización de la
práctica se encuentra la capacidad para ajustarse a los plazos
establecidos.


Las tareas en que se estructura la práctica son las siguientes:

  * Diseño mobile-first de la interface
  * Implementación del contenido y funcionalidad (html5 + js)
  * Implementación del diseño _responsive_ (css3)
  * Accessibilidad (W3C WAI)
  
  
## Autoevaluación

Cada tarea incluye un apartado con una tabla de guía para la
autoevaluación del trabajo que has realizado. Utiliza esas tablas para
detectar las carencias y fortalezas de tu trabajo.

Estas tablas no son excluyentes. Cada tarea puede incluir aspectos de
las tareas anteriores. Por ejemplo, en la tarea 3 podrías encontrar
carencias a corregir sobre el diseño de la tarea 1. Utiliza las tablas de las tareas
anteriores para autoevaluar dichos aspectos.


## Descripción de la aplicación

La aplicación que tienes que desarrollar forma parte de un sistema de
control de accesos covid-19. El sistema consta de los siguientes
contenedores:

  - Una B.D. donde se almacena información de las instalaciones,
    entidades, miembros de las entidades, fechas de acceso a las
    instalaciones, etc.
  
  - Un servidor que proporciona acceso a la B.D. mediante un api tipo
    REST.
  
  - Una aplicación web que permite a las usuarias del sistema las
    operaciones habituales de alta en el sistema, consulta y
    modificación de información personal, etc.
  
  - Una aplicación móbil que permite el registro de los accesos a las
    instalaciones mediante códigos QR.
  
  - La aplicación de escritorio que desarrollate en una práctica anterior.

 
### Usuaria objetivo
    
	Usuaria: Persona que hace uso de las instalaciones.
	
    Las personas que hacen uso de la instalación durante distintos tipos
    de eventos: entrenamientos, conciertos, congresos, ... y que, previamente,
	se registran en el sistema.


### Requisitos no funcionales

	Plataforma de ejecución: web
	
    Lenguajes: html5, css3, javascript
	
	Librerías, frameworks, ...: ninguno
	

### Requisitos funcionales

La aplicación incluye los siguientes casos de uso:

	Dar de alta una persona
		Proporciona el formulario habitual para registrar los datos de
		una nueva usuaria del sistema

Los datos a introducir serán el _login_, _password_, nombre,
apellidos, dni


	Consultar la información personal
                Permite a una usuaria del sistema consultar los datos de su perfil:
         	nombre, apellidos, ..., su código QR y una lista de sus accessos
                más relevantes. 

Una usuaria registrada puede consultar en cualquier momento la
información descrita. A la hora de definir la lista de accessos a mostrar, puedes
guiarte por la disponibilidad de funciones del api de la B.D. También debes limitar
el número de items mostrados de manera que no sea necesario el uso de páginación.

Recuerda que los códigos QR están asociados a una persona e incluyen la siguiente
información: nombre, apellidos, uuid de su entrada en la BD.

    La información incluida en el QR es común para todos los componentes del sistema.
	Es un string con el siguiente formato: "{nombre},{apellidos},{uuid}"
	

<a href="{{page.url|baseUrl}}tarea_1" class="paper-btn">Siguiente: Tarea 1</a>
