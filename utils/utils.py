from logging import getLogger

from utils import constants

logger = getLogger(__name__)


def is_sql(extension: str) -> bool:
    logger.info({'action': 'is_sql', 'status': 'run', })
    if extension in ".":
        _, extension = extension.rsplit(".", 1)

    if extension.lower() in constants.sql_extension:
        logger.info({'action': 'is_sql', 'is_sql': 'yes', })
        return True
    else:
        logger.info({'action': 'is_sql', 'is_sql': 'no', })
        return False


def has_extension(file_name, extension: str) -> bool:
    if extension is None:
        return True

    if file_name[-len(extension):] == extension:
        return True

    return False
