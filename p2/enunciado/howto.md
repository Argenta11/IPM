---
layout: generic
title: ¿ Cómo realizar la práctica ?
banner:
  src: "/img/pexels-christina-morillo-1181622.jpg"
  copy_url: "https://www.pexels.com/es-es/foto/seis-mujeres-de-pie-y-sentadas-dentro-de-la-habitacion-1181622/"
  copy: "Christina Morillo"
---

## Objetivo

En esta práctica tienes que desarrollar una aplicación gráfica para
móviles, aplicando los conocimientos adquiridos sobre el desarrollo
de interfaces gráficas de usuaria.


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

  * Diseño de la interface
  * Diseño sw e implementación del primer caso de uso
  * Diseño sw e implementación del segundo caso de uso
  * Internacionalización
  
  
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
  
  - La aplicación de escritorio que desarrollas en esta práctica.

La aplicación realiza consultas directamente a la B.D. y muestra los
resultados, todo a través de una interface gráfica.
 
 
### Usuaria objetivo
    
	Usuaria: Responsable COVID.
	
	Una de las tareas del responsable COVID es el control del acceso
    a las instalaciones bajo su supervisión. El control incluye anotar
    las personas que hacen uso de la instalación durante distintos tipos
    de eventos: entrenamientos, conciertos, congresos, ... 


### Requisitos no funcionales

	Plataforma de ejecución: android o iOS
	
    Lenguaje de programación: dart
	
	Librería gráfica: flutter
	

### Requisitos funcionales

La aplicación incluye los siguientes casos de uso:

	Anotar la entrada/salida de una persona
		Permite anotar la fecha, hora de entrada, hora de salida y temperatura al entrar
        de una persona. La identificación de la persona se realiza a partir del código QR
        que posee dicha persona.

La identificación de una persona se realiza a partir de su código
QR. Esto quiere decir que la persona usuaria de la instalación dispone
de un código QR en la pantalla de su móvil, impreso, ...  El
responsable COVID (la usuaria de la aplicación) antes de permitir el
acceso a la instalación, escaneará el código QR con la aplicación y
obtendrá los datos de la persona del servidor. A continuación anotará
en la aplicación los datos de la persona usuaria, la fecha y hora de
entrada y la temperatura.

Cuando la persona usuaria abandone la instalación, el responsable
COVID anotará la fecha y hora de salida.


	Gestionar la lista de personas asistentes durante un evento
        Permite consultar la lista de personas que han entrado/salido de la instalación
        durante un evento. El inicio y fin de un evento lo marca la propia usuaria de
        la aplicación.

La usuaria de la aplicación puede consultar en cualquier momento la lista de personas
que están o han hecho uso de la aplicación, y alguna información derivada. En concreto
es muy interesante el número de personas que están en la instalación y el número total
de personas que accedieron a la instalación.


También, como parte de los casos de uso, la aplicación tiene que
gestionar los problemas creados tanto por la usuaria de la aplicación
como por las personas usuarias de la instalación. En concreto:

  - Se olvida de registrar la entrada y/o la salida de una persona.
  
    En este caso hay que ofrecer una alternativa para anotar la entrada/salida
    en una hora concreta, distinta a la actual.

  - La persona usuaria ha olvidado su código QR.
  
    En este caso hay que ofrecer una alternativa para introducir sus
    datos manualmente.


La información registrada durante el uso de la aplicación se debe
enviar al servidor. Dado que se trata de una aplicación para
dispositivos móviles, es necesario que consideres la optimización de
las comunicaciones, i.e. las peticiones al servidor.

Recuerda que los códigos QR están asociados a una persona e incluyen la siguiente
información: nombre, apellidos, uuid de su entrada en la BD.

    La información incluida en el QR es común para todos los componentes del sistema.
	Es un string con el siguiente formato: "{nombre},{apellidos},{uuid}"
	

> N.B.: Esta app organiza el registro de acceso en base a eventos. Es
> la propia usuaria de la app la que marca el inicio y fin de un
> evento. Sin embargo, en la B.D. no se guarda ninguna información de
> los eventos en sí mismos, sólo se guardan los registros de entrada y
> salida.

<a href="{{page.url|baseUrl}}tarea_1" class="paper-btn">Siguiente: Tarea 1</a>
