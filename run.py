# -*- coding: utf-8 -*-
#__author__ = 'cai'
#__data__ : 2019-05-22 10:43

from route import loop, init

loop.run_until_complete(init())
loop.run_forever()