import logging


def create_logger() -> logging.Logger:

    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    logger.setLevel(logging.INFO)
    format_setting = "%(asctime)s [%(levelname)s] %(message)s"
    formatter = logging.Formatter(format_setting)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
