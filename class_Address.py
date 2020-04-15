# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:57:29 2020

@author: duanyiting
"""
class Address:
    def address(country,province,city,street,ip):
        print("%s%s省%s市%s邮编：%s\n"%(country,province,city,street,ip))
country=input()
province=input()
city=input()
street=input()
ip=input()
Address.address(country,province,city,street,ip)