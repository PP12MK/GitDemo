import inspect
import logging

import pytest

@pytest.mark.usefixtures("setup")
class BaseClass:
    def getlogger(self):
        loggerName=inspect.stack()[1][3]
        logger=logging.getlogger(loggerName)
        fileHandler=logging.FileHandler("logfile.log")
        formatter=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger