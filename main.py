from logging import basicConfig, INFO
import sys

from controllers import converter

logger = basicConfig(level=INFO, stream=sys.stdout)

if __name__ == '__main__':
    converter.database_converter()
