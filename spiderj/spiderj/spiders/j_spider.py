import scrapy
from ..items import NoItem
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class JSpider(scrapy.spiders.CrawlSpider):
    name = "jav"
    allowed_domains = ["www.jav321.com"]
    url = "https://www.jav321.com/star/1007544/"
    start_urls = (
            url+'1',
    )

    rules = (
        Rule(LinkExtractor(allow=r'/star/1007544/\d+'), follow = True),
        Rule(LinkExtractor(allow=r'/video/\S+'), follow = False, callback = 'parse_item'),
    )

    def parse_item(self, response):
        item = NoItem()
        #movies = response.xpath("//div[@class='thumbnail']/a/@href")

        item['product_no'] = response.xpath('//small/text()').extract()[0].split(' ',1)[0]
        item['tags'] = response.xpath('//a[following-sibling::b[text()=\'番号\'] and preceding-sibling::b[text()=\'标签\']]/text()').extract()
        item['actress_no'] = response.xpath('//small/text()').extract()[0].split(' ',1)[1]
        #item['url'] = response.url

        yield item