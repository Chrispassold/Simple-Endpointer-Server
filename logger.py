import logging


class ColorsCmd:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Logger:
    format = logging.Formatter('%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')
    logger = None

    def __init__(self, name, filename):
        handler = logging.FileHandler(filename, 'w', 'UTF-8')
        handler.setFormatter(self.format)

        self.logger = logging.getLogger(name)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

    def debug(self, message):
        print(ColorsCmd.OKBLUE, message, ColorsCmd.OKBLUE)
        if self.logger:
            self.logger.debug(message)

    def success(self, message):
        print(ColorsCmd.OKGREEN, message, ColorsCmd.OKGREEN)
        if self.logger:
            self.logger.info(message)

    def fail(self, message, error):
        print(ColorsCmd.FAIL, message, ColorsCmd.FAIL)
        if self.logger:
            self.logger.fatal(str(error))
