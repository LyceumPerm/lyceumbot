import datetime
import os

import schedule
import wget

from constants import GOOGLETABLE_URL
from parser import TableParser

local_filename = 'resources/schedule/23.01week.xlsx'
update_logger = open('logs/updates.log', 'a', encoding='utf8')


class TableUpdater:

    def download_file(self, url):
        wget.download(url, local_filename)

    def update(self):
        if os.path.isfile(local_filename):
            os.remove(local_filename)

        update_logger.write(str(datetime.datetime.now()) + '\n')
        update_logger.flush()

        self.download_file(GOOGLETABLE_URL)
        parser = TableParser(local_filename)
        parser.clear()
        parser.parse()

    def run(self):
        schedule.every(9).minutes.do(self.update)
        while True:
            try:
                schedule.run_pending()
            except:
                pass


if __name__ == '__main__':
    updater = TableUpdater()
    updater.run()
