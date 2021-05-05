import logging
import colorlog

def define_log_settings():
    logger = colorlog.getLogger()
    logger.setLevel(colorlog.colorlog.logging.DEBUG)

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter())
    logger.addHandler(handler)

    logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s] %(filename)s:%(lineno)d | %(levelname)s - %(message)s',
                        datefmt='%H:%M:%S'
                        )
