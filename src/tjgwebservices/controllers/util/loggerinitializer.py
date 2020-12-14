import logging

def initialize_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
     
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
