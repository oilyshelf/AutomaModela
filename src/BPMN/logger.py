import logging
import logging.config


def getlogger():
    # logger
    logg = logging.getLogger(__name__)
    logg.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.FileHandler(r'log.txt')
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    sh.setLevel(logging.INFO)
    # logger.propagate = False

    # add handlers to logger
    logg.addHandler(ch)
    logg.addHandler(sh)
    return logg


logger = getlogger()
