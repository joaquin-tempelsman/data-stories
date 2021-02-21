# *Data Stories* - 
-------------------------------------
Repositorio de Joaquin Tempelsman.
Located: CABA, Buenos Aires, Argentina. 

## Transaction forcast - digital channels (mobile and web) made with Facebook Prophet.
[*Proyecto*](https://github.com/joaquin-tempelsman/data-stories/tree/master/transaction%20forecasting%20-%20prophet)

Desarrollo para cliente, actualmente en producción. La exploración, preprocesamiento, entrenamiento, validación y tuneo del modelo pueden encontrarse en la [notebook](https://github.com/joaquin-tempelsman/data-stories/blob/master/transaction%20forecasting%20-%20prophet/prophet_manual_tunning.ipynb) prophet_manual_tunning.ipynb donde se relizaron las pruebas.

En [production](https://github.com/joaquin-tempelsman/data-stories/tree/master/transaction%20forecasting%20-%20prophet/production), se encuentran las versiones de código en formato productivo, con logs, modulos de monitoreo y documentación formal generada para presentar el proyecto.

<u>Módulo de scoring<u>: Con cada run, se prueban los 3 modelos por canal (6 en total) en un rolling cross validation. Los resultados se ponderan con un sistema de scoring basado en tres métricas. SLA_OVER_COUNT (no exceder el dato real por debajo del 10%) , mediana del error porcentual y SLA_COUNT (no exceder el dato real por arriba o por debajo del 10%). 

En base al scoring, el modelo ganador es el que realiza la predicción de ese canal para ese período. Se guarda como ganador, hasta el próximo run. (si omitimos el scoring, se toma el último ganador directamente).

<u>Módulo de monitoreo<u>: Se implementa un módulo de monitoreo que genera métricas en base a todas las predicciones pasadas (incremental). Reporta métricas agrupadas por mes junto con un [plot](https://github.com/joaquin-tempelsman/data-stories/blob/master/transaction%20forecasting%20-%20prophet/cross_validation%20performance_report.png) que evalúa el desempeño del modelo en train para evaluar visualmente la performance del fiteo de las curvas. También se realiza un plot para evaluar el peso de los regresores, sumando explicatividad al modelo.

<u>Documentación<u>: autogenerada con sphinx, anexamos al modelo la documentación formal de todas las funciones y modulos utilizados con normativa usada por numpy.
[link](https://github.com/joaquin-tempelsman/data-stories/tree/master/transaction%20forecasting%20-%20prophet/production/docs/build)

<img src="https://github.com/joaquin-tempelsman/data-stories/blob/master/assets/trx_docs_sample.png" height="800">

## Whatsapp group analyzer - Analytics & Wordcloud
[*Proyecto*](https://github.com/joaquin-tempelsman/data-stories/tree/master/Whatsapp%20group%20-%20analytics)

Este proyecto toma el historial de chat exportable desde la aplicación, contruye un DataFrame y propone
los siguientes informes>

Informe:

Graphs (Seaborn/Bokeh)
- Serie de tiempo - mensajes por día.
- Actividad por hora por año. Permite ver como funciona la actividad del grupo en función de la hora del día, segmentado por año. (output en notebook)
- Participación de cada usuario, por año. (output file stacked.html)
- Participación de cada usuario general. (output file pie.html)

Tablas
- Sample de chats con el día más activo. En un caso fue 24 de nov de 2018 (12 veces el promedio diario del grupo), final cancelada de la copa libertadores Boca-River. 
- Top 5 días más activos, promedio diario de mensajes.
- Miembros del grupo que más mensajes multimedia envìaron.

Wordcloud

Procedimiento
- Se procesan los mensajes de texto en el siguiente orden para poder hacer un análisis de palabras y luego el WC
- Se remueven los emojis > tokenizamos mensajes > llevamos todo a minúsculas / quitamos stopwords / quitamos caracteres de puntuacion / dropeamos mensajes vacios

Obtenemos
- Lista de palabras más usadas y cantidad de apariciones en la historia del grupo
- Producimos la nube de palabras (output en notebook).


nota: La base de chats no esta publicada por cuestiones de privacidad - los miembros saben de su colaboración al proyecto.


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
