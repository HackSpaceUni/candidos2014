# -*- coding: utf-8 -*-
import time
import urlparse
import re
from urlparse import urlsplit
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from jne.items import CandidatoItem

class CandidatosSpider(Spider):
    name = 'candidatos'
    allowed_domains = ['200.48.102.67']
    start_urls = [ 'http://200.48.102.67/pecaoe/sipe/HojaVida.htm?' ]

    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        base_url = response.url
        paginas = range(1,10)
        for pagina in paginas:
           url = '%sc=%s&p=72&op=140' % (base_url, pagina)
           yield Request(url, callback=self.parse_page)

    def parse_page(self, response):
        self.driver.get(response.url)
        
        time.sleep(5)

        candidatoItem = CandidatoItem()

        cargo_postula = self.driver.find_element_by_xpath('//span[@id="txtCargoPostula"]').text

        candidatoItem['cargo_postula'] = cargo_postula

        return candidatoItem


