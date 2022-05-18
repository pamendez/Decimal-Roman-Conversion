# Answers to Questionnarie
The following are the answers to the questionnaire present in a homework of the laboratory component of the subject known as "Application Development Tendencies" (INS364L).

The answers are in spanish instead of english:

________

1. ¿Qué es un Coding Dojo?
Un coding dojo, o dojo de codificación, es una reunión en un sitio determinado donde un conjunto de programadores y desarrolladores se juntan para poder trabajar en resolver un reto de programación. Generalmente, este tipo de eventos tiene el propósito de ser divertido y permitir la mejora de las habilidades de programación de dichas personas a través de la practica deliberada y continua.
Referencia utilizada: https://lorenzosolano.com/what-is-coding-dojo/.
 
2. Diferencia entre Requerimientos, Criterios de Aceptación y Escenarios de Prueba. Dar ejemplos a partir de un problema distinto a la referencia.
Los requerimientos representan una propiedad que debe exhibir el software para resolver un problema de la vida real basado en una necesidad que debe resolverse; Los criterios de aceptación son enunciados que indican como se puede validar si una funcionalidad de un software satisface un requerimiento previamente establecido; Y los escenarios de prueba son ejemplos concretos y claro que ponen a prueba un único criterio de aceptación y, a su vez, un requerimiento asociado a dicho criterio de aceptación.
Referencia utilizada: https://lorenzosolano.com/requirements-acceptance-criteria-and/.
 
A partir de estos conceptos, supongamos que un centro de salud nos pide un programa que, dada una fila de personas, este las ordene por turnos y nivel de prioridad. Basado en esta problemática, tenemos los siguientes ejemplos:
1. Requerimientos:
* **Req-1:** El sistema deberá ordenar por turnos todas las personas que llegan y se colocan en la fila.
* **Req-2:** El sistema deberá ordenar internamente la fila por orden de prioridad a partir de su turno asignado.
 
2. Criterios de aceptación:
* **Crit-1-1:** El sistema deberá validar los turnos a partir del orden de llegada de las personas.
* **Crit-1-2:** El sistema deberá mantener el orden de los turnos independientemente de la cantidad de personas que se agreguen a la fila.
* **Crit-1-3:** El sistema deberá eliminar el turno una vez la persona esté siendo atendida.
* **Crit-2-1:** El sistema deberá validar la prioridad de los turnos y ordenarlos basado en el orden de llegada.
 
3. Casos de prueba:
* **Sce-1-1-1:** Se agrega una persona a la lista de turnos cuando no hay turnos que preceden a la persona a agregar.
* **Sce-1-1-2:** Se agrega una persona a la lista de turnos cuando existan turnos que preceden a la persona a agregar.
* **Sce-1-2-1:** Se valida la integridad de los turnos una vez se agrega a una persona a la lista de turnos.
Sce-1-2-2: Se valida la integridad de los turnos una vez se elimina a una persona a la lista de turnos.
Sec-1-3-1: Se valida la eliminación del turno de la persona que se atiende.
* **Sec-2-1-1:** Se valida el ordenamiento por prioridad a partir del orden de llegada se agrega alguien a la lista de turnos dada una prioridad.
* **Sec-2-1-2:** Se valida el ordenamiento por prioridad a partir del orden de llegada se elimina alguien a la lista de turnos dada una prioridad.
 
3. De dos ejemplos de requerimientos no-funcionales, y especifique cuál es su categoría (seguridad, performance, portabilidad, etc.)
Dos ejemplos de requerimientos no funcionales son los siguientes:
El sistema deberá tener colores agradables al usuario. Este requerimiento no funcional es de tipo de interfaz (interface).
El sistema deberá tener un tiempo de respuesta no más de 2 segundos. Este requerimiento no funcional es de tipo de rendimiento (performance).
 
4. ¿Qué es TDD?
El Desarrollo Impulsado por Pruebas, o Test Driven Development (TDD), es un enfoque de desarrollo de software en el que se desarrollan casos de prueba para especificar y validar lo que hará el código. En términos simples, los casos de prueba para cada funcionalidad se crean y prueban primero antes del código y si la prueba falla, entonces se escribe el nuevo código para pasar la prueba y hacer que el código sea simple y libre de errores. Los siguientes pasos definen cómo realizar un desarrollo estilo TDD:

1. Agregue una prueba.
2. Ejecuta todas las pruebas y ve si se produce un error en alguna prueba nueva.
3. Escribe algo de código.
4. Ejecute pruebas y refactorizar el código.
5. Repita todos los pasos hasta que sea necesario.
Referencia utilizada: https://www.guru99.com/test-driven-development.html.
 
