# Tarea #4

## Problema 

Paulina tiene una cafetería en una zona costera del norte de españa, donde sirve principalmente comidas.
En su experiencia, entran más clientes en su negocio si sirve comidas frescas los días que hace calor y comidas calientes los días que hace frío, pero el tiempo en la zona es bastante impredecible.
Para intentar mejorar sus beneficios, ha decidido registrar los valores de temperaturas de la última semana y calcular tendencia para decidir si, al día siguiente, servirá comidas frías o calientes.

Por suerte o por desgracia, Paulina no es experta en programación así que te ha contratado a ti para que desarrolles un software que le diga cuál es la tendencia cada día.
El programa calculará la tendencia como la resta entre la temperatura del último día y la del día anterior, es decir, tendencia = temperaturaAyer - temperaturaAnteayer.
Si el resultado es positivo, o dicho de otra forma mayor que cero, la tendencia será al alza. Por otro lado, si el resultado es negativo, es decir, menor que cero, la tendencia será a la baja.
En consecuencia, si la tendencia es positiva cocinará comidas frescas y si la tendencia es negativa comidas calientes.

Los datos que ha recogido son:
Semana 1: lunes: 19ºC, martes: 21ºC, miércoles: 20ºC, jueves: 23ºC, viernes: 25ºC, sábado: 27ºC, domingo: 29ºC
Semana 2: lunes: 31ºC, martes: 30ºC, miércoles: 30ºC, jueves: 33ºC, viernes: 32ºC, sábado: 30ºC, domingo: 27ºC
Semana 3: lunes: 23ºC, martes: 24ºC, miércoles: 22ºC, jueves: 19ºC, viernes: 18ºC, sábado: 22ºC, domingo: 22ºC

Tus tareas para este proyecto son:
Crear una función que permita calcular la tendencia dadas dos temperaturas, y devuelva si la tendencia es positiva o negativa
Crear un programa que recorra las semanas y calcule la tendencia para cada uno de los días donde sea posible
Crear un programa que calcule, con todos los datos, que porcentaje de aciertos tiene el programa, entendiendo como acierto que si la tendencia es al alza la temperatura suba y si la tendencia es la baja la temperatura descienda
Bonus: crea una interfaz que muestre una tabla con los días para cada semana, las temperaturas, y un color que indique el resultado de la tendencia para cada día donde sea posible calcularla.