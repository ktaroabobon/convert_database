from pathlib import Path
from logging import getLogger

import pandas as pd
import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative

from utils import utils

logger = getLogger(__name__)


class DataFrame(object):

    def __init__(self, import_info, output_info: dict):
        self.import_info = import_info
        self.output_info = output_info
        self.df = None
        self.base_dir = Path(__file__).resolve().parent.parent

    def import_data(self) -> bool:
        logger.info({'action': 'import data', 'status': 'run', })
        if not self.import_info:
            return False

        if self.import_info['file_type'].lower() == 'csv':
            """
            importファイルがcsvの場合
            """
            logger.info(self.import_info)
            if not utils.has_extension(self.import_info['file_name'], "csv"):
                self.import_info['file_name'] = f"{self.import_info['file_name']}.csv"
            try:
                self.df = pd.read_csv(
                    filepath_or_buffer=self.base_dir / "import_data" / f"{self.import_info['file_name']}",
                )
            except Exception as e:
                logger.info({'action': 'import_data', 'error': e}, self.import_info)
                return False
            return True

        if self.import_info['file_type'].lower() == 'excel':
            """
            importファイルがexcelの場合
            """
            logger.info(self.import_info)
            if not utils.has_extension(self.import_info['file_name'], "xlsx"):
                self.import_info['file_name'] = f"{self.import_info['file_name']}.xlsx"
            try:
                self.df = pd.read_excel(
                    filepath_or_buffer=self.base_dir / "import_data" / f"{self.import_info['file_name']}",
                    sheet_name=self.import_info['table_name'],
                )
            except Exception as e:
                logger.info({'action': 'import_data', 'error': e}, self.import_info)
                return False
            return True

        if utils.is_sql(self.import_info["file_type"]):
            database_name = self.import_info['file_name']
            if self.import_info["file_type"].lower() == 'mysql':
                """
                importファイルがMYSQLの場合
                """
                logger.info(
                    self.import_info,
                    {
                        'database': 'MYSQL',
                        'database_name': database_name,
                    })
                engine = sqlalchemy.create_engine(
                    f'mysql+pymysql://root:@localhost/{database_name}')
            else:
                """
                importファイルがMYSQL以外(sqlite3)の場合
                """
                logger.info(
                    self.import_info,
                    {
                        'database': 'sqlite3',
                        'database_name': database_name,
                    })
                if not utils.has_extension(database_name, "db"):
                    database_name = f"{database_name}.db"
                database_path = self.base_dir / "import_data" / database_name
                engine = sqlalchemy.create_engine(f'sqlite:///{database_path}')

            try:
                self.df = pd.read_sql(
                    self.import_info['table_name'], con=engine
                )
            except Exception as e:
                logger.info({'action': 'import_data', 'error': e}, self.import_info)
                return False
            return True

    def output_data(self) -> bool:
        logger.info({'action': 'output_data data', 'status': 'run', })
        if not self.output_info:
            return False

        if self.output_info['file_type'].lower() == 'csv':
            """
            outputファイルがcsvの場合
            """
            logger.info(self.output_info)
            if not utils.has_extension(self.output_info['file_name'], "csv"):
                self.output_info['file_name'] = f"{self.output_info['file_name']}.csv"
            try:
                self.df.to_csv(
                    self.base_dir / "output_data" / f"{self.output_info['file_name']}",
                )
            except Exception as e:
                logger.info({'action': 'output_data', 'error': e}, self.output_info)
                return False
            return True

        if self.output_info['file_type'].lower() == 'excel':
            """
            outputファイルがexcelの場合
            """
            logger.info(self.output_info)
            if not utils.has_extension(self.output_info['file_name'], "xlsx"):
                self.output_info['file_name'] = f"{self.output_info['file_name']}.xlsx"
            try:
                self.df.to_excel(
                    self.base_dir / "output_data" / f"{self.output_info['file_name']}",
                    sheet_name=self.output_info['table_name'],
                )
            except Exception as e:
                logger.info({'action': 'output_data', 'error': e}, self.output_info)
                return False
            return True

        if utils.is_sql(self.output_info["file_type"]):
            database_name = self.output_info['file_name']
            if self.output_info["file_type"].lower() == 'mysql':
                """
                outputファイルがMYSQLの場合
                """
                logger.info(
                    self.output_info,
                    {
                        'database': 'MYSQL',
                        'database_name': database_name,
                    })
                engine = sqlalchemy.create_engine(
                    f'mysql+pymysql://root:@localhost/{database_name}')
            else:
                """
                outputファイルがMYSQL以外(sqlite3)の場合
                """
                logger.info(
                    self.output_info,
                    {
                        'database': 'sqlite3',
                        'database_name': database_name,
                    })
                if not utils.has_extension(database_name, "db"):
                    database_name = f"{database_name}.db"
                database_path = self.base_dir / "output_data" / database_name
                engine = sqlalchemy.create_engine(f'sqlite:///{database_path}')

            try:
                self.df.to_sql(
                    self.output_info['table_name'], con=engine
                )
            except Exception as e:
                logger.info({'action': 'output_data', 'error': e}, self.output_info)
                return False
            return True
