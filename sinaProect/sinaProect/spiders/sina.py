# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from scrapy_splash import SplashMiddleware
from sinaProect.items import SinaproectItem

class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['finance.sina.com.cn']
    start_urls = ['http://finance.sina.com.cn/stock/sl/#qmxindustry_1']

    def start_requests(self):

        for url in self.start_urls:
            yield SplashRequest(url,callback=self.parse,args={'wait':0.5})

    def parse(self, response):

        stock_div = response.xpath('//div[@class="tblOuter"]//tbody/tr')
        for sto in stock_div:
            item = SinaproectItem()

            bankuai = sto.xpath('.//td[1]/a/text()').extract()
            item['版块'] = bankuai[0] if bankuai else ''

            gsjs = sto.xpath('.//td[2]//text()').extract()
            item['公司家数'] = gsjs[0] if gsjs else ''

            pjjg = sto.xpath('.//td[3]//text()').extract()
            item['平均价格'] = pjjg[0] if pjjg else ''

            zde = sto.xpath('.//td[4]//text()').extract()
            item['涨跌额'] = zde[0] if zde else ''

            zdf = sto.xpath('.//td[5]//text()').extract()
            item['涨跌幅'] = zdf[0] if zdf else ''

            zcjl = sto.xpath('.//td[6]//text()').extract()
            item['总成交量'] = zcjl[0] if zcjl else ''

            zcje = sto.xpath('.//td[7]/text()').extract()
            item['总成交额'] = zcje[0] if zcje else ''

            lzg = sto.xpath('.//td[8]//text()').extract()
            item['领涨股'] = lzg[0] if lzg else ''

            zdf1 = sto.xpath('.//td[9]//text()').extract()
            item['涨跌幅1'] = zdf1[0] if zdf1 else ''

            dqj = sto.xpath('.//td[10]//text()').extract()
            item['当前价'] = dqj[0] if dqj else ''

            zde1 = sto.xpath('.//td[11]//text()').extract()
            item['涨跌额1'] = zde1[0] if zde1 else ''

            yield item

