# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from models import Options, db_connect, create_options_table


class OptionsPipeline(object):
    def __init__(self):
    	engine = db_connect()
        create_options_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
    	if '-' in item['askPrice']:
    		return item
    	if '-' in item['askQty']:
    		return item
    	if '-' in item['oi']:
    		return item

        session = self.Session()
        option = Options(**item)
        try:
            session.add(option)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item