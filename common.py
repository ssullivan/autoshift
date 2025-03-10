#############################################################################
#
# Copyright (C) 2018 Fabian Schweinfurth
# Contact: autoshift <at> derfabbi.de
#
# This file is part of autoshift
#
# autoshift is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# autoshift is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with autoshift.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
import logging
from logging import NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
from os import path

FILEPATH = path.realpath(__file__)
DIRNAME = path.dirname(FILEPATH)


def initLogger():

    colors = {
        NOTSET: 36,
        DEBUG: 33,
        INFO: 34,
        WARNING: .35,
        ERROR: 31,
        CRITICAL: "5;31"
    }
    logger = None

    logger = logging.getLogger("autoshift")

    def rec_filter(record):
        record.module_lineno = ""
        if record.levelno == DEBUG:
            record.module_lineno = "\033[1;36m{}:{} - ".format(
                record.module,
                record.lineno)
        record.color = colors[record.levelno]
        record.spaces = " " * (8 - len(record.levelname))
        return True

    h = logging.StreamHandler()
    h.setFormatter(
        logging.Formatter("\r{bcolor}%(asctime)s "
                          "[\033[1;%(color)sm%(levelname)s\033[0m{bcolor}] "
                          "\033[0m%(spaces)s"
                          "%(module_lineno)s"


                          "\033[0m%(message)s"
                          .format(bcolor="\033[1;36m")))
    h.addFilter(rec_filter)
    logger.handlers = []
    logger.addHandler(h)
    return logger


_L = initLogger()
