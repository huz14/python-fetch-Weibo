#env=/usr/bin/python
#coding=utf-8

import bs4
import os
import time
import urllib
import urllib2
import re
import cookielib
import WeiboLogin

class WBParser(object):
    def __init__(self, URL, opener, ROILabel = ['oid', 'onick', 'sex']):
        self.opener = opener;
        response = self.opener.open(URL);
        self.pageSoup = bs4.BeautifulSoup(response.read());
        self.ROILabel = ROILabel;
        
    def fetchHeader(self):
        headScripts = self.pageSoup.head.find_all('script');
        #print headScripts;
        for headScript_i in headScripts:
            speStr = "$CONFIG";
            if speStr in headScript_i.string:
                configs = headScript_i.string.split('{};')[-1];
                #print configs;
                configs = configs.replace('$CONFIG[','');
                configs = configs.replace(']','');
                #print configs;
                tagList = [config_i.strip().strip('\n') for config_i in configs.split(';')];
                ROIData = dict([(tag_i.split('=')[0].strip("'"),tag_i.split('=')[1].strip("'"))\
                                for tag_i in tagList if tag_i.split('=')[0].strip("'") in self.ROILabel]);
                return ROIData;
    def fetchScript(self):
        for script_i in self.pageSoup.find_all('script'):
            script_i_split = str(script_i).split('{')[-1];
            if '"ns":"pl.content.weiboDetail.index"' in script_i_split:
                text = script_i_split.replace('\/','/');
                text = text.split('"html":')[-1].split('}')[0];
                text = text.replace('&lt;','<');
                text = text.replace('&gt;','>');
                text = text.replace('\\"', '"');
                script = bs4.BeautifulSoup(text);
                WBTexts = script.find_all('a', attrs = {'extra-data':'type=atname'});
                hrefs = [];
                for text_i in WBTexts:
                    text_i = text_i.prettify();
                    hrefs.append(text_i.split('href="')[-1].split('" render')[0]);
                ret = [];
                for href_i in hrefs:
                    response = self.opener.open(href_i);
                    curParser = WBParser(href_i, self.opener);
                    ret.append(curParser.fetchHeader());
                return ret;
