# -*- coding: utf-8 -*-
import scrapy
from stackov.items import JobItem

class JobsBotSpider(scrapy.Spider):
    name = 'jobs_bot'
    base_url = 'https://stackoverflow.com'
    start_urls = [base_url + '/jobs?med=site-ui&ref=jobs-tab/']

    def parse(self, response):
        
        next_url = None
        next_url = response.xpath('//div[@class="jobsfooter js-footer"]//a[@class="prev-next job-link test-pagination-next"]/@href')

        elements = response.xpath('//div[@class="listResults"]//div[@class="-job-summary "]')
        for e in elements:        
            job_item = JobItem()
            title = e.css('div.-title h2.g-col10 a.job-link::text').extract()[0]
            company = e.css('div.-company div.-name::text').extract()[0]            
            location = e.css('div.-company div.-location::text').extract()[0]
            job_item['title'] = title
            job_item['company'] = " ".join(company.split()) # Remove redundent white spaces
            job_item['location'] = " ".join(location.split()).strip("-") # Remove redundent white spaces
            yield job_item

        yield scrapy.Request(self.base_url + next_url.extract()[0], callback=self.parse)
