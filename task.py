import logging

logger = logging.getLogger(__name__)


def add(a, b):
    logger.debug("{} + {} = {}".format(a, b, a + b))
    return a + b
