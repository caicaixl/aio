# -*- coding: utf-8 -*-
#__author__ = 'cai'
#__data__ : 2019-05-22 11:35
from templates.temp import Temp
import logging
import os
from logging.handlers import TimedRotatingFileHandler

# from aio import logger

if not os.path.exists("./log/"):
    os.mkdir("./log/")
logger = logging.getLogger()
logger.setLevel(logging.INFO)
fmt = logging.Formatter(fmt="%(asctime)s %(levelname)s %(message)s", datefmt='%Y-%m-%d %H:%M:%S')

console = logging.StreamHandler()
console.setFormatter(fmt)
logger.addHandler(console)

file_handler = TimedRotatingFileHandler(filename=f"./log/phone_deduplication", encoding="UTF-8", when="MIDNIGHT")
file_handler.suffix = "%Y%m%d.log"
file_handler.setFormatter(fmt)
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

BASEPATH = os.path.dirname(__file__)

TEMPLATESPATH = os.path.join(BASEPATH,'templates')
TEMPLATES = Temp()

ALLPHONENUMPATH = os.path.join(BASEPATH,'all_phone_num')



