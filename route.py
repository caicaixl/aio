# -*- coding: utf-8 -*-
#__author__ = 'cai'
#__data__ : 2019-05-22 10:16
import asyncio
from pathlib import Path

import aiohttp_jinja2
import jinja2
from aiohttp import web

from control.index import  Home
from setting import  logger

loop = asyncio.get_event_loop()

async def init():
    app = web.Application(loop=loop,logger=logger)
    here = Path(__file__).resolve().parent
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(here)))

    CONTORLLER = Home()
    # app.router.add_get("/csv/{name}", CONTORLLER.respCsv)
    # app.router.add_post("/home/phone", CONTORLLER.verifyjson)
    # app.router.add_post("/", CONTORLLER.login)
    app.router.add_get("/",CONTORLLER.home)
    app.router.add_get("/xxl",CONTORLLER.xxl)
    app.router.add_get("/music-json",CONTORLLER.music_json)
    app.router.add_static('/css/',path='templates/css',name='css')
    app.router.add_static('/js/',path='templates/js',name='js')
    app.router.add_static('/html/',path='templates/html',name='html')
    app.router.add_static('/static/',path='static',name='static')
    app.router.add_static('/bitmap/',path='static/bitmap',name='bitmap')
    app.router.add_static('/audio/',path='static/audio',name='audio')
    app.router.add_static('/fonts/',path='templates/fonts',name='fonts')
    # app.router.add_resource('/audio/',path='static/audio',name='audio')
    # app.router.add_static('/dream',path='static/audio/dream',name='audio')

    app_runner = web.AppRunner(app)
    await app_runner.setup()
    server = await loop.create_server(app_runner.server, '127.0.0.1', '1901')
    logger.info(f'server started at http://127.0.0.1:1901')
    # logger.info(f'server started at http://0.0.0.0:15247')
    return server