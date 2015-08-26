#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'nunosilva, github.com/craked5'


import ujson
import sys
from http import SteamBotHttp


item_exceptions_status = False
item_exceptions = []

print 'HELLO DEAR FRIEND, THANK YOU FOR TRYING THIS SHITTY BOT EHEH NOW LETS BEGIN ASKING THE bIG QUESTIONS :D \n'

inv_url = raw_input("Please paste your inventory url in here (like this "
                    "http://steamcommunity.com/id/craked5/inventory): ")
if raw_input('Do you want to add any item that you dont want to sell? (y/n)? \n') == 'y':
    while item_exceptions_status == False:
        item_exceptions.append(raw_input('Please type the item name (the format is '
                                         'like this: P250 | Supernova (Field-Tested))'))
        if raw_input('Do you want to add any other item to the exceptions (y/n)? ') == 'y':
            print "Ok"
        else:
            item_exceptions_status = True

cookies_json = {}
password_json = {}
setup_cookies = False
setup_password = False
balance = 0
median_prices_list = {}

#----------------------------FUNCTIONS TO SET COOKIES AND PASSWORD TO FILE (Has to restart afet)------------------------
def setPassword():

    username = raw_input('Please type your username: \n')
    password = raw_input('Please type your password: \n')

    password_json['password'] = password
    password_json['username'] = username

    try:
        password_json_file = open('password.json', 'w')
        ujson.dump(password_json, password_json_file)
        password_json_file.close()
    except (IOError,ValueError, TypeError):
        print "Error opening the cookies.json or the password.json file"
        return False

    print "Done, please restart the program or it wont work! \n"

def setCookies():
    wte = raw_input("Please input your webTradeEligibility cookie: \n")
    sessionid = raw_input("Please input your sessionid cookie: \n")
    steamLogin = raw_input("Please input your steamLogin cookie: \n")
    steamLoginSecure = raw_input("Please input your steamLoginSecure cookie: \n")
    sma = raw_input("Please input your steamMachineAuth cookie (name+value together): \n")
    steamRememberLogin = raw_input("Please input your steamRememberLogin cookie: \n")

    cookies_json['webTradeEligibility'] = wte
    cookies_json['sessionid'] = sessionid
    cookies_json['steamLogin'] = steamLogin
    cookies_json['steamLoginSecure'] = steamLoginSecure
    cookies_json['steamMachineAuth'] = sma
    cookies_json['steamRememberLogin'] = steamRememberLogin

    try:
        cookies_json_file = open('cookies.json', 'w')
        ujson.dump(cookies_json, cookies_json_file)
        cookies_json_file.close()
    except IOError:
        print "Error opening cookie.json file"
        return False
    except (ValueError,TypeError):
        print "Error dumping data to cookie.json file"
        return False
#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------INITIALIZE AN INSTANCE OF THE RECENT LISTINGS MODE---------------------------------
def getmedianprice(item):

        list_median_prices = {}

        temp_item_priceover = http.querypriceoverview(item)
        if type(temp_item_priceover) == int:
            print "Erro ao obter preco medio de " + item
            print "Status code da querie: " + str(temp_item_priceover)

        elif type(temp_item_priceover) == bool:
            print "Erro ao obter preco medio de " + item
            print "Status code da querie: " + str(temp_item_priceover)

        elif temp_item_priceover.has_key('median_price'):
            temp_median_price = temp_item_priceover['median_price']
            if isinstance(temp_median_price, basestring):
                temp_median_price = temp_median_price.decode('unicode_escape').encode('ascii','ignore')
                temp_median_price = temp_median_price.replace(',','.').replace('-','0')
                temp_median_price = float(temp_median_price)

        print 'O preco medio de ' + item + ' e: ' + str(temp_median_price)

        return temp_median_price

def getlowestprice(item):
        temp_item_priceover = http.querypriceoverview(item)
        if type(temp_item_priceover) == int:
            print "Erro ao obter preco mais baixo actualmente de " + item
            print "Status code da querie: " + str(temp_item_priceover)
            return False

        if type(temp_item_priceover) == bool:
            return False

        elif temp_item_priceover.has_key('lowest_price'):
            temp_lowest_price = temp_item_priceover['lowest_price']
            if isinstance(temp_lowest_price, basestring):
                temp_lowest_price = temp_lowest_price.decode('unicode_escape').encode('ascii','ignore')
                temp_lowest_price = temp_lowest_price.replace(',','.').replace('-','0')
                temp_lowest_price = float(temp_lowest_price)
                return temp_lowest_price


