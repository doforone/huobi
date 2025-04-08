# -*- coding: UTF-8 -*-

from urllib import request, parse
from urllib.parse import quote

import time
import json
import pyodbc

from PIL import Image, ImageDraw,ImageFont
import random

#============================时间到强制结束线程
import threading
import inspect
import ctypes

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
 
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

#=============================

def get_htmll(urll,dataa=None):     #请求页面，这个函数要用线程，长时间不响应就杀死线程，参数5秒有时不起作用
    print(urll)
    if 1:
        global htmll
        headers = {'user-agent': 'Chrome/73.0.3683.86 Safari/537.36'}
        try:
            req = request.Request(urll, headers=headers)
            with request.urlopen(req, timeout=125) as resp:
                htmll=resp.read().decode("utf-8")
        except Exception as e:
            htmll=""


if __name__ == "__main__":
    htmll=""

    aaa=["5min", "15min", "30min", "60min", "4hour", "1day"]

    bbb=["usdthusd","nasusdt","hb10usdt","omgusdt","btsusdt","ctxcusdt",\
         "lbausdt","thetausdt","iotausdt","ontusdt","ocnusdt","gntusdt",\
         "iostusdt","adausdt","neousdt","smtusdt","topusdt","bsvusdt",\
         "dtausdt","cmtusdt","btmusdt","ltcusdt","eosusdt","actusdt",\
         "ttusdt","socusdt","elausdt","hptusdt","gxcusdt","itcusdt",\
         "ruffusdt","etcusdt","hitusdt","nulsusdt","steemusdt","nanousdt",\
         "xmrusdt","irisusdt","hcusdt","zecusdt","dashusdt",\
         "zrxusdt","btcusdt","bttusdt","cvcusdt","zilusdt","paiusdt",\
         "dcrusdt","sntusdt","storjusdt","bchusdt","rsrusdt","trxusdt",\
         "xrpusdt","lambusdt","htusdt","aeusdt","kanusdt","wavesusdt",\
         "wiccusdt","linkusdt","qtumusdt","newusdt","mdsusdt","atomusdt",\
         "xlmusdt","letusdt","vetusdt","bixusdt","dogeusdt","elfusdt",\
         "xemusdt","ethusdt"]

    bbb+=["uniusdt","bagsusdt","mdxusdt","dotusdt","filusdt"]
    bbb+=["ftiusdt","swftcusdt","xmxusdt","btsusdt","hitusdt","dhtusdt","yeeusdt","lolusdt","nbsusdt"]
    
    aa="1day"
    bbb=['omgusdt', 'irisusdt', 'vidyusdt', 'uniusdt', 'sntusdt', 'cvpusdt', \
         'wiccusdt', 'linkusdt', 'ruffusdt', 'btsusdt', 'htusdt', 'avaxusdt', \
         'thetausdt', 'woousdt', 'wtcusdt', 'dhtusdt', 'lbausdt', \
         'elfusdt', 'dtausdt', 'swrvusdt', 'gnxusdt', 'bhdusdt', 'kavausdt', \
         'chzusdt', 'uipusdt', 'topusdt', 'hotusdt', 'pvtusdt', 'loomusdt', \
         'mxcusdt', 'zrxusdt', 'firousdt', 'hb10usdt', 'kncusdt', 'mcousdt', \
         'ltcusdt', 'mlnusdt', 'xrpusdt', 'nulsusdt', 'wxtusdt', 'btcusdt', \
         'blzusdt', 'dcrusdt', 'swftcusdt', 'yfiiusdt', 'balusdt', 'zenusdt', \
         'dashusdt', 'trxusdt', 'dockusdt', 'borusdt', 'pearlusdt', 'linausdt', \
         'antusdt', 'hptusdt', 'cnnsusdt', 'maticusdt', 'ethusdt', 'xmxusdt', \
         'letusdt', 'aacusdt', 'titanusdt', 'cmtusdt', 'ksmusdt', 'xmrusdt', \
         'grtusdt', 'kanusdt', 'zilusdt', 'iotausdt', 'bttusdt', 'lendusdt', \
         'snxusdt', 'itcusdt', 'ektusdt', 'vetusdt', 'etcusdt', 'ontusdt', \
         'hitusdt', 'forusdt', 'nodeusdt', 'lambusdt', 'gtusdt', \
         'xrtusdt', 'actusdt', 'badgerusdt', 'bchausdt', 'lxtusdt', 'valueusdt', \
         'bandusdt', 'dfusdt', 'astusdt', 'oxtusdt', 'arusdt', 'aeusdt', \
         'nhbtcusdt', 'elausdt', 'wavesusdt', 'glmusdt', 'bixusdt', 'arpausdt', \
         'steemusdt', 'dogeusdt', 'eosusdt', 'hcusdt', 'dacusdt', 'crvusdt', \
         'creusdt', 'qtumusdt', 'rsrusdt', 'achusdt', 'akrousdt', 'nasusdt', \
         'umausdt', 'filusdt', 'socusdt', 'ckbusdt', 'frontusdt', 'batusdt', \
         'ringusdt', 'ogousdt', 'rvnusdt', 'bsvusdt', 'dkausdt', 'nexousdt', \
         'hbarusdt', 'smtusdt', 'mkrusdt', 'renusdt', 'bntusdt', 'manausdt', \
         'atpusdt', 'yeeusdt', 'phausdt', 'venusdt', 'gxcusdt', 'emusdt', \
         'botusdt', 'pondusdt', 'reefusdt', 'daiusdt', 'sandusdt', 'adausdt', \
         'hbcusdt', 'nbsusdt', 'crousdt', 'lolusdt', 'nestusdt', 'fsnusdt', \
         'ctxcusdt', 'xemusdt', 'compusdt', 'hiveusdt', 'iostusdt', 'stptusdt', \
         'egtusdt', 'uuuusdt', 'sklusdt', 'sunusdt', 'ognusdt', 'cvcusdt', \
         'skmusdt', 'ttusdt', 'ftiusdt', 'utkusdt', 'ocnusdt', 'wnxmusdt', \
         'mtausdt', 'iotxusdt', 'abtusdt', 'gofusdt', 'polsusdt', 'icxusdt', \
         'waxpusdt', 'nsureusdt', 'nanousdt', 'storjusdt', 'xlmusdt', 'oneusdt', \
         'mxusdt', 'bchusdt', 'fisusdt', 'yfiusdt', 'xtzusdt', 'jstusdt', \
         'massusdt', 'seeleusdt', 'bagsusdt', '1inchusdt', 'algousdt', 'zecusdt', \
         'nknusdt', 'cruusdt', 'tnbusdt', 'solusdt', 'btmusdt', 'kcashusdt', \
         'sushiusdt', 'bethusdt', 'nearusdt', 'neousdt', 'newusdt', 'chrusdt', \
         'trbusdt', 'atomusdt', 'lrcusdt', 'dotusdt', 'vsysusdt', 'paiusdt', \
         'injusdt', 'flowusdt', 'lunausdt', 'mdxusdt', 'ankrusdt', 'aaveusdt', \
         'fttusdt', 'mdsusdt']

    bbb=["bsvusdt","btmusdt","cmtusdt","crousdt","cvpusdt","hcusdt","nestusdt","newusdt","ogousdt","ontusdt","tnbusdt","itcusdt","btcusdt","ethusdt"]
    for bb in bbb:
        t = threading.Thread(target=get_htmll,args=("http://bi.kefabu.com:5000/huobi/?symbol="+bb+"&period="+aa+"&size=2000",))
        t.setDaemon(True)
        t.start()
        t.join(13)
        if t.is_alive ():
            stop_thread(t)
            print("查询K线失败！......"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        else:
            try:
                ddd=json.loads(htmll)
                #print(ddd)
                lenn=len(ddd["data"][1:])
                print("---")
                print(lenn)
                print("===")
                
                amount_v=[]
                price_v=[]
                for dd in ddd["data"][1:][::-1]:
                    idd=dd["id"]
                    openn=dd["open"]
                    high=dd["high"]
                    low=dd["low"]
                    closee=dd["close"]
                    amount=dd["amount"]
                    vol=dd["vol"]
                    count=dd["count"]

                    high_low=high-low
                    if high_low!=0 and amount!=0:
                        #amount_v.append(amount/high_low)
                        amount_v.append(high_low)
                        price_v.append(vol/amount)

                image = Image.open("111.png")
                draw =ImageDraw.Draw(image)
                #------------------------
                maxx=max(amount_v)
                minn=min(amount_v)
                h_l_1=f"H/L: {round(maxx/minn,3)}"
                maxx_minn=maxx-minn
                i=0
                lenn=len(amount_v)
                if lenn>1900:
                    amount_v=amount_v[-1900:]
                    lenn=1900
                for dd in amount_v:
                    #draw.line((i, 629, i, 629-int(((dd-minn)/maxx_minn)*300)), 'black')
                    #draw.line((i, 329, i, 329+int(((dd-minn)/maxx_minn)*300)), 'black')
                    draw.line((i, 312, i, 312+int(((dd-minn)/maxx_minn)*300)), 'black')
                    i+=1
                    if i==lenn-20:
                        draw.line((i, 312+int(((dd-minn)/maxx_minn)*300),i,619), "#cccccc")
                #=========================
                #------------------------
                maxx=max(price_v)
                minn=min(price_v)
                h_l_2=f"H/L: {round(maxx/minn,3)}"
                maxx_minn=maxx-minn
                i=0
                lenn=len(price_v)
                if lenn>1900:
                    price_v=price_v[-1900:]
                    lenn=1900
                for dd in price_v:
                    draw.line((i, 308, i, 308-int(((dd-minn)/maxx_minn)*300)), 'black')
                    i+=1
                    if i==lenn-20:
                        draw.line((i, 308-int(((dd-minn)/maxx_minn)*300),i,0), "#cccccc")
                #=========================
                setFont = ImageFont.truetype('fonts/msyh.ttf', 16)
                fillColor = "#000000"
                width, height = image.size
                #ttt1=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ddd[0][0]/1000))
                ttt1=time.strftime("%Y-%m-%d", time.localtime(ddd["data"][lenn-2]["id"]))
                ttt2=time.strftime("%Y-%m-%d", time.localtime(ddd["data"][1]["id"]))
                text_size = setFont.getsize(f"{bb}_{aa} ({ttt1}, {ttt2}) ({h_l_2})")
                text_size2 = setFont.getsize(f"({h_l_1})")
                #print(text_size)
                draw.text(((width-text_size[0])/2, 0), f"{bb}_{aa} ({ttt1}, {ttt2}) ({h_l_2})", font=setFont, fill=fillColor)
                draw.text(((width-text_size2[0])/2, height-20), f"({h_l_1})", font=setFont, fill=fillColor)
                
                #Image1.show()
                image.save(f"img_振幅/{bb}_{aa}_1.png", "png")
            except Exception as e:
                print(e)
                pass

        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
    print("--end--")

