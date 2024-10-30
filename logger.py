import logging
import sys

logging.basicConfig(
    #DEBUG, INFO, WARNING, ERROR, CRITICAL
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",

    handlers=[
        logging.FileHandler(filename='logs.log', mode='w'),
        logging.StreamHandler(sys.stdout)
    ]
)