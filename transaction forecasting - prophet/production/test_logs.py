import logging
import pandas as pd
import typer


fh = logging.FileHandler('example2.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
formatterstr = logging.Formatter('%(asctime)s - %(message)s')
sh.setFormatter(formatterstr)

logger = logging.getLogger('LogdemiApp')
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.addHandler(sh)


df = pd.read_csv('/home/charly/Descargas/datasets-master-a6fa39d2490c3afd5b5eb24b6f250c13fe8b4f5a/Car Evaluation/car.data')
logger.info('Dataset Cargado')
logger.info(f'Columnas del dataset: {df.columns}')
logger.error('Esto es un error')
logger.debug('Esto es para depurar')
logger.debug('Otro Mas')
logger.warn('Esto es un warning')

app = typer.Typer()

@app.command()
def simple_train(x: int):
    logger.info('Comenzando entrenamiento sencillo')
    logger.debug(f'Los datos son: {x}')
    pass

@app.command()
def train_hiperx(x: int):
    logger.warn('reentrenando hiperparametros!')
    pass

if __name__ == '__main__':
    app()


