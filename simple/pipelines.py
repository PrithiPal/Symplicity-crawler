# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib
import scrapy
from scrapy.conf import settings
import pymongo
from scrapy import Field,Item

class JobItem(scrapy.Item) :

    job_description = scrapy.Field()
    job_id = scrapy.Field()
    job_identifier = scrapy.Field()
    job_title = scrapy.Field()
    job_deadline = scrapy.Field()
    
    
#Monolithic function that parses the job posting page, stores relevant information
#and returns item to be stored in the database

class JobPipeline(object) :

    def format_job_description(self,item) :
        job_description_string = ''
        for l in item['job_description'] :
            job_description_string = job_description_string + l
        return job_description_string

    def format_job_id(self,item) :
        job_id_string = ''
        for l in item['job_id'] :
            job_id_string = job_id_string + l

        eliminate_char = ['\n','\t']
        for c in eliminate_char :
            job_id_string = job_id_string.replace(c,"")

        return job_id_string

    def format_job_title(self,item) :
        job_title_string = ''
        for l in item['job_title'] :
            job_title_string = job_title_string + l

        ## remove \n \t from the job_title_string
        eliminate_char = ['\n','\t']
        for c in eliminate_char :
            job_title_string = job_title_string.replace(c,"")

        return job_title_string

    def download_job_attachment(self,item) :

        download_filename, headers = urllib.request.urlretrieve(item['job_attachment_download_link'])
        return download_filename

    def open_spider(self,spider) :
        print("OPEN SPIDER")


    def process_item(self,item,spider) :
        print("PROCESS_ITEM")

        item['job_description'] = self.format_job_description(item)
        item['job_id'] = self.format_job_id(item)
        item['job_title'] = self.format_job_title(item)

        #print("NEW JOB DESCRIPTION: ",item['job_description'])
        #print("NEW JOB ID:",item['job_id'])
        #print("NEW JOB TITLE:",item['job_title'])

        #download_filename = self.download_job_attachment(item)
        #print("FILE DOWNLOADED: ",download_filename)

        return item




    def close_spider(self,spider) :

        print("CLOSE SPIDER")

class MonodbPipeline(object) :


    def __init__(self) :

        connection = pymongo.MongoClient(
        settings['MONGODB_SERVER'],
        settings['MONGODB_PORT']

        )

        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]


    def open_spider(self,spider) :
        print("MONGO OPEN SPIDER")

    def process_item(self,item,spider) :
        # reformat the fields
        item['job_description'] = self.format_job_description(item)
        item['job_id'] = self.format_job_id(item)
        item['job_title'] = self.format_job_title(item)

        self.collection.insert(dict(item))
        print("ITEM INSERTED")

        return item
    def format_job_description(self,item) :
        job_description_string = ''
        for l in item['job_description'] :
            job_description_string = job_description_string + l
        return job_description_string

    def format_job_id(self,item) :
        job_id_string = ''
        for l in item['job_id'] :
            job_id_string = job_id_string + l

        eliminate_char = ['\n','\t']
        for c in eliminate_char :
            job_id_string = job_id_string.replace(c,"")

        return job_id_string

    def format_job_title(self,item) :
        job_title_string = ''
        for l in item['job_title'] :
            job_title_string = job_title_string + l

        ## remove \n \t from the job_title_string
        eliminate_char = ['\n','\t']
        for c in eliminate_char :
            job_title_string = job_title_string.replace(c,"")

        return job_title_string


    def close_spider(self,spider) :
        print("MONGO CLOSE SPIDER")
