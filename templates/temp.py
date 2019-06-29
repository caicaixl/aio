# -*- coding: utf-8 -*-
#__author__ = 'cai'
#__data__ : 2019-05-22 11:09
import os

class Temp:
    def __init__(self):
        path = os.path.dirname(__file__)
        self.jsPath = os.path.join(path,'js')
        self.cssPath = os.path.join(path,'css')
        self.htmlPath = os.path.join(path,'html')
        self.jsonsPath = os.path.join(path,'Jsons')

    def js(self,name):
        thiePath = os.path.join(self.jsPath,name)
        with open(thiePath,'r',encoding='utf-8') as fp:
            data = fp.read()
        return data

    def css(self,name):
        thiePath = os.path.join(self.cssPath,name)
        with open(thiePath,'r',encoding='utf-8') as fp:
            data = fp.read()
        return data

    def html(self,name):
        thiePath = os.path.join(self.htmlPath,name)
        with open(thiePath,'r',encoding='utf-8') as fp:
            data = fp.read()
        return data

    def jsons(self,name):
        thiePath = os.path.join(self.jsonsPath,name)
        with open(thiePath,'r',encoding='utf-8') as fp:
            data = fp.read()
        return data




