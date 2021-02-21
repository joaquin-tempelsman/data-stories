"""main.py module description

module that runs transaction prediction using facebook prophet.

inputs:
preprocessed data from rscript module.
hyper parameter and regresors for each model stored in pickle files

extra:
verbosity from prophet fit is silenced.
verbosity from cross validation prophet, is not silenced yet.

"""




#pendientes!
#REVISAR LINEA 37 EN CV y 54

import requests
from datetime import date
import pandas as pd
import sys
import typer
import logging
import operator

sys.path.append('..')
#import mods
import ingesta_prep
import carga_modelo_corto
import carga_modelo_largo
import cv
import scoring
import iter_predict


logger = logging.getLogger('trx_main')
logger.setLevel(logging.NOTSET)


fh = logging.FileHandler('log_trx.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh) ####!

sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
formatterstr = logging.Formatter('%(asctime)s - %(message)s')
sh.setFormatter(formatterstr)

# filter out everything that is above INFO level (WARN, ERROR, ...)
sh.addFilter(lambda record: record.levelno <= logging.INFO)
logger.addHandler(sh)


#FUNCION MAIN QUE CORRE TYPER
def principal(long :bool =  False, cv_off: bool = False, multiproc_off: bool = False):
    """generates prediction (SHORT = Default) outputs saved in /predicciones
    
    parameters
    ----------
    long : str
        changes output to long prediction.

    paralell : str
        cross validation for model selection is done with one core instead of all cores.

    cv-off : str
        cancel cross validation for model selection. Uses best model from previous run.


    Returns
    -------
    csv with prediction to predicciones/entregable/

    csv with prediction and detailed data to predicciones/

    csv with cv summary results, optional

    """
    

    logger.info('running forecast model with settings as:')
    logger.info('long prediction = ' + str(long))
    logger.info('stop cross validation = ' + str(cv_off))
    logger.info('running cv with one procesor only  = ' + str(multiproc_off))

    ruta = '../../data/raw/'
    logger.info('getting data from' + ruta)

    data_prep = pd.read_csv(ruta + 'data_prep.csv') 
    logger.debug('data imported correctly')


    logger.debug('running module: ingesta_prep - short prediction version')
    AB2_data, AB1_data, AB3_data, MB3_data , MB2_data, MB1_data = ingesta_prep.ingesta(data_prep)
    logger.debug('module end')


    datasets_short = [AB1_data, AB2_data, AB3_data, MB1_data, MB2_data, MB3_data]

    logger.info('running module: ingesta_prep - > ingesta (long prediction version)')
    AB2_data_long, AB1_data_long, AB3_data_long, MB3_data_long, MB2_data_long, MB1_data_long = ingesta_prep.ingesta(data_prep, prediccion_corta=False)
    logger.debug('module end')
    datasets_long = [AB1_data_long, AB3_data_long, MB1_data_long, MB2_data_long, MB3_data_long]
    logger.info('data prepared')

    
    #PREPARACION MODELO CORTO
    logger.debug('running module: carga_modelo_corto - > load_regresors_short')
    logger.info('getting hypers and regresors - short model')
    regs_dict_short, hyper_dict_short = carga_modelo_corto.load_regresors_short()
    logger.debug('module end')

    #LISTA DE MODELOS CORTOS A PREDECIR
    logger.debug('running module: carga_modelo_corto -> load_models_short')
    to_predict_dict_short = carga_modelo_corto.load_models_short(regs_dict_short ,hyper_dict_short, datasets_short)
    logger.debug('module end')
    logger.info('short models to predict - ready')




    #PREPARACION MODELO LARGO
    logger.debug('running module: carga_modelo_largo - > load_regresors_long')
    logger.info('getting hypers and regresors - short long')
    regs_long_ab,regs_longs_mb ,hyper_dict_long = carga_modelo_largo.load_regresors_long()
    logger.debug('module end')

    #LISTA DE MODELOS LARGOS A PREDECIR
    logger.debug('running module: carga_modelo_largo -> load_models_long')
    to_predict_dict_long = carga_modelo_largo.load_models_long(regs_long_ab ,regs_longs_mb, hyper_dict_long, datasets_long)
    logger.info('long models to predict - ready')
    logger.debug('module end')

   
    #CROSS VALIDATION ENTRE MODELOS Y SCORING PARA SELECCIONAR EL MEJOR DE CADA CANAL
    if cv_off == False:
        logger.debug('running module: cv -> cv_iteration')
        logger.info('running cross validation for all models, best model will be selected for each channel')

        cv_result = cv.cv_iteration(to_predict_dict_short, to_predict_dict_long, long = long, multiproc_off = multiproc_off)
        logger.debug('module end')

        
        logger.info('loading config.csv - > scoring parameters for model selection')     
        config = pd.read_csv('config.csv') #base de trx 01 enero 20018 a 31 ago 2020
        sla_over_scoring = config[config.variable == 'sla_over_scoring'].score.values
        sla_scoring = config[config.variable == 'sla_scoring'].score.values
        perc_error_median_scoring = config[config.variable == 'perc_error_median_scoring'].score.values
        sla_over_threshold = config[config.variable == 'sla_over_threshold'].score.values
        logger.debug('scoring vars loaded correctly')

        logger.debug('running module: scoring -> get_model_score')
        logger.info('scoring with parameters:')
        logger.info('sla_over score:' + str(sla_over_scoring))
        logger.info('sla_score:' + str(sla_scoring))
        logger.info('perc_error_median score:' + str(perc_error_median_scoring))
        logger.info('sla_over_threshold:' + str(sla_over_threshold))

        logger.debug('running module: scoring -> get_model_score')
        score_ab, score_mb = scoring.get_model_score(results = cv_result, sla_over_scoring = sla_over_scoring, sla_scoring = sla_scoring , perc_error_median_scoring = perc_error_median_scoring, sla_over_threshold = sla_over_threshold, long=long)
        logger.debug('module end')

        logger.debug('getting max score for each channel')
        ab_best_model = max(score_ab.items(), key=operator.itemgetter(1))[0]
        mb_best_model = max(score_mb.items(), key=operator.itemgetter(1))[0]

        logger.info('best_ab_model ->' + str(ab_best_model))
        logger.info('best_mb_model ->' + str(mb_best_model))

        logger.debug('subseting predict dict to winners models only')

        #FILTRO EL DICCIONARIO PARA PREDECIR SOLAMENTE LOS MODELOS GANADORES DEL PASO ANTERIOR
        if long == False:
            #to_predict_dict_short = to_predict_dict_short[ab_best_model,mb_best_model]
            logger.debug('subseting dict - short prediction')
            to_predict_dict_short = {k: to_predict_dict_short[k] for k in [ab_best_model,mb_best_model] if k in to_predict_dict_short}
            

        if long == True:
            #to_predict_dict_long = to_predict_dict_long[ab_best_model,mb_best_model]
            logger.debug('subseting dict - long prediction')
            to_predict_dict_long = {k: to_predict_dict_long[k] for k in [ab_best_model,mb_best_model] if k in to_predict_dict_long}

        print('short models=' + str(to_predict_dict_short.keys()))
        print('long models=' + str(to_predict_dict_long.keys()))

    else:
        #SI NO HAY CV, USAR MODELO OBTENIDO CON CV DE LA VEZ ANTERIOR
        pass

    #FUNCION DE PREDICCION LARGA O CORTA.
    logger.debug('running module: iter_predict -> predict / long prediction =' + str(long))
    iter_predict.predict(to_predict_dict_short, to_predict_dict_long, long = long)
    logger.debug('module end')

    exit()

if __name__ == "__main__":
    
    typer.run(principal)

    logger.info('end')
 