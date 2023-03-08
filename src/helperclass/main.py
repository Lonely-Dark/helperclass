#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.10

import logging
import os.path

import coloredlogs


class Helper:

    def __init__(self, name: str = __name__, streams: int = 1, filename: str = "log.log", log_level: int = 10) -> None:
        """
        Helper class for logging and .env file. For me and my projects.
        :param name: name of the logger
        :param streams: 1,2,3; 1 - StreamHandler, 2 - FileHandler, 3 - All Handlers
        :param filename: filename of the log file
        :param log_level: DEBUG, INFO, WARNING, ERROR, CRITICAL (10, 20, 30, 40, 50)
        """

        self.log_format: str = '[%(asctime)s] [%(filename)s] [%(levelname)s] [%(' \
                               'lineno)d]: %(' \
                               'message)s '
        self.log_level = log_level
        formatter_colored: coloredlogs.ColoredFormatter = coloredlogs.ColoredFormatter(self.log_format)
        self.logger: logging.Logger = logging.getLogger(name)

        match streams:
            case 1:
                handler_stream: logging.StreamHandler = logging.StreamHandler()
                handler_stream.setLevel(self.log_level)
                handler_stream.setFormatter(formatter_colored)
                self.logger.addHandler(handler_stream)
            case 2:
                handler_file: logging.FileHandler = logging.FileHandler(
                    filename=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log.log'), mode='w')
                handler_file.setLevel(self.log_level)
                handler_file.setFormatter(formatter_colored)
                self.logger.addHandler(handler_file)
            case 3:
                handler_stream: logging.StreamHandler = logging.StreamHandler()
                handler_stream.setLevel(self.log_level)
                handler_stream.setFormatter(formatter_colored)
                handler_file: logging.FileHandler = logging.FileHandler(
                    filename=os.path.join(os.path.dirname(os.path.abspath(__file__)), filename), mode='w')
                handler_file.setLevel(self.log_level)
                handler_file.setFormatter(formatter_colored)
                self.logger.addHandler(handler_stream)
                self.logger.addHandler(handler_file)
