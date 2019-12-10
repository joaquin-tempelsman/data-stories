# *Data Stories* - 
-------------------------------------
Repositorio de Joaquin Tempelsman.
Located: CABA, Buenos Aires, Argentina. 

## Web Scrapping y Natural Language processing  @GuiaOleo.com.ar -
[*Proyecto*](https://github.com/JoaquinTemp87/data-stories/tree/master/Web%20Scapping%20-%20GuiaOleo)

Este proyecto, busca procesar las reviews cargadas en la reconocida web Guia Oleo tomando la información de todas las reviews para luego de segmentarlas aplicar distintas formas de topic modeling. La idea es encontrar temas o tópicos ocultos en las reviews, hallar patrones y insights.

El proyecto consta de cuatro etapas:
- Scrapping del sitio guiaoleo.com.ar
- Parsear los htmls y ordenar la información útil en un dataframe
- Normalizar el texto en las reviews, quitando caracteres de puntuación, stopwords y tokenizar.
- Modeling y visualizaciones. Bag Of Words, LDA, LSA y NMF.

Proyecto realizado en conjunto con Johanna Barrera. 

## Arboles de clasificación y regresión simples vs bagging (ensambles)
[*Proyecto*](https://github.com/joaquin-tempelsman/data-stories/tree/master/Bagging)

En este lab vamos a comparar el rendimiento de un caso de árbol de clasificación y otro de regresión con el rendimiento de cada versión implementando bagging.

El método de bagging busca generar un conjunto de modelos que en promedio predigan mejor, utilizando técnicas de resampling (bootstrapping) sobre el set de muestras de entrenamiento.

En el caso de la regresión, tendremos un promedio de los outputs de todos los modelos. En el caso de la clasificación, el voto de la mayoría determinará el resultado binario en este caso.

La ventaja es la reducción de la varianza o overfitting y corrigen así este problema que tienen los árboles en general logrando una combinación exitosa.

Usaremos dos datasets:

Clasificación, utilizaremos el dataset cancer de mama de sklearn.

Regresión, utilizaremos el dataset diabetes también de sklearn.

## Arboles de clasificación vs Gridsearch
[*Proyecto*](https://github.com/joaquin-tempelsman/data-stories/tree/master/Clasificacion)

En este LAB vamos a modelar un arbol de clasificación y una versión aumentada con Gridsearch usando las librerías de scikit-learn para poder predecir la probabilidad de un atáque cardíaco. Usaremos el conocido dataset Heart.csv para entrenar el modelo con 303 pacientes.

## Predicción de ventas - desafio Kaggle (in progress)
[*Proyecto*](https://github.com/joaquin-tempelsman/data-stories/tree/master/Predict%20Sales%20-%20Kaggle)

Pasos a realizar:
-Análisis exploratorio de los distintos dataset (completado)
-Armado del dataset principal (completado)
-Modelo de predicción (pending)
-Conclusiones (pending)
