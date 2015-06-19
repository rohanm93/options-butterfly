import scrapy
from options.items import OptionsItem

class OptionsSpider(scrapy.Spider):
    name = "optionsspider"
    allowed_domains = ["nseindia.com"]
    start_urls = [
        "http://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=242&symbol=RELIANCE&symbol=reliance&instrument=OPTSTK&date=-&segmentLink=17&segmentLink=17",
        "http://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=2212&symbol=TCS&symbol=tcs&instrument=OPTSTK&date=-&segmentLink=17&segmentLink=17"
    ]

    def parse(self, response):
        rows = response.xpath('//*[@id="wrapper_btm"]/div[3]/table/tr')
        i = 0
        for row in rows:
            itemCall = OptionsItem()
            itemCall['date'] = "date"
            itemCall['time'] = "time"
            itemCall['stockName'] = "stock name"
            itemCall['currentPrice'] = "price"
            itemCall['strikePrice'] = row.xpath('td[12]//text()').extract()
            itemCall['askPrice'] = row.xpath('td[10]/text()').extract()
            itemCall['askQty'] = row.xpath('td[11]/text()').extract()
            itemCall['oi'] = row.xpath('td[2]/text()').extract()
            yield itemCall
        pass
