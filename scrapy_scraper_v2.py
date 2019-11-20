# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 08:46:09 2019

@author: Rishabh
"""
import scrapy
import os
import re
import sys
from scrapy.selector import Selector 
from scrapy.crawler import CrawlerProcess
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from flashtext import KeywordProcessor
import logging

DOMAIN_DICT = { "Healthcare" : ["Health","Provider","Medicare","Coverage","Dental","Insurance","medicaid","pharmaceutical","services","preventive"],
                "Finance" : ["Invest","Debt","Mortgage","Loans","Economy","Finance","fund","banking","government","credit"],
                "Media" : ["News","Sports","Movies","Subscriber","Billing","Media","broadcast","advertising","music","TV"],
                "Ecommerce" : ["Deals","Coupons","Giftcards","Customers","Delivery","Buy","Sell","merchandise","electronics","fashion"],
                "Telecom" : ["Wireless","Telecommunications","Mobile","Internet","iphone","cable","devices","contact","bandwidth","network"],
                "Technology" : ["Cloud","Big Data","Artificial Intelligence","PHP","Java","Python","Android","Digital","Software","Automation"]
}



 
def searchkeywords(key,values,words):
	keyword_processor = KeywordProcessor()
	for term_1 in values:
		keyword_processor.add_keyword(term_1)
		keywords_found = keyword_processor.extract_keywords(str(words))
		
	#print("Set correspoding to " + key + str(set(keywords_found)))
	return list(set(keywords_found)),key



class Myspider(scrapy.Spider):
    name = "search"
    #print(str(sys.argv[1]))
    search = str(sys.argv[1]).replace(' ','+').lower()
    url = 'https://www.google.co.in/search?q=' + search
    #print(url)

    start_urls = [url]
    
    def __init__(self):
        logging.getLogger('scrapy').propagate = False
    
    def parse(self,response):
        text_from_html = []
        
        html = response.xpath('//div[@class="g"]')[0].extract()
        print("++++++++")
        
        print("++++++++")
        resultset = Selector(text=html).xpath('//h3[@class="r"]//a[@href]')[0].xpath("@href").extract()
        print("++++++++")
        result = str(resultset).split('/url?q=')[1].split('&')[0]
       
        page = requests.get(result)
        html_cont = page.content
        soup = BeautifulSoup(html_cont,'html.parser')
        for script in soup(["script", "style"]):
            script.decompose() 
        texts = soup.get_text()
        
        lines = (line.strip() for line in texts.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        texts = '\n'.join(chunk for chunk in chunks if chunk)
        text = list(map(str,texts.split()))
        
        stop_words = set(stopwords.words('english'))
        #text_from_html.append[texts]
        words = [w for w in text if not w in stop_words]
        #print(words)
        
        cnt_list = []
        key_list = []


        for key,values in DOMAIN_DICT.items():
        	ret_set,key = searchkeywords(key,values,words)
        	#print(key)
        	

        	cnt_list.append(len(ret_set))
        	key_list.append(key)

        #print(cnt_list)
        ot_dict = dict(zip(key_list,cnt_list))
        

        result = {
        "Org name" : self.search ,
        "Domain Name" : result ,
        "Field of work" : max(ot_dict,key=ot_dict.get) ,
        "Confidence Score" : int(ot_dict[max(ot_dict,key=ot_dict.get)])/len(DOMAIN_DICT[max(ot_dict,key=ot_dict.get)]) 
        }

        print (result)



process = CrawlerProcess({
    'USER_AGENT' : 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(Myspider)
process.start()
#

    
