#env=/usr/bin/python
#coding=utf-8

import WBParser
import WeiboLogin

if __name__ =='__main__':
    userName, passWord = 'huzhan8787@qq.com', 'HZ100200123';
    ROILabel = ['oid', 'onick', 'sex'];
    weiboLogin = WeiboLogin.WeiboLogin(userName, passWord);
    if(weiboLogin.Login() == True):
        print "login successfully!";
    else:
        print "login failed!";
    htmlLink = 'http://weibo.com/2177228323/C5KB4bOel?from=page_1005052177228323_profile&wvr=6&mod=weibotime&type=comment';
    opener = weiboLogin.getOpener();
    wbParser = WBParser.WBParser(htmlLink, opener);
    medianUser = wbParser.fetchScript();
    print '\n';
    for user_i in medianUser:
        for key in ROILabel:
            print user_i[key];
