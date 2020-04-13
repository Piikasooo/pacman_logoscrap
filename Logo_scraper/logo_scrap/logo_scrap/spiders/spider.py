import scrapy
from scrapy import signals


class LogoSpider(scrapy.Spider):
    """
    Spider to find links to logos from the site
    """

    name = "logo"
    find_url = []
    start_urls = ['https://www.gethatch.com/en/', ]

    def parse(self, response):
        """
        Function for finding links to other pages of the site
        :param response:
        :return:
        """
        for next_page in response.css("div.inner a::attr(href)").getall():
            yield scrapy.Request(next_page, callback=self.parse_link_logo)

    def parse_link_logo(self, response):
        """
        Function for finding links to logos from the page
        :param response:
        :return:
        """
        for link in response.css("img.qode_client_main_image::attr(src)").getall():
            if link not in self.find_url:
                self.find_url.append(link)
        for link in response.css("div.testimonial_image_holder img::attr(src)").getall():
            if link not in self.find_url:
                self.find_url.append(link)


    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(LogoSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        """
        Printed links to console output.
        :param spider:
        :return:
        """
        for link in self.find_url:
            print(link)

