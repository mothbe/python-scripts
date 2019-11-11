import logging
import argparse
from logging.config import fileConfig

if __name__=="__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-d','--debug', help='Enabling debug messages', action="store_true")
  # parser.add_argument('-d','--debug', help='Enabling debug messages', required=False)
  args = parser.parse_args()
  loggers='root'

  if args.debug:
    loggers='console'

  print('loggers: {}'.format(loggers))
  print('Args: {}'.format(args))
  fileConfig('logging_config.ini')
  logger = logging.getLogger(loggers)
  logger.debug('the best scripting language is python in the world')
  
  a = 5
  b = 0
  
  try:
    c = a / b
  except Exception as e:
    logger.error("Exception occurred", exc_info=True)
