import logging #superhero book

logger = logging.getLogger('SuperHero')

logging.basicConfig(level=logging.WARNING) # setting what all to be written in the superhero book

logger.info('Your mission is started')
logger.warning('The tree is very tall !')
logger.error('You slipped from the tree')
logger.critical('The kitten falling from your hand , do back-up')
logger.info('Mission Failed')