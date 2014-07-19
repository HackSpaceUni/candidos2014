# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.contrib.exporter import CsvItemExporter
from jne.items import CandidatoItem

class JnePipeline(object):
    
    candidato_filename = './output/candidato.csv'

    def __init__(self):
        self.candidato_file = open(self.candidato_filename, 'wb')
        self.candidato_exporter = CsvItemExporter(self.candidato_file)


    def process_item(self, item, spider):
        if isinstance(item, CandidatoItem):
            self.candidato_exporter.export_item(item)
        return item
