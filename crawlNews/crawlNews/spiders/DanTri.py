import json
import scrapy
from datetime import datetime

OUTPUT_FILENAME = 'C:/Users/MSI 14RAS/PycharmProjects/Week02-Scrapy/crawlNews/crawlNews/spiders/Output/dantri.txt'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))

class CrawlDantri (scrapy.Spider):
        name = 'dantri'

        start_urls = ['https://dantri.com.vn/suc-khoe/hai-benh-vien-cua-da-nang-cang-minh-dieu-tri-cho-12-ca-mac-covid-19-nang-20200808170111879.htm#dt_source=Cate_SuKien&dt_campaign=Cover&dt_medium=1']

        def parse(self, response):
                data = {
                'link': response.url,
                'title': response.css('h1.dt-news__title::text').get(),
                'author': response.css('.dt-news__content strong').css('::text').get(),
                'content': response.css('.content-box p , .img-wrapper+ p , .dt-news__content p+ p , .dt-news__content > p:nth-child(1) , .dt-news__sapo h2').css('::text').get(),
                'date': response.css('.dt-news__time').css('::text').get(),
                'tags': response.css('.dt-news__tag a').css('::text').get()
                }

                with open(OUTPUT_FILENAME, 'a+', encoding='utf8') as f:
                        f.write(json.dumps(data, ensure_ascii=False))
                        f.write('\n')
                        print('SUCCESS:', response.url)

                for href in response.css('a::attr(href)').getall():
                        yield response.follow(href, callback=self.parse)
