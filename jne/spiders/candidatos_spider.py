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
        paginas = range(104272,104273)
        for pagina in paginas:
           url = '%sc=%s&p=72&op=140' % (base_url, pagina)
           yield Request(url, callback=self.parse_page)

    def parse_page(self, response):
        items=[]

        self.driver.get(response.url)
        
        time.sleep(5)

        candidatoItem = CandidatoItem()

        content = self.driver.find_element_by_xpath('//span[@id="txtCargoPostula"]')
        candidatoItem['cargo_postula'] = content.text

        content = self.driver.find_element_by_xpath('//span[@id="txtLugarPostula"]')
        candidatoItem['lugar_postula'] = content.text
         
        content = self.driver.find_element_by_xpath('//span[@id="txtDNI"]')
        candidatoItem['dni'] = content.text
         
        content = self.driver.find_element_by_xpath('//span[@id="txtApellidoPaterno"]')
        candidatoItem['apellido_paterno'] = content.text
         
        content = self.driver.find_element_by_xpath('//span[@id="txtApellidoMaterno"]')
        candidatoItem['apellido_materno'] = content.text
         
        content = self.driver.find_element_by_xpath('//span[@id="txtNombres"]')
        candidatoItem['nombres'] = content.text
         
        content = self.driver.find_element_by_xpath('//span[@id="txtFechaNacimiento"]')
        candidatoItem['fecha_nacimiento'] = content.text
         
        content = self.driver.find_element_by_xpath('//span[@id="txtCorreoElectronico"]')
        candidatoItem['correo_electronico'] = content.text
         
        content = self.driver.find_element_by_xpath('//span[@id="txtLugarResicencia"]')
        candidatoItem['lugar_residencia'] = content.text
         
        content = self.driver.find_element_by_xpath('//span[@id="txtLugarDepartamentoRes"]')
        candidatoItem['lugar_departamento_residencia'] = content.text
         
        content = self.driver.find_element_by_xpath('//span[@id="txtLugarProvinciaRes"]')
        candidatoItem['lugar_provincia_residencia'] = content.text
         
        content = self.driver.find_element_by_xpath('//span[@id="txtLugarDistritoRes"]')
        candidatoItem['lugar_distrito_residencia'] = content.text
         
        content = self.driver.find_element_by_xpath('//span[@id="txtTiempoRes"]')
        candidatoItem['lugar_tiempo_residencia'] = content.text

        items.append(candidatoItem)
        
        content = self.driver.find_element_by_xpath('//*[@id="tblExperiencia"]')
        for tr_e_l in content.find_elements_by_css_selector('tr'):
            print tr_e_l.text

        return items


