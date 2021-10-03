from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["https://www.amazon.in/"]
    start_urls = ["https://www.amazon.in/s?k=iphone+12"]


    def parse(self, response):
        nodes = Selector(response).xpath("//div[contains(@class, 's-asin')]")

        for node in nodes:
            item = StackItem()
            # import pdb;pdb.set_trace()
            item['title'] = node.xpath(".//span[contains(@class, 'a-text-normal')]/text()").extract()[0]
            price = node.xpath(".//span[contains(@class, 'a-price-whole')]/text()").extract()
            if price:
                item['price'] = price[0]
            item['url'] = node.xpath(".//a[contains(@class, 's-no-outline')]/@href").extract()[0]
            item['image'] = node.xpath(".//img[contains(@class, 's-image')]/@src").extract()[0]
            yield item

