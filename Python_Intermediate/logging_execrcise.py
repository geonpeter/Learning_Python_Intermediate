import logging

logger = logging.getLogger('SuperHeroLogger')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

file_handler = logging.FileHandler('superhero_logs.txt')
file_handler.setLevel(logging.DEBUG)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


logger.info("Superhero mission started.")
logger.warning("Villain sighted! Proceed with caution.")
logger.error("Gadget malfunction! Need repairs.")
logger.critical("Backup needed immediately!")
logger.debug("Mission update: All clear.")