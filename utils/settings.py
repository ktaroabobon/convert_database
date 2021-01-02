import configparser

config = configparser.ConfigParser()
config.read('settings.ini', encoding='utf-8')

import_file_type = config['import']['type']
import_file_name = config['import']['file_name']
import_table_name = config['import']['table_name']

output_file_type = config['output']['type']
output_file_name = config['output']['file_name']
output_table_name = config['output']['table_name']


def import_info() -> dict:
    return {
        "file_type": import_file_type,
        "file_name": import_file_name,
        "table_name": import_table_name,
    }


def output_info() -> dict:
    return {
        "file_type": output_file_type,
        "file_name": output_file_name,
        "table_name": output_table_name,
    }
