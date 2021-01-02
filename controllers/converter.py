from logging import getLogger

from models import dataframe
from utils import settings

logger = getLogger(__name__)


def database_converter() -> None:
    logger.info({'action': 'database_converter', 'status': 'run', })
    df = dataframe.DataFrame(import_info=settings.import_info(), output_info=settings.output_info())

    logger.info({'action': 'database_converter', 'message': 'import database', })
    if not df.import_data():
        logger.warning({'action': 'import data', 'status': 'failure', })
        raise

    logger.info({'action': 'database_converter', 'message': 'convert database', })
    if not df.output_data():
        logger.warning({'action': 'output_data data', 'status': 'failure', })
        raise

    return