try:
    cookies_json_file = open('cookies.json', 'r')
    cookies_json = ujson.load(cookies_json_file)

    wte = cookies_json.get('webTradeEligibility').encode('ascii','ignore')
    sma = cookies_json.get('steamMachineAuth').encode('ascii','ignore')
    sessionid = cookies_json.get('sessionid').encode('ascii','ignore')
    sls = cookies_json.get('steamLoginSecure').encode('ascii','ignore')
    sl = cookies_json.get('steamLogin').encode('ascii','ignore')
    srl= cookies_json.get('steamRememberLogin').encode('ascii','ignore')
    setup_cookies = True
except (IOError,ValueError):
    print 'NO COOKIES AND PASSWORD DETECTED \n'
    print 'PLEASE PLEASE SET YOUR COOKIES BEFORE DOING ANYTHING, YOU CAN DO THAT BY ' \
          'TYPING setcookies \n'

try:
    password_json_file = open('password.json', 'r')
    password_json = ujson.load(password_json_file)
    password = password_json.get('password').encode('ascii','ignore')
    username = password_json.get('username').encode('ascii','ignore')
    setup_password = True
except IOError:
    print "PASSWORD NOT DETECTED, PLEASE TYPE setpassword TO SET YOUR PASSWORD \n"

if setup_password and setup_cookies:
    http = SteamBotHttp(wte,sma,sessionid,sls,sl,srl,password,username)

    if http.login() is False:
        print "There was a problem logging you in, maybe check your cookies or your password file and if that does not" \
              "work try to delete them and input everything again! \n"
        print "I'm gonna exit now since there is nothing i can do!"
        sys.exit()
    balance = http.getsteamwalletsite()
    if balance is False:
        print "There was a problem logging you in, maybe check your cookies or your password file and if that does not" \
              "work try to delete them and input everything again! \n"
        print "I'm gonna exit now since there is nothing i can do!"
        sys.exit()
    print "YOU ARE LOGGED IN WITH THE USERNAME: " + username
    print "Your balance is " + str(balance)
else:
    print "Error regarding the cookies or the password, maybe they haven't been setup"
    print "Do you want to set them up now? (y/n) \n"
    if raw_input() == 'y':
        setCookies()
        setPassword()
    else:
        print "OK not now but to continue the program and actually sell something you have to :D"
        sys.exit()

inv = http.getinv(inv_url)

for key in inv['rgInventory']:
    if inv['rgInventory'][key]['classid']+'_'+inv['rgInventory'][key]['instanceid'] in inv['rgDescriptions']:
        inv_id = inv['rgInventory'][key]['classid']+'_'+inv['rgInventory'][key]['instanceid']
        if inv['rgDescriptions'][inv_id]['market_hash_name'] in item_exceptions:
            print "The item " + inv['rgDescriptions'][inv_id]['market_hash_name'] + \
                  " is on the exceptions list so it will not be sold!"
        else:
            if inv['rgDescriptions'][inv_id]['marketable'] is 1:
                print "Preparing to sell the item " + inv['rgDescriptions'][inv_id]['market_hash_name']
                median_price = getmedianprice(inv['rgDescriptions'][inv_id]['market_hash_name'])
                if median_price <= 0.06:
                    price_sell_without_fee = 0.01
                    price_sell = 0.03
                else:
                    lowest_price = getlowestprice(inv['rgDescriptions'][inv_id]['market_hash_name'])
                    if ((float(lowest_price)+(0.02*float(lowest_price)))/float(median_price)) >= 0.95:
                        price_sell = float(lowest_price)
                        price_sell_without_fee = price_sell/1.15
                    else:
                        price_sell = float(median_price*0.95)
                        price_sell_without_fee = price_sell/1.15

                sell_response = http.sellitem(inv['rgInventory'][key]['id'],float(price_sell_without_fee))

                if sell_response[0] is 200:
                    print "Sold the item " + inv['rgDescriptions'][inv_id]['market_hash_name']
                    print "The listed price for the item was " + str(price_sell) + \
                          " and i will receive " + str(price_sell_without_fee) + '\n'
                else:
                    print "I couldn't sell the item " + inv['rgDescriptions'][inv_id]['market_hash_name'] + ' \n'

print "\nThe program is all done! Please check if everything went alright! If not, please use my contacts to send " \
    "feedback! \n"
print "If everything well alright please consider donating as i am a poor college student!"
print "My trade link -> https://steamcommunity.com/tradeoffer/new/?partner=18934038&token=YLpD8hHY"
print "Paypal -> craked5@gmail.com \n"
print "For feedback use:"
print "Github -> github.com/craked5"
print "email -> craked5@gmail.com"
print "twitch -> craked5 \n"
print "Thanks for using this thing :D"



#-----------------------------------------------------------------------------------------------------------------------




