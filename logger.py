import logging

LOG_FORMAT= "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename ="./logs/debug.log",
						level= logging.DEBUG,
						format= LOG_FORMAT,
						filemode= 'a')

logging.getLogger(__name__).addHandler(logging.NullHandler())