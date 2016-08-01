# -*- coding: utf-8 -*-
"""
Created on Mon Aug 01 17:33:31 2016

@author: Administrator
"""
from scrapy.spiders import Spider
from scrapy.selector import Selector
from dirbot.items import Website

class duonan(Spider):
    name="looker"
    start_ursl="http://ieeexplore.ieee.org/Xplore/home.jsp"
    allowed_domains = ['ieeexplore.ieee.org']
    
def parse(self,response):
    sel = Selector(response)
    sites = sel.xpath('//*[@id="mostDownloadedArticlesTab"]/ul/li/')    
    items=[]
    

    
    for site in sites:
        item=Website()
        item['one']=site.xpath('/a.text()').extarct()
        item['second']=site.xpath('/a.text()')
 
        items.append(item)
        return items    
    
    #LayoutWrapper > div:nth-child(11) > div:nth-child(2)