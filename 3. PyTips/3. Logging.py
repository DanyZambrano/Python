import logging


# Niveles de Registro:
'''
    .notset    > 0  (Imprime todos los registros)
    .debug     > 10
    .info      > 20
    .warning   > 30 (Nivel por defecto)
    .error     > 40
    .critical  > 50
'''


# Formato
# (msg, *args, **kwargs)

logging.getLogger().disabled = False


logging.basicConfig(filename='/Users/danyzambrano/downloads/example.log', 
                    filemode='w', 
                    format='%(asctime)s - %(name)s -  %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p',
                    level=logging.NOTSET)



logging.debug('Mensaje 2')
logging.info('Mensaje 2')
logging.warning('Mensaje 2')
logging.error('Mensaje 2')
logging.critical('Mensaje 2')




def sumatoria(valorA: int, valorB: int, valorC: int) -> int:
    if (valorC >= 30):
        logging.warning('El valorC (%s) esta fuera de los limites', valorC)

    suma = valorA + valorB + valorC
    return suma


suma = sumatoria(10, 20, 30)
logging.info('sumatoria es: (%s)', suma)
