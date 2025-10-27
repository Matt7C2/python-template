# Import sistema
import os # per leggere variabili di ambiente
import time

# Import internals
from utils.index import *
from utils2.index2 import funzione1, funzione2

# Import externals
from loguru import logger # per stampa log
from dotenv import load_dotenv

## Routine main
def main():    
    load_dotenv()
    
    # Variabili presenti nel file .env
    logger.info(f'file env -> FILE_ENV_1: {os.getenv('FILE_ENV_1')}')
    
    # Variabili da modulo interno
    logger.info(f'funzione da modulo: {getDateString()}')
    logger.info(f'funzioni da modulo: {funzione1()}, {funzione2()}')
    
    # Variabili presenti nel Dockerfile
    logger.info(f'docker env -> ENV_DOCKER: {os.getenv('ENV_DOCKER')}')
    logger.info(f'docker env -> TZ: {os.getenv('TZ')}')

    time.sleep(1) # secondi: per test file con container

    logger.info('Fine')

    # (opzionale) Termina il programma senza errori
    #exit(0)
    
main()
