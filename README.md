# TP2 - Programacion Dinamica

## Como correrlo

python3 tp2.py archivo.txt

Por ejemplo:

python3 tp2.py datos/ejemplo_4.txt

## El problema

Hay una fila de monedas. Sophia y Mateo juegan por turnos y en cada turno
sacan la primera o la ultima moneda de la fila. Siempre empieza Sophia.

Mateo juega siempre igual: agarra la moneda mas grande entre la primera y
la ultima. Sophia puede elegir lo que quiera.

## Objetivo

Que Sophia junte la mayor cantidad de plata posible. No siempre le va a
poder ganar a Mateo, pero queremos que saque lo maximo que se pueda.

## Idea

Como ya sabemos lo que va a hacer Mateo, la unica que decide es Sophia.
Cada vez que juegan los dos queda una fila mas corta, asi que se pueden
resolver primero las filas chicas, guardar los resultados en una tabla
y usarlos para las filas mas grandes.

Para cada fila Sophia prueba sacar la moneda de la izquierda o la de la
derecha, despues Mateo saca la mas grande, y nos quedamos con la opcion
que le deja mas a Sophia.

Si las dos puntas valen lo mismo, tomamos que Mateo saca la de la izquierda.

La complejidad deberia ser n al cuadrado, porque hay que llenar una tabla
de n por n.

## Cosas para hacer

- Pasar el codigo a tp2.py y mostrar las jugadas y el total de cada uno
- Demostrar que la solucion da el maximo
- Revisar el formato de los archivos de ejemplo
- Medir tiempos con distintos tamanios de fila
- Comparar con el TP1
- Escribir las conclusiones