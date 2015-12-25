#env = /usr/bin/python
#encoding = utf-8

import urllib2
import cookielib  
import WeiboEncode
import WeiboSearch
 

class WeiboLogin:
    def __init__(self, user, pwd, enableProxy = False):
        #"init WeiboLogin enableProxy"
        print "Initializing WeiboLogin..."
        self.userName = user;
        self.passWord = pwd;
        self.enableProxy = enableProxy;

        self.serverUrl = "http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.11)&_=1379834957683"
        self.loginUrl = "http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.11)"
        self.postHeader = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0'}
	
    def Login(self):
        self.EnableCookie(True)#cookie

        serverTime, nonce, pubkey, rsakv = self.GetServerTime()#
        postData = WeiboEncode.PostEncode(self.userName, self.passWord, serverTime, nonce, pubkey, rsakv)#
        print "Post data length:\n", len(postData)  
        req = urllib2.Request(self.loginUrl, postData, self.postHeader)
        print "Posting request..."
        #result = urllib2.urlopen(req)#parse sina weibo login step
        result = self.opener.open(req);
        text = result.read()
        print text;
        try:
            loginUrl = WeiboSearch.sRedirectData(text)#parse redirection
            urllib2.urlopen(loginUrl)
        except:
            print 'Login error!'
            return False

        print 'Login sucess!'
        return True
	
    def EnableCookie(self, enableProxy):

        #cookiejar = cookielib.LWPCookieJar()#cookie
        cookiejar = cookielib.CookieJar();
        cookie_support = urllib2.HTTPCookieProcessor(cookiejar)  
        '''if enableProxy:
                proxy_support = urllib2.ProxyHandler({'http':'http://xxxxx.pac'})#
                opener = urllib2.build_opener(proxy_support, cookie_support, urllib2.HTTPHandler)
                print "Proxy enabled"
        else:'''
        #self.opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        self.opener = urllib2.build_opener(cookie_support);
        urllib2.install_opener(self.opener)#cookie opener
        
    def loginHTML(self, htmlLink):
        return self.opener.open(htmlLink);
    def getOpener(self):
	    return self.opener;
    
    def GetServerTime(self):
            "Get server time and nonce, which are used to encode the password"

            print "Getting server time and nonce..."
            serverData = urllib2.urlopen(self.serverUrl).read()#
            print serverData  
            try:
                    serverTime, nonce, pubkey, rsakv = WeiboSearch.sServerData(serverData)#get serverTime nonce
                    return serverTime, nonce, pubkey, rsakv
            except:
                    print 'Get server time & nonce error!'
                    return None
 
