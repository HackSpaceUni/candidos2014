# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CandidatoItem(Item):
    # define the fields for your item here like:
    cid=Field()
    cargo_postula=Field()
    lugar_postula=Field()
    dni=Field()
    apellido_paterno=Field()
    apellido_materno=Field()
    nombres=Field()
    fecha_nacimiento=Field()
    correo_electronico=Field()
    lugar_residencia=Field()
    lugar_departamento_residencia=Field()
    lugar_provincia_residencia=Field()
    lugar_distrito_residencia=Field()
    lugar_tiempo_residencia=Field()

class ExperienciaItem(Item):
    centro_de_trabajo=Field()
    sector=Field()
    fecha_desde=Field()
    fecha_hasta=Field()
    cargo=Field()
    ubicacion=Field()
