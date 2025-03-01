# Import sistema
import os # per leggere variabili di ambiente
import time

# Import internals
from utils.index import *
from utils2.index2 import funzione1, funzione2

# Import externals
from loguru import logger # per stampa log

## Routine main
def main():    
    # info presenti nello script di avvio (visibili solo in windows con il "set" all'interno dello script di npm)
    #logger.info(`pnpm run script -> ENV: ${process.env.ENV}`)
    #logger.info(`pnpm run script -> ENV2: ${process.env.ENV2}`)

    # Variabili comuni nella config del package.json
    #logger.info(`pnpm config -> VAR_A: ${process.env.npm_package_config_VAR_A}`);

    # Variabili presenti nel file .env
    logger.info(f'file env -> FILE_ENV_1: {os.getenv('FILE_ENV_1')}')
    
    # Variabili da modulo interno
    logger.info(f'funzione da modulo: {getDateString()}')
    logger.info(f'funzioni da modulo: {funzione1()}, {funzione2()}')
    
    # Variabili presenti nel Dockerfile
    logger.info(f'docker env -> ENV_DOCKER: {os.getenv('ENV_DOCKER')}')
    logger.info(f'docker env -> TZ: {os.getenv('ENV_DOCKER')}')
    
    # time.sleep(30) # per test con container
    
main()
