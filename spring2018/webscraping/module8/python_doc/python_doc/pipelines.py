from datetime import datetime

class LogItemPipeline(object):

    def __init__(self, filename):
        # Saving filename to instance variable
        self.file_name = filename
        self.file_handle = None

    @classmethod    
    def from_crawler(cls, crawler):
        # Gets value of LOG_FILE_NAME from settings.py
        log_file_name = crawler.settings.get('LOG_FILE_NAME')
        # Returns a LogItemPipeline object 
        return cls(log_file_name)

    def open_spider(self, spider):
        # Opening the log file 
        self.file_handle = open(self.file_name, 'w')
        self.file_handle.write(str(datetime.now()) + ': Spider opened\n')

    def process_item(self, item, spider):
        section_name = item['section_name']
        self.file_handle.write(str(datetime.now()) + ': Section \'' + section_name + '\' processed\n')
        return item


    def close_spider(self, spider):
        # Closing the log file
        self.file_handle.write(str(datetime.now()) + ': Spider closed\n')
        self.file_handle.close()