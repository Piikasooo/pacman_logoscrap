import scrapy
from ..items import Logo
from scrapy.loader import ItemLoader


class LogoSpider(scrapy.Spider):
    name = "logo"

    start_urls = ['https://www.gethatch.com/en/', ]