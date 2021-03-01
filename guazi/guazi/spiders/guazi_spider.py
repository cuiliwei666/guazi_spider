import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GuaziSpiderSpider(CrawlSpider):
    name = 'guazi_spider'
    allowed_domains = ['guazi.com']
    start_urls = ['https://www.guazi.com/ty/buy/o1']

    rules = (
        Rule(LinkExtractor(allow=r'/ty/buy/o\d/'), follow=True),
		Rule(LinkExtractor(allow=r'https://www.guazi.com/[a-z]+/\w+\.htm#fr_page=list&fr_pos=city&fr_no=\d+'), callback='parse_item', follow=False),
    )
    def parse_item(self, response):
        item = {}
        url = response.url
        print(url)
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
