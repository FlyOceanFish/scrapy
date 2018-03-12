# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):
    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'lxml')
        new_urls = self.__get_new_urls(page_url, soup)
        new_data = self.__get_new_data(page_url, soup)
        print "爬取结束:%s" % page_url
        return new_urls, new_data

    def __get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all("a", href=re.compile(r'/item/(%\w{2}){1,}'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def __get_new_data(self, page_url, soup):
        data = {}
        data['url'] = page_url
        soup.find('dd')
        return data
