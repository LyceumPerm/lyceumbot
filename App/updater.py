import datetime
import time
import os

import wget

from constants import GOOGLETABLE_URL, CURRENT_FILE, available_days
from parser import TableParser

local_filename = f'resources/schedule/{CURRENT_FILE}'
update_logger = open('logs/updates.log', 'a', encoding='utf8')


def update_table():
    if os.path.isfile(local_filename):
        os.remove(local_filename)

    update_logger.write(str(datetime.datetime.now()) + '\n')
    update_logger.flush()

    wget.download(GOOGLETABLE_URL, local_filename)
    parser = TableParser(local_filename)
    parser.parse()
    parser.__del__()

    update_logger.write(str(datetime.datetime.now()) + '\n\n')
    update_logger.flush()


if __name__ == '__main__':
    while True:
        update_table()
        time.sleep(20 * 60)
