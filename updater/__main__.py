import datetime
import time
import os

import wget

from app.config import URL, SCHEDULE_PATH, UPDATES_LOG_PATH
from .parser import TableParser

update_logger = open(UPDATES_LOG_PATH, 'a', encoding='utf8')


def update_table():
    if os.path.isfile(SCHEDULE_PATH):
        os.remove(SCHEDULE_PATH)

    update_logger.write(str(datetime.datetime.now()) + '\n')
    update_logger.flush()

    wget.download(URL + '/export?exportFormat=xlsx', SCHEDULE_PATH, bar=None)
    parser = TableParser(SCHEDULE_PATH)
    parser.parse()
    parser.__del__()

    update_logger.write(str(datetime.datetime.now()) + '\n\n')
    update_logger.flush()


def main():
    while True:
        update_table()
        time.sleep(20 * 60)


if __name__ == '__main__':
    main()
