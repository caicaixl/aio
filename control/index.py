# -*- coding: utf-8 -*-
#__author__ = 'cai'
#__data__ : 2019-05-22 10:48
# import os

from aiohttp import web

from setting import TEMPLATES


class Home:
    def __init__(self):
        pass

    # @aiohttp_jinja2.template('templates/html/csv.html')
    # async def login(self,request):
    #     # idxHtml = TEMPLATES['info'].html('login.html')
    #     # resp = web.Response(body=idxHtml)
    #     # resp.headers['content-type'] = 'text/html'
    #     # return



    # async def respCsv(self,request):
    #     la = self.loginAuthentication(request)
    #     if not la:
    #         resp = web.Response(body=f'<p>cookie验证错误</p><p><a hred="/html/login.html">返回登录页面</a></p>')
    #         resp.headers['content-type'] = 'text/html'
    #         return resp
    #     name = request.match_info.get('name')
    #     _path = os.path.join(ALLPHONENUMPATH,name)
    #     logger.info(f'下载{_path}')
    #     r = web.FileResponse(f'{_path}')
    #     r.enable_compression()
    #     return r

    async def home(self, request):
        data = TEMPLATES.html('music.html')
        resp = web.Response(body=data)
        resp.headers['content-type'] = 'text/html'
        return resp

    async def xxl(self, request):
        data = TEMPLATES.html('xxl.html')
        resp = web.Response(body=data)
        resp.headers['content-type'] = 'text/html'
        return resp

    async def music_json(self, request):
        data = TEMPLATES.jsons('music.json')
        resp = web.Response(body=data)
        resp.headers['content-type'] = 'application/json'
        return resp

    # async def login(self,request):
    #     data = await request.post()
    #     name = data['username']
    #     password = data['password']
    #     if name != "cccxl" or password != "c91034":
    #         logger.info(f'账号密码错误,{name}---{password}')
    #         data = {'status': 401, 'cookie': '','data':'密码错误'}
    #         return web.json_response(data)
    #     logger.info('login账号密码验证成功')
    #     data = {'status': 200, 'cookie': 'key=cccxlc91034','data':'登陆成功'}
    #     return web.json_response(data)


    # def loginAuthentication(self,request):
    #     if request.cookies.get('key', '') != 'cccxlc91034':
    #         return web.json_response({'status':401,'log':'cookie验证出错'})
    #     return 1