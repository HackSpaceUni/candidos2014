# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.contrib.exporter import CsvItemExporter
from jne.items import CandidatoItem, ExperienciaLaboralItem

class JnePipeline(object):
    
    candidato_filename = './output/candidato.csv'
    experiencia_laboral_filename = './output/experiencia_laboral.csv'

    def __init__(self):
        self.candidato_file = open(self.candidato_filename, 'wb')
        self.candidato_exporter = CsvItemExporter(self.candidato_file)
        self.experiencia_laboral_file = open(self.experiencia_laboral_filename, 'wb')
        self.experiencia_laboral_exporter = CsvItemExporter(self.experiencia_laboral_file)

    def process_item(self, item, spider):
        if isinstance(item, CandidatoItem):
            self.candidato_exporter.export_item(item)
        if isinstance(item, ExperienciaLaboralItem):
            self.experiencia_laboral_exporter.export_item(item)

        return item
