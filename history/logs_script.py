import logging

logger = logging.getLogger('calc')
logger.setLevel(logging.DEBUG)

handler_calc = logging.FileHandler('history/logs.txt', mode='a')
formatter_calc = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

handler_calc.setFormatter(formatter_calc)
logger.addHandler(handler_calc)
