import scrapy
from options.items import OptionsItem
import datetime

class OptionsSpider(scrapy.Spider):
    name = "optionsspider"
    allowed_domains = ["nseindia.com"]
    start_urls = [
        "http://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=242&symbol=RELIANCE&symbol=reliance&instrument=OPTSTK&date=-&segmentLink=17&segmentLink=17",
        "http://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=2212&symbol=TCS&symbol=tcs&instrument=OPTSTK&date=-&segmentLink=17&segmentLink=17"
    ]

    def parse(self, response):
        rows = response.xpath('//*[@id="wrapper_btm"]/div[3]/table/tr')
        stockName = response.xpath('//*[@id="wrapper_btm"]/table[1]/tr/td[2]/div/span[1]/b//text()').extract()[0].split(' ',1)[0]
        currentStockPrice = response.xpath('//*[@id="wrapper_btm"]/table[1]/tr/td[2]/div/span[1]/b//text()').extract()[0].split(' ',1)[1]
        dateTimeXpath = response.xpath('//*[@id="wrapper_btm"]/table[1]/tr/td[2]/div/span[2]/text()').extract()[0]
        dateTimeUpdated = datetime.datetime.strptime(dateTimeXpath,'As on %b %d, %Y %H:%M:%S IST')

        i = 0 # use this to skip first x records; might not be needed with later filter of oi>=0

        for row in rows:
            itemCall = OptionsItem()
            itemCall['dateTimeUpdated'] = dateTimeUpdated
            itemCall['stockName'] = stockName
            itemCall['currentPrice'] = currentStockPrice
            itemCall['strikePrice'] = ''.join(row.xpath('td[12]//text()').extract())
            itemCall['askPrice'] = ''.join(row.xpath('td[10]/text()').extract())
            itemCall['askQty'] = ''.join(row.xpath('td[11]/text()').extract())
            itemCall['oi'] = ''.join(row.xpath('td[2]/text()').extract())
            itemCall['cp'] = 'c'
            
            itemPut = OptionsItem()
            itemPut['dateTimeUpdated'] = dateTimeUpdated
            itemPut['stockName'] = stockName
            itemPut['currentPrice'] = currentStockPrice
            itemPut['strikePrice'] = ''.join(row.xpath('td[12]//text()').extract())
            itemPut['askPrice'] = ''.join(row.xpath('td[15]/text()').extract())
            itemPut['askQty'] = ''.join(row.xpath('td[16]/text()').extract())
            itemPut['oi'] = ''.join(row.xpath('td[22]/text()').extract())
            itemPut['cp'] = 'p'
            yield itemCall
            yield itemPut
        pass