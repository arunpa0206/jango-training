
'''
import logging
logging.basicConfig(level=logging.DEBUG)

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

import logging

logging.basicConfig(filename='example.log',filemode='w',level=logging.DEBUG)
logging.debug('This message should go to the log file')

logging.info('So should this')
logging.warning('And this, too')
'''

import logging
logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')

'''

import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')
