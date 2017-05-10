import scrapy
from splinter import Browser
import logging
import time
import urllib
from scrapy.loader import ItemLoader








class JobItem(scrapy.Item) :

    job_description = scrapy.Field()
    job_id = scrapy.Field()
    job_identifier = scrapy.Field()
    job_title = scrapy.Field()
    job_deadline = scrapy.Field()


class symplicitySpider(scrapy.Spider) :
    logging.getLogger('scrapy').setLevel(logging.WARNING)
    logging.getLogger('scrapy').propagate = False
    name = "makdi"

    global b
    b = Browser('chrome')

    def start_requests(self) :

        b.visit('https://cas.sfu.ca/cas/login?service=http%3A%2F%2Fsfu-csm.symplicity.com%2Fsso%2Fstudents%2Flogin') ## symplicity login
        b.find_by_id('username').first.fill(str(self.username))
        b.find_by_id('password').first.fill(self.password)
        b.find_by_value('Sign In').first.click()
                #loged inw
        cookiesFromSplinter= b.cookies.all()
                #print("response from splinter = ",str(b.url))
        cookie_file = open('cookies.txt','w')
        cookie_file.write(str(cookiesFromSplinter))


        #time.sleep(2)
        print("GOING TO MAIN PAGE NOW....")
        yield scrapy.Request(url="https://sfu-csm.symplicity.com/students/index.php?s=home",callback=self.parse_main_page,cookies=cookiesFromSplinter)

    def parse_main_page(self,response) :


    #    time.sleep(2)
        print("GOING TO JOB POSTINGS PAGE NOW....")
        #b.visit("https://sfu-csm.symplicity.com/students/index.php?s=jobs&ss=jobs&mode=list")
        yield scrapy.Request(url="https://sfu-csm.symplicity.com/students/index.php?s=jobs&ss=jobs&mode=list",callback=self.parse_job_search_page)

    def parse_job_search_page(self,response) :

        #time.sleep(3)
        job_links = response.css('#_list_form > ul > li > div.list-item-body > div.list-item-title > a::attr(href)').extract()

        base_url = "https://sfu-csm.symplicity.com/students/index.php"
        for job in job_links :
            ##time.sleep(5)
            full_link = base_url + job
            print("FULL LINK:",full_link)

            yield scrapy.Request(url=str(full_link),callback=self.parse_job)

    def parse_job(self,response) :

        print("INSIDE JOB")



        job_description_html = "#frame > div.page-main > div > div > div > div.job_review_wrap.form-layout.has-sidebar > div > div.form-col > div.job_display > div.job_display_desc > div.job_description::text"
        job_id_html = "#frame > div.page-main > div > div > div > div.job_review_wrap.form-layout.has-sidebar > div > div.form-col > div.job_display > div.job-bfields > div:nth-child(2) > div.widget.jobfld-visual_id::text"
        job_identifier = response.url[response.url.find('id'):response.url.find('&s')+1]
        job_attachment_link_html = "div#dnf_class_values_job__attachment__0__preview__widget > a::attr(href)"
        job_title_html = "#frame > div.page-main > div > div > div > div.job_review_wrap.form-layout.has-sidebar > div > div.form-col > div.job_display > div.visual-header-info.dark-theme > div > div.job-emp-info > h1::text"
        job_deadline_html = "div#edfab414adccd8b67f7727e3ae03b85b"
        #job_attachment_download_link = "https://sfu-csm.symplicity.com" + str(job_attachment_link)

        job_loader = ItemLoader(item=JobItem(),response=response)
        job_loader.add_css('job_description',job_description_html)
        job_loader.add_css('job_id',job_id_html)
        job_loader.add_value('job_identifier',job_identifier)
        job_loader.add_css('job_title',job_title_html)
        job_loader.add_css('job_deadline',job_deadline_html)
        #print("DESCRIPTION:",job_loader.get_collected_values('job_description'))
        #print("ID",job_loader.get_collected_values('job_id'))
        #print("IDENTIFIER",job_loader.get_collected_values('job_identifier'))
        #print("LINK",job_loader.get_collected_values('job_attachment_link'))
        #print("TITLE",job_loader.get_collected_values('job_title'))
        return job_loader.load_item()
        #rint("DONWLOAD_LINK:,",job_attachment_download_link)
        #file_name, headers = urllib.request.urlretrieve(job_attachment_download_link)
        #print("FILENAME: ",file_name)

        b.quit()
#edfab414adccd8b67f7727e3ae03b85b
