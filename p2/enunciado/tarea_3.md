---
layout: generic
title: "Tarea 3: Diseño sw e implementación del segundo caso de uso"
banner:
  src: "img/pexels-andrew-neel-6633920.jpg"
  copy_url: "https://www.pexels.com/es-es/foto/apple-iphone-escritorio-ordenador-portatil-6633920/"
  copy: "Andrew Neel"
---

En esta tarea tienes que realizar la parte central del desarrollo
software: el diseño software y su implementación.


> Recuerda: El desarrollo software es un proceso iterativo. Es normal
> que durante la realización de esta tarea decidas añadir, eliminar o
> modificar partes del diseño de la interface. Si es el caso, no te
> olvides de actualizar los ficheros correspondendientes.


No olvides que tu diseño software se tiene que basar en el principo de
separar el estado de la vista. Consulta las distintas alternativas
habituales para _flutter_ (_flutter state managment_) y elige la que
consideres más adecuada para tu aplicación.

Al contrario de lo que ocurre con el diseño de la interface, para el
diseño sw sí que existe un estándar establecido: UML. Emplea este
lenguaje para crear los diagramas tanto estáticos como
dinámicos.

Basándote en tu diseño sw, implementa la aplicación. No olvides que
además de los problemas considerados en la descripción del caso de
uso, también tiene que gestionar otros errores. Por ejemplo, teniendo
en cuenta que la aplicación tiene que conectarse con la BD, algunos
errores esperables son:

  - No es posible conectarse con el servidor.
  
  - El servidor no responde.
  
  - El servidor devuelve un mensaje de error.


## Requisitos

Recuerda que el caso de uso a desarrollar es:

	Gestionar la lista de personas asistentes durante un evento
        Permite consultar la lista de personas que han entrado/salido de la instalación
        durante un evento. El inicio y fin de un evento lo marca la propia usuaria de
        la aplicación.

Tal y como se describe en la sección <a
href="{{page.url|baseUrl}}howto" class="button big">Cómo realizar la
práctica</a>

Además de lo indicado en el apartado anterior y en las tareas
anteriores, tienes que cumplir los siguientes requisitos:

  - Los resultados de esta tarea incluyen los diagramas UML y el
    código de la aplicación.
	
  - Los diagramas siguen el estándar UML y se entregan, al menos, en
    formato pdf. Los diagramas pueden estar distribuidos en cualquier
    número de ficheros.
	
  - El diseño de la interface está actualizado.


## Autoevaluación

Para realizar una autoevaluación de esta tarea, puedes guiarte por las
tablas de las tareas anteriores y la siguiente tabla:


| Criterios | Nivel ||
|-----------| ----- |-|
|           |  Bueno | Inadecuado |
| Cumple los requisitos de la lista proporcionada | Cumple todos los requisitos | No cumple algún requisito |
| El diseño sw está bien expresado | Se ajusta al estándar UML y cada artefacto se usa según su significado | No sigue el estándar UML |
| El diseño sw separa estado e interface | Aplica alguna de las opciones de _state managment_ de flutter | Existen dependencias entre el estado y la interface |
| El diseño sw incluye diagramas estáticos y dinámicos | Existen diagramas tanto estáticos (p.e diagrama de clases) como dinámicos (p.e. diagrama de secuencia) | Faltan los diagramas estáticos o los dinámicos |
| El diseño sw es suficiente | El diseño incluye todos los elementos necesarios para realizar la implementación | La implementación incluye elementos que no se corresponden con el diseño sw |
| La implementación sigue el diseño de la interface | La interface de la aplicación implementada coincide con el diseño de la interface  | Existen discrepancias entre el diseño de la interface y la implementación |
| La aplicación gestiona los errores | La aplicación captura los errores e informa convenientemente a la usuaria | Los errores provoca mal funcionamiento de la aplicación, son ignorados o no se informa convenientemente a la usuaria |
| La aplicación gestiona los fallos humanos | La aplicación ofrece alternativas en los casos de error humano descritos | En caso de error humano, no es posible completar el uso de la app |
| La implementación es correcta | Se ejecuta sin fallos en todos los casos | La ejecución falla para algún caso |


> Recuerda que el profesor sólo evaluará los ficheros que están en tu
> repositorio de _github classroom_. Es más seguro que tú también
> autoevalues tu trabajo sobre un _clone_ de ese repositorio.


<a href="{{page.url|baseUrl}}tarea_4" class="paper-btn">Siguiente: Tarea 4</a>
