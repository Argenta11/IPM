---
layout: generic
title: "Tarea 2: Implementar contenido y funcionalidad"
banner:
  src: "/img/pexels-pixabay-270557.jpg"
  copy_url: "https://www.pexels.com/es-es/foto/monitor-que-muestra-texto-de-error-270557/"
  copy: "Pixabay"
---

En esta tarea tienes que realizar una parte importante de la
implementación de la aplicación.

> Recuerda: El desarrollo software es un proceso iterativo. Es normal
> que durante la realización de esta tarea decidas añadir, eliminar o
> modificar partes del diseño de la interface. Si es el caso, no te
> olvides de actualizar los ficheros correspondendientes.

Para esta tarea implementarás:

  - Estructura y contenido de la interface. Es decir los documentos
    html que conforman la vista de la aplicación.
	
  - Funcionalidad: el código javascript correspondiente a la parte
    del cliente, es decir, el navegador.
	
No incluyas ningún elemento de estilo (css). Tampoco puedes usar
ninguna librería, framework, ...

## Requisitos

Tienes que cumplir los requisitos indicados en los apartados y tareas
anteriores, y además:

  - No usar ningún librería, framework, ...
  
  - Los documentos html cumplen el estándar html5. El validador del
    W3C no detecta ningún error.
	
  - El código javascript se ajusta al estándar y las características
    están implementadas en, al menos, tres navegadores en su última
    versión oficial. En caso de duda, se toma como referencia la
    información ofrecida por [caniuse.com](https://caniuse.com/)


## Autoevaluación

Para realizar una autoevaluación de esta tarea, puedes guiarte por las
tablas de las tareas anteriores y la siguiente tabla:


| Criterios | Nivel ||
|-----------| ----- |-|
|           |  Bueno | Inadecuado |
| Cumple los requisitos de la lista proporcionada | Cumple todos los requisitos | No cumple algún requisito |
| La implementación sigue el diseño de la interface | La interface de la aplicación implementada coincide con el diseño de la interface  | Existen discrepancias entre el diseño de la interface y la implementación |
| La aplicación gestiona los errores | La aplicación captura los errores e informa convenientemente a la usuaria | Los errores provoca mal funcionamiento de la aplicación, son ignorados o no se informa convenientemente a la usuaria |
| La aplicación gestiona los fallos humanos | La UX es optima cuando se introducen errores en los formularios | Los errores en los formularios no se tratan convenientemente |
| La implementación es correcta | Se ejecuta sin fallos en todos los casos | La ejecución falla para algún caso |
| La implementación es estándar | El código html es html5 | El validador informa de errores en el html |
| La implementación es _cross-browser_ | El código javascript funciona en la mayoría de navegadores | Se usan características no implementadas en los navegadores actuales |


## Recursos

La B.D. y el servidor asociado son los mismos que en las prácticas anteriores. No
obstante, como es habitual en la vida del software, desde el comienzo del cuatrimestre
se han liberado versiones nuevas. Por tanto, si no has actualizado a la última versión,
este es el momento de hacer un _pull_ del repositorio para obtener dicha versión. A
continuación, como los contenerdores docker tienen una versión antigua, tendrás que
borrarlos y volver a crearlos con la nueva.

También necesitarás un serivdor web que, como mínimo, sirva los documentos html, css
y el código javascript. Como es habitual en una aplicación web, es muy probable que
el código javascript tenga problemas para acceder a otros servidores (en tu caso, el
servidor de la B.D.). Así que a mayores el servidor web tendrá que responder a las
peticiones del código javascript y consultar la B.D. en su lugar. Teniendo esto en
cuenta, elige el servidor web o framework que consideres oportuno para implementar
la parte de backend de la aplicación.

<a href="{{page.url|baseUrl}}tarea_3" class="paper-btn">Siguiente: Tarea 3</a>
