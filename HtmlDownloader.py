# -*- coding:UTF-8 -*-
import requests


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        print "开始爬取:%s" % url
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        headers = {'User-Agent':user_agent}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None