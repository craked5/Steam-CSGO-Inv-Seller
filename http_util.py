#!/usr/bin/env python
# -*- coding: utf-8 -*-
_author__ = 'nunosilva, github.com/craked5'

class Httpdata:

    def __init__(self,wte,sma,sessionid,sls,sl,srl,password,username):
        self.sessionid = sessionid
        self.steamLogin = sl
        self.steamLoginSecure = sls
        self.webTradeEligibility = wte
        self.steamMachineAuth = sma
        self.password = password
        self.steamRememberLogin = srl
        self.username = username

        self.headers_wallet = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip,deflate,sdch",
            "Accept-Language": "pt-PT,pt;q=0.8,en-US;q=0.6,en;q=0.4,fr;q=0.2,es;q=0.2",
            'Connection':'keep-alive',
            'Cookie':'Steam_Language=english; '
                     '730_17workshopQueueTime=1432014476; '
                     'recentlyVisitedAppHubs=220%2C316950%2C440%2C72850%2C295110%2C730; '
                     'sessionid='+self.sessionid+';'
                     'steamCountry=PT%7Ceadce223f9093afc9f086e613abc8402; '
                     'strInventoryLastContext=730_2; '
                     'steamLogin='+self.steamLogin+'; '
                     'timezoneOffset=3600,0; '
                     'webTradeEligibility='+self.webTradeEligibility+'; '
                     'tsTradeOffersLastRead=1435052082',
            'DNT':1,
            'Host':'steamcommunity.com',
            'HTTPS':1,
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/43.0.2357.130 Safari/537.36'
        }

        self.headers_item_priceoverview = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip,deflate,sdch",
            "Accept-Language": "pt-PT,pt;q=0.8,en-US;q=0.6,en;q=0.4,fr;q=0.2,es;q=0.2",
            'Cache-Control':'no-cache',
            'Connection':'keep-alive',
            'Cookie':'Steam_Language=english; '
                     '730_17workshopQueueTime=1432014476; '
                     'recentlyVisitedAppHubs=220%2C316950%2C440%2C72850%2C295110%2C730; '
                     'sessionid='+self.sessionid+';'
                     'steamCountry=PT%7Ceadce223f9093afc9f086e613abc8402; '
                     'strInventoryLastContext=730_2; '
                     'steamLogin='+self.steamLogin+'; '
                     'timezoneOffset=3600,0; '
                     'webTradeEligibility='+self.webTradeEligibility,
            'DNT':1,
            'Host':'steamcommunity.com',
            'Upgrade-Insecure-Requests':1,
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/43.0.2357.130 Safari/537.36'
        }

        self.headers_sell = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip,deflate,sdch",
            "Accept-Language": "pt-PT,pt;q=0.8,en-US;q=0.6,en;q=0.4,fr;q=0.2,es;q=0.2",
            "Host": "steamcommunity.com",
            'Cookie': self.steamMachineAuth+'; '
                      'Steam_Language=english; '
                      '730_17workshopQueueTime=1432014476; '
                      'steamRememberLogin='+self.steamRememberLogin+'; '
                      'recentlyVisitedAppHubs=220%2C316950%2C440%2C72850%2C295110%2C730; '
                      'sessionid='+self.sessionid+';'
                      'webTradeEligibility='+self.webTradeEligibility+'; '
                      'steamLogin='+self.steamLogin+'; '
                      'steamLoginSecure='+self.steamLoginSecure+'; '
                      'strInventoryLastContext=730_2; '
                      'tsTradeOffersLastRead=1434610877; '
                      'timezoneOffset=3600,0',
            "Referer": "https://steamcommunity.com/id/craked5/inventory",
            "Origin": "https://steamcommunity.com",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/43.0.2357.124 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }

        self.rsa_headers = {
            'Accept':'text/javascript, text/html, application/xml, text/xml, */*',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'pt-PT,pt;q=0.8,en-US;q=0.6,en;q=0.4,fr;q=0.2,es;q=0.2',
            'Connection':'keep-alive',
            'Content-Length':44,
            'Content-type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': self.steamMachineAuth+'; '
                     'Steam_Language=english; '
                     '730_17workshopQueueTime=1432014476; '
                     'recentlyVisitedAppHubs=220%2C316950%2C440%2C72850%2C295110%2C730; '
                     'sessionid='+self.sessionid+';'
                     'steamCountry=PT%7C90d987902b02ceec924245352748dc71; '
                     'strInventoryLastContext=730_2; '
                     'timezoneOffset=3600,0',
            'CSP':'active',
            'DNT':1,
            'Host':'steamcommunity.com',
            'Origin':'https://steamcommunity.com',
            'Referer':'https://steamcommunity.com/login/home/?goto=0',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/43.0.2357.130 Safari/537.36',
            'X-Prototype-Version':1.7,
            'X-Requested-With':'XMLHttpRequest'
        }

        self.transfer_headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'pt-PT,pt;q=0.8,en-US;q=0.6,en;q=0.4,fr;q=0.2,es;q=0.2',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Content-Length':184,
            'Content-Type':'application/x-www-form-urlencoded',
            'Cookie':'browserid=740048883567382728; '
                     +self.steamMachineAuth+'; '
                     'lastagecheckage=1-January-1981; '
                     'recentapps=%7B%22362890%22%3A1430846718%2C%22295110%22%3A1430761022%2C%22252490%22%3A1430173804%2C'
                     '%22271590%22%3A1428971636%2C%22290930%22%3A1427354378%2C%22353560%22%3A1426972561%2C%22262390%22%3'
                     'A1424562332%2C%22239140%22%3A1422402521%7D; '
                     'timezoneOffset=3600,0; '
                     'steamCountry=PT%7Ceadce223f9093afc9f086e613abc8402; '
                     'steamLogin='+self.steamLogin+'; '
                     'steamLoginSecure='+self.steamLoginSecure+'; ',
            'DNT':1,
            'Host':'steamcommunity.com',
            'Origin':'https://steamcommunity.com',
            'Referer':'https://steamcommunity.com/login/home/?goto=0',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
        }

        #price = preco que eu quero receber = price+fee_price
        self.data_sell = {
            "sessionid" : self.sessionid,
            "appid" : 730,
            "contextid" : 2,
            "assetid" : 2624120824,
            "amount" : 1,
            "price" : 1000
        }

        self.rsa_data = {
            'username': self.username,
            'donotcache': 0
        }

        self.login_data = {
            'password': '',
            'username': self.username,
            'twofactorcode':'',
            'emailauth':'',
            'loginfriendlyname':'',
            'captchagid':-1,
            'captcha_text':'',
            'emailsteamid':'',
            'rsatimestamp': '',
            'remember_login':'false',
            'donotcache': 0
        }

        self.transfer_data = {
            'steamid': 0,
            'token':'',
            'auth':'',
            'remember_login':'',
            'token_secure':''
        }

