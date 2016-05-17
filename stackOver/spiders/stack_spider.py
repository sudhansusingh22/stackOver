from scrapy import Spider
from scrapy.selector import Selector
from stackOver.items import StackItem


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = ["http://stackoverflow.com/questions?sort=newest"]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')
        userDetails = Selector(response).xpath('//div[@class="summary"]//div[@class="user-details"]')

        for question,user in zip(questions,userDetails):
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            item['userName'] = user.xpath('a/text()').extract()[0]
            item['userUrl'] = user.xpath('a/@href').extract()[0]  
            yield item