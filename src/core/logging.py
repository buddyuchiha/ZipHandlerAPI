import logging

from core.config import settings


logger = logging.Logger("ZipHandlerAPI Logger")
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

file_handler = logging.FileHandler(settings.LOGGING_FILE)
file_handler.setFormatter(formatter)
file_handler.setLevel("INFO")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel("ERROR")

logger.addHandler(file_handler)
logger.addHandler(stream_handler)