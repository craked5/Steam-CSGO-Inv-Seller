#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'nunosilva, github.com/craked5'

from bs4 import BeautifulSoup
import requests as req
import json
import time
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from http_util import Httpdata

class SteamBotHttp:

    def __init__(self,wte,sma,sessionid,sls,sl,srl,password,username):
        self.httputil = Httpdata(wte,sma,sessionid,sls,sl,srl,password,username)
        self.down_state = 0
        self.host = 'steamcommunity.com'
        self.pre_host_normal = 'http://'
        self.pre_host_https = 'https://'
        self.market = '/market'
        self.mylistings = '/mylistings/'
        #currency=3/2003 == euro
        self.item_price_viewer = '/priceoverview/?currency=3&appid=730&market_hash_name='
        self.recent_listed = '/recent/?country=PT&language=english&currency=3'

        #TESTE RECENT_LISTED -APAGAR DEPOIS
        self.recent_listed_countrys1 = '/recent/?country='
        self.recent_listed_countrys2 = '&language=english&currency=3'

        self.complete_url_item = self.pre_host_normal+self.host+self.market+self.item_price_viewer
        self.complete_url_recent = self.pre_host_normal+self.host+self.market+self.recent_listed
        self.sell_item_url = self.pre_host_https+self.host+self.market+'/sellitem/'
        self.buy_item_url_without_listingid = self.pre_host_https+self.host+self.market+'/buylisting/'
        self.render_item_url_first_part = self.pre_host_normal+self.host+self.market+'/listings/730/'
        self.render_item_url_sencond_part = '/render/?currency=3'
        self.recent_compare = {}

    def login(self):

        try:
            donotcache = self.now_milliseconds()

            self.httputil.rsa_data['donotcache'] = donotcache
            self.httputil.login_data['donotcache'] = donotcache

            temp_rsa = req.post('https://steamcommunity.com/login/getrsakey/', headers=self.httputil.rsa_headers,
                                data=self.httputil.rsa_data)

            temp_ras_good = json.loads(temp_rsa.content)
            self.httputil.login_data['rsatimestamp'] = temp_ras_good['timestamp']
            mod = long(temp_ras_good['publickey_mod'], 16)
            exp = long(temp_ras_good['publickey_exp'], 16)
            rsa_key = RSA.construct((mod, exp))
            rsa = PKCS1_v1_5.PKCS115_Cipher(rsa_key)
            encrypted_password = rsa.encrypt(self.httputil.password)
            encrypted_password = base64.b64encode(encrypted_password)
            self.httputil.login_data['password'] = encrypted_password

            temp_dologin = req.post('https://steamcommunity.com/login/dologin/', headers=self.httputil.rsa_headers,
                                    data=self.httputil.login_data)

            temp_dologin_good = json.loads(temp_dologin.content)
            self.httputil.transfer_data['steamid'] = temp_dologin_good['transfer_parameters']['steamid']
            self.httputil.transfer_data['token'] = temp_dologin_good['transfer_parameters']['token']
            self.httputil.transfer_data['auth'] = temp_dologin_good['transfer_parameters']['auth']
            self.httputil.transfer_data['remember_login'] = temp_dologin_good['transfer_parameters']['remember_login']
            self.httputil.transfer_data['token_secure'] = temp_dologin_good['transfer_parameters']['token_secure']

            req.post('https://store.steampowered.com/login/transfer', headers=self.httputil.transfer_headers
                                     ,data=self.httputil.transfer_data)
        except:
            return False

    def now_milliseconds(self):
        self.donotcache = int(time.time() * 1000)

    def querypriceoverview(self,item):
        try:
            steam_response = req.get(self.complete_url_item + item, headers=self.httputil.headers_item_priceoverview,timeout=15)
            if steam_response.status_code == 200:
                try:
                    item_temp_str_no_uni = steam_response.content.decode('unicode_escape').encode('ascii','ignore')
                    item_temp = json.loads(item_temp_str_no_uni)
                except ValueError:
                    return steam_response.status_code, steam_response.content
                return item_temp
            else:
                return steam_response.status_code
        except req.Timeout:
            return False


    def getinv(self,inv_url):
        try:
            temp_inv = req.get(inv_url+'/json/730/2/')
            array = json.loads(temp_inv.content)

            return array
        except:
            return False

    #price = ao preco que eu quero receber
    #price vem em float
    def sellitem(self,assetid,price):

        list_return = []
        price_temp = price * 100
        price_temp = round(price_temp)

        self.httputil.data_sell['assetid'] = int(assetid)
        self.httputil.data_sell['price'] = int(price_temp)

        temp = req.post(self.sell_item_url, data=self.httputil.data_sell, headers=self.httputil.headers_sell)

        list_return.append(temp.status_code)
        list_return.append(temp.content)
        list_return.append(int(price_temp))

        return list_return

    def getsteamwalletsite(self):
        try:
            temp = req.get('http://steamcommunity.com/market/',headers=self.httputil.headers_wallet)
            if temp.status_code is 200:
                soup = BeautifulSoup(temp.content,'html.parser')
                balance_soup = soup.find('span',{'id':'marketWalletBalanceAmount'})

                if balance_soup is not None:
                    balance_soup = balance_soup.get_text()
                    balance_str = balance_soup.encode('ascii','ignore').replace(',','.')

                    return float(balance_str)
                else:
                    return False
            else:
                return False
        except:
            return False

#-----------------------------------------AUX FUNCTIONS------------------------------------------------------------------