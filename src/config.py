import logging

# Configure logging output.
logging_format = "[%(asctime)s] %(message)s"
date_format = "%Y-%d-%m %H:%M:%S"

logging.basicConfig(format=logging_format,
                    datefmt=date_format,
                    level=logging.DEBUG)

DEFAULT_HOST = "localhost"

ONE_DAY_IN_SECONDS = 86400