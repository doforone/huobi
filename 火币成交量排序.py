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

    bbb=[
    "1inchusdt",    "aacusdt",    "aaveusdt",    "abtusdt",    "achusdt",
    "actusdt",    "adausdt",    "aeusdt",    "akrousdt",    "algousdt",    "ankrusdt",    "antusdt",    "api3usdt",    "arpausdt",    "arusdt",    "astusdt",    "atomusdt",    "atpusdt",
    "auctionusdt",    "avaxusdt",    "badgerusdt",    "bagsusdt",    "balusdt",    "bandusdt",    "batusdt",    "bchausdt",
    "bchusdt",    "bethusdt",    "bhdusdt",    "bixusdt",    "blzusdt",    "bntusdt",    "borusdt",    "bsvusdt",    "btcusdt",    "btmusdt",    "btsusdt",    "bttusdt",    "chrusdt",
    "chzusdt",    "ckbusdt",    "cmtusdt",    "cnnsusdt",    "compusdt",    "creusdt",    "crousdt",    "cruusdt",
    "crvusdt",    "ctxcusdt",    "cvcusdt",    "cvpusdt",    "dacusdt",    "dashusdt",    "dcrusdt",
    "dfusdt",    "dhtusdt",    "dkausdt",    "dockusdt",    "dogeusdt",    "dotusdt",    "dtausdt",    "egtusdt",    "ektusdt",    "elausdt",    "elfusdt",    "emusdt",    "eosusdt",    "etcusdt",    "ethusdt",    "filusdt",
    "firousdt",    "fisusdt",    "flowusdt",    "forusdt",    "frontusdt",    "fsnusdt",    "ftiusdt",    "fttusdt",    "glmusdt",    "gnxusdt",
    "gofusdt",    "grtusdt",    "gtusdt",    "gxcusdt",    "hb10usdt",    "hbarusdt",    "hbcusdt",    "hcusdt",    "hitusdt",    "hiveusdt",    "hotusdt",
    "hptusdt",    "htusdt",    "icxusdt",    "injusdt",    "iostusdt",    "iotausdt",    "iotxusdt",    "irisusdt",    "itcusdt",
    "jstusdt",    "kanusdt",    "kavausdt",    "kcashusdt",    "kncusdt",    "ksmusdt",    "lambusdt",    "lbausdt",
    "letusdt",    "linausdt",    "linkusdt",    "lolusdt",    "loomusdt",    "lrcusdt",    "ltcusdt",    "lunausdt",    "lxtusdt",    "manausdt",    "maskusdt",
    "massusdt",    "maticusdt",    "mdsusdt",    "mdxusdt",    "mkrusdt",    "mlnusdt",    "mtausdt",    "mxcusdt",
    "mxusdt",    "nanousdt",    "nasusdt",    "nbsusdt",    "nearusdt",    "neousdt",    "nestusdt",    "newusdt",    "nexousdt",    "nhbtcusdt",    "nknusdt",    "nodeusdt",    "nsureusdt",    "nulsusdt",
    "ocnusdt",    "ognusdt",    "ogousdt",    "omgusdt",    "oneusdt",    "ontusdt",    "oxtusdt",    "paiusdt",    "pearlusdt",
    "phausdt",    "polsusdt",    "pondusdt",    "pvtusdt",    "qtumusdt",    "reefusdt",    "renusdt",    "ringusdt",
    "rsrusdt",    "ruffusdt",    "rvnusdt",    "sandusdt",    "seeleusdt",    "sklusdt",    "skmusdt",    "smtusdt",    "sntusdt",    "snxusdt",    "socusdt",    "solusdt",    "steemusdt",    "storjusdt",    "stptusdt",    "sunusdt",    "sushiusdt",
    "swftcusdt",    "swrvusdt",    "thetausdt",    "titanusdt",    "tnbusdt",    "topusdt",    "trbusdt",    "trxusdt",    "ttusdt",    "uipusdt",    "umausdt",
    "uniusdt",    "utkusdt",    "uuuusdt",    "valueusdt",    "vetusdt",    "vidyusdt",    "vsysusdt",    "wavesusdt",    "waxpusdt",
    "wiccusdt",    "wnxmusdt",    "woousdt",    "wtcusdt",    "wxtusdt",    "xemusdt",    "xlmusdt",    "xmrusdt",    "xmxusdt",    "xrpusdt",
    "xrtusdt",    "xtzusdt",    "yamusdt",    "yeeusdt",    "yfiiusdt",    "yfiusdt",    "zecusdt",    "zenusdt",    "zilusdt",    "zksusdt",    "zrxusdt"
]
    vols={}
    for bb in bbb:
        t = threading.Thread(target=get_htmll,args=("http://bi.kefabu.com:5000/huobi/?symbol="+bb+"&period="+aa+"&size=11",))
        t.setDaemon(True)
        t.start()
        t.join(13)
        if t.is_alive ():
            stop_thread(t)
            print("查询K线失败！......"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        else:
            try:
                ddd=json.loads(htmll)
                lenn=len(ddd["data"][1:])
                
                vol=0
                for dd in ddd["data"][1:][::-1]:
                    vol+=dd["vol"]

                vols[bb]=vol

            except Exception as e:
                print(e)
                pass

        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

    ttt=sorted(vols.items(), key=lambda x : x[1], reverse=True)
    print(ttt)

    sss=[]
    for tt in ttt:
        sss+=[tt[0]]
    print(sss)
    print("--end--")

