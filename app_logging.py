# coding:utf8
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_fmt = '[%(asctime)s] %(levelname)s %(message)s'
formatter = logging.Formatter(log_fmt)

""" 输出日志到控制台 """
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter('%(threadName)s - %(levelname)s - %(message)s'))
# 如果不需要打印到控制台，注释这行即可
logger.addHandler(streamHandler)  

""" 输出日志到日志文件 """
rotatingFileHandler = RotatingFileHandler("logs/app.log", maxBytes=500000, backupCount=2)
rotatingFileHandler.setFormatter(logging.Formatter('%(threadName)s - %(levelname)s - %(message)s'))
# 设置级别如果低于设置的级别则无效
rotatingFileHandler.setLevel(logging.INFO)  
logger.addHandler(rotatingFileHandler)
