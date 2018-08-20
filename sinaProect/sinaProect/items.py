# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaproectItem(scrapy.Item):
	
    版块 = scrapy.Field()

    公司家数 = scrapy.Field()

    平均价格 = scrapy.Field()

    涨跌额 = scrapy.Field()

    涨跌幅 = scrapy.Field()

    总成交量 = scrapy.Field()

    总成交额 = scrapy.Field()

    领涨股 = scrapy.Field()

    涨跌幅1 = scrapy.Field()

    当前价 = scrapy.Field()

    涨跌额1 = scrapy.Field()
