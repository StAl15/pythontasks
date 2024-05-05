import logging


class Logger():
    def __init__(self):
        logging.basicConfig(level=logging.INFO, filename='LOG.log', filemode='w')

    def logging_info(self, msg):
        logging.info(msg)

    def logging_debug(self, msg):
        logging.debug(msg)

    def logging_warning(self, msg):
        logging.warning(msg)

    def logging_error(self, msg):
        logging.error(msg)

    def logging_critical(self, msg):
        logging.critical(msg)
