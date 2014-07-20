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

from jne.items import CandidatoItem, ExperienciaLaboralItem

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
        
        time.sleep(3)

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
        
        el = self.driver.find_element_by_xpath('//*[@id="tblExperiencia"]')
        num_filas_experiencia =  len(el.find_elements_by_xpath('.//tbody/tr'))        
        if (num_filas_experiencia > 1):
            num_items_experiencia = (num_filas_experiencia + 1)/4
            for item_experiencia in range(0, num_items_experiencia):
                experienciaLaboralItem = ExperienciaLaboralItem()

                content = el.find_element_by_xpath('.//tbody/tr['+str(4*item_experiencia+1)+']/td[1]')
                experienciaLaboralItem['centro_de_trabajo'] = content.text
                content = el.find_element_by_xpath('.//tbody/tr['+str(4*item_experiencia+1)+']/td[2]')
                experienciaLaboralItem['sector'] = content.text
                content = el.find_element_by_xpath('.//tbody/tr['+str(4*item_experiencia+2)+']/td[1]')
                experienciaLaboralItem['fecha_desde'] = content.text
                content = el.find_element_by_xpath('.//tbody/tr['+str(4*item_experiencia+2)+']/td[2]')
                experienciaLaboralItem['fecha_hasta'] = content.text
                content = el.find_element_by_xpath('.//tbody/tr['+str(4*item_experiencia+3)+']/td[1]')
                experienciaLaboralItem['cargo'] = content.text
                content = el.find_element_by_xpath('.//tbody/tr['+str(4*item_experiencia+3)+']/td[2]')
                experienciaLaboralItem['ubicacion'] = content.text

                items.append(experienciaLaboralItem)
    

        return items