5. ¿Qué son pruebas unitarias automatizadas?
Las pruebas unitarias automatizadas son un método de software de prueba en el que las unidades o pequeñas secciones del código se comprueban rigurosamente para garantizar que funcionen correctamente. Se puede escribir un programa separado específicamente para probar la unidad automáticamente, utilizando cada pieza razonable de datos que el código pueda encontrar en el uso en el mundo real, aunque muchos lenguajes de programación tienen un marco para pruebas unitarias automatizadas más fáciles. El objetivo de las pruebas unitarias automatizadas es demostrar que cada parte de un proyecto de desarrollo de software más grande funciona según lo previsto.
Referencia utilizada: https://www.computerhope.com/jargon/a/automated-unit-testing.htm.
 
6. ¿Cuál fue el 1er framework de pruebas unitarias y para cual lenguaje fue creado?
El primer framework de pruebas unitarias fue SUnit, desarrollado para el lenguaje de programación Smalltalk.
Referencias utilizadas: https://en.wikipedia.org/wiki/SUnit; http://sunit.sourceforge.net/.
 
7. Describa los componentes de la arquitectura xUnit.
Todos los marcos de xUnit comparten la siguiente arquitectura de componentes básicos, con algunos detalles de implementación variados. Estos son los siguientes:
 
Corredor de pruebas (Test runner).
Caso de prueba (Test case).
Accesorios de prueba (Test fixtures).
Suite de pruebas (Test suites).
Ejecución de pruebas (Test execution).
Formateador de resultados de la prueba (Test result formatter).
Afirmaciones (Assertions).

Referencia utilizada: https://quick-adviser.com/what-are-the-components-of-an-xunit-test-framework/.
 
8. Indique al menos tres desventajas de las pruebas unitarias automatizadas.
- Con las pruebas unitarias automatizadas, debe aumentar la cantidad de código que debe escribirse. Por lo general, tiene que escribir una o más pruebas unitarias dependiendo de cuán complejas sean las cosas.
- Si bien el código de prueba debe ser bastante simple, este método de prueba sigue siendo más trabajo y más código, lo que significa más horas y más costo.
- Las pruebas unitarias automatizadas son problemáticas cuando se necesita probar la interfaz de usuario (UI). Son buenos para cuando necesita probar la implementación de la lógica empresarial, pero no son excelentes para la interfaz de usuario.
- Las pruebas unitarias automatizadas no pueden ni detectarán todos los errores en un programa, pues existen muchos factores para que ocurra un error a nivel unitario como a nivel completo.
Referencia utilizada: https://theqalead.com/topics/unit-testing/.
 
9. Indique al menos tres ventajas de las pruebas unitarias automatizadas.
- Las pruebas unitarias hacen que sea más seguro y fácil refactorizar el código al implementar pruebas que aseguran que la refactorización ocurra sin problemas ni interrupciones. Elimina el riesgo de cambiar el código fuente más antiguo.
- Hacer pruebas unitarias automatizadas es esencialmente asegurar la garantía de calidad del código., pues muestra problemas y errores antes de que el producto tenga una prueba de integración.
- Las pruebas unitarias automatizadas ayudan a encontrar problemas y resolverlos antes de realizar más pruebas para que no afecten a otros bits de código. Esto incluye errores en la ejecución de un programador y problemas con una especificación para la unidad en sí.
- Las pruebas unitarias automatizadas permiten la refactorización del código y simplifican la integración. Encuentra cambios y ayuda a mantener y ajustar el código, reduciendo errores y defectos, y verificando la precisión de cada unidad.
Referencia utilizada: https://theqalead.com/topics/unit-testing/.
 
10. Tomando el algoritmo de conversión de números arábigos o "decimales" a números Romanos:
Cree un documento donde se listen los Requerimientos, Criterios de Aceptación y Casos de Prueba para una aplicación de consola.
Los casos de prueba deben ser de dos categorías: End-To-End (desde el UI) y Unitarios (caja blanca, código, bajo nivel)

El documento se puede visualizar en el siguiente enlace: https://github.com/pamendez/Decimal-Roman-Conversion/blob/main/docs/Documentation.md.
 
11. Utilizando el lenguaje de su preferencia cree cinco o más casos de prueba unitarios automatizados utilizando un framework de automatización de pruebas para el algoritmo en cuestión.
Las pruebas unitarias pueden ser vistas mediante el siguiente enlace: https://github.com/pamendez/Decimal-Roman-Conversion/blob/main/test_convert.py. El framework de pruebas unitarias utilizado es Pytest para Python.
