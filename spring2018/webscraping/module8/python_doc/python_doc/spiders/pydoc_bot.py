import scrapy
from python_doc.items import DocSectionItem

class PydocBotSpider(scrapy.Spider):
    name = "pydoc_bot"
    start_urls = (
        'https://docs.python.org/3/',
    )

    def parse(self, response):
        for a_el in response.xpath('//table[@class="contentstable"]//a[@class="biglink"]'):
            section = DocSectionItem()
            section['section_name'] = a_el.xpath('./text()').extract()[0]
            section['section_link'] = a_el.xpath('./@href').extract()[0]
            print(type(section))
            yield section
