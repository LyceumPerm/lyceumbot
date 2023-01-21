import datetime

import schedule
import wget

from constants import GOOGLETABLE_URL
from parser import TableParser

local_filename = 'resources/schedule/23.01week.xlsx'
update_logger = open('logs/updates.log', 'a', encoding='utf8')


class TableUpdater:

    def download_file(self, url):
        wget.download(url, local_filename)

    def download_and_parse_file(self):
        update_logger.write(str(datetime.datetime.now()) + '\n\n')
        update_logger.flush()

        self.download_file(GOOGLETABLE_URL)
        parser = TableParser(local_filename)
        parser.clear()
        parser.parse()

    def run(self):
        schedule.every(30).seconds.do(self.download_and_parse_file)
        while True:
            try:
                schedule.run_pending()
            except:
                pass


if __name__ == '__main__':
    updater = TableUpdater()
    updater.run()
