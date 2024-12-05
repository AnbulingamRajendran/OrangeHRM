import logging
import os

import pytest


class logGenerator:
    @staticmethod
    def logGen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\Logs\\reports.log', mode='w')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                                      datefmt='%d-%b-%y %I:%M:%S %p')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger

