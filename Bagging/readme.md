### Arboles de clasificación y regresión simples vs bagging (ensambles)
En este lab vamos a comparar el rendimiento de un caso de árbol de clasificación y otro de regresión con el rendimiento de cada versión implementando bagging.

El método de bagging busca generar un conjunto de modelos que en promedio predigan mejor, utilizando técnicas de resampling (bootstrapping) sobre el set de muestras de entrenamiento.

En el caso de la regresión, tendremos un promedio de los outputs de todos los modelos. En el caso de la clasificación, el voto de la mayoría determinará el resultado binario en este caso.

La ventaja es la reducción de la varianza o overfitting y corrigen así este problema que tienen los árboles en general logrando una combinación exitosa.

Usaremos dos datasets:

Clasificación, utilizaremos el dataset cancer de mama de sklearn.

Regresión, utilizaremos el dataset diabetes también de sklearn.
