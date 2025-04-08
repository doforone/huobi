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

def htmll(url, params=None, add_to_headers=None):
    global html
    headers = {
        "User-Agent": "Chrome",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    if add_to_headers:
        headers.update(add_to_headers)

    postdata=None
    if params:
        postdata = json.dumps(params).encode("utf-8")

    try:
        if postdata:
            req = request.Request(url=url, data=postdata, headers=headers,
                                  origin_req_host=None, unverifiable=False,
                                  method="POST")
        else:
            req = request.Request(url=url, headers=headers,
                                  origin_req_host=None, unverifiable=False,
                                  method="GET")
            
        with request.urlopen(req, timeout=9) as resp:
            html=resp.read().decode("utf-8")


            ttt=json.loads(html)
            if ttt["status"]=="ok":
                ttt["data"].reverse()  #改成时间从小到大排序
                
                if ttt["data"][-1]["id"]//aaa[aa]==timee_ab()//aaa[aa]:
                    ttt["data"].pop()
                    #print(f"{bb}: 正常")
                else:
                    #print(ttt["data"][-1]["id"])
                    f_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    print(f"{bb}: 不正常--------{f_time}")

##                if ttt["data"][-1]["id"]//aaa[aa]==timee_ab()//aaa[aa]-1:
##                    #print(f"{bb}: 2正常")
##                    pass
##                else:
##                    f_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
##                    print(f"{bb}: 2不正常--------{f_time}")
            else:
                f_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print(f"Data_Err:{bb}......{f_time}")




            
    except Exception as e:
        print(e)
        html=""

def exch_timee():  #交易所时间
    global ab_time
    uuu=api_a+api_b+"/v1/common/timestamp"
    try:
        html=htmll(uuu)
        ttt=json.loads(html)
        if ttt["status"]=="ok":
            lock.acquire()
            ab_time=int(time.time()*1000)-ttt["data"]
            lock.release()
    except Exception as e:
        #print(e)
        pass


def timee_ab():  #准确UTC时间
    return time.time()-ab_time/1000

if __name__ == "__main__":

    aaa={"1min":60, "5min":300, "15min":900, "30min":1800, "60min":3600,
         "4hour":14400, "1day":86400}

    bbb=['btcusdt', 'ethusdt', 'eosusdt', 'bchusdt', 'xrpusdt', 'ltcusdt',
         'htusdt', 'bsvusdt', 'trxusdt', 'linkusdt', 'dotusdt', 'adausdt',
         'jstusdt', 'etcusdt', 'bttusdt', 'zecusdt', 'uniusdt', 'dogeusdt',
         'dashusdt', 'filusdt', 'omgusdt', 'sunusdt', 'sushiusdt', 'iostusdt',
         'ontusdt', 'xlmusdt', 'atomusdt', 'seeleusdt', 'qtumusdt', 'mdxusdt',
         'yfiusdt', 'neousdt', 'crvusdt', 'yfiiusdt', 'xmrusdt', 'grtusdt',
         'thetausdt', 'algousdt', 'zilusdt', 'aaveusdt', 'btmusdt', 'bagsusdt',
         'xtzusdt', 'aacusdt', 'wiccusdt', 'crousdt', 'lambusdt', 'hcusdt',
         'ttusdt', 'zksusdt', 'vetusdt', '1inchusdt', 'dacusdt', 'rsrusdt',
         'nodeusdt', 'newusdt', 'lunausdt', 'achusdt', 'ksmusdt', 'iotausdt',
         'elfusdt', 'topusdt', 'kavausdt', 'xemusdt', 'zrxusdt', 'elausdt',
         'akrousdt', 'nasusdt', 'renusdt', 'cvcusdt', 'hptusdt', 'ctxcusdt',
         'nearusdt', 'storjusdt', 'flowusdt', 'gxcusdt', 'actusdt', 'phausdt',
         'letusdt', 'bandusdt', 'maticusdt', 'polsusdt', 'socusdt', 'mxusdt',
         'paiusdt', 'btsusdt', 'itcusdt', 'dtausdt', 'badgerusdt', 'antusdt',
         'snxusdt', 'maskusdt', 'compusdt', 'ruffusdt', 'sntusdt', 'nestusdt',
         'wavesusdt', 'kcashusdt', 'hb10usdt', 'hiveusdt', 'titanusdt',
         'chzusdt', 'forusdt', 'gofusdt', 'ogousdt', 'avaxusdt', 'glmusdt',
         'egtusdt', 'valueusdt', 'ektusdt', 'manausdt', 'reefusdt', 'steemusdt',
         'mdsusdt', 'irisusdt', 'aeusdt', 'trbusdt', 'emusdt', 'batusdt',
         'pearlusdt', 'ckbusdt', 'bhdusdt', 'nulsusdt', 'smtusdt', 'cmtusdt',
         'nexousdt', 'massusdt', 'fsnusdt', 'ocnusdt', 'woousdt', 'fttusdt',
         'arpausdt', 'zenusdt', 'lbausdt', 'chrusdt', 'pondusdt', 'lrcusdt',
         'mkrusdt', 'vsysusdt', 'solusdt', 'hbcusdt', 'mxcusdt', 'borusdt',
         'skmusdt', 'vidyusdt', 'sandusdt', 'bixusdt', 'swrvusdt', 'balusdt',
         'atpusdt', 'iotxusdt', 'wtcusdt', 'wnxmusdt', 'gtusdt', 'sklusdt',
         'lxtusdt', 'frontusdt', 'nknusdt', 'ognusdt', 'kncusdt', 'uuuusdt',
         'lolusdt', 'rvnusdt', 'umausdt', 'arusdt', 'nbsusdt', 'ankrusdt',
         'oneusdt', 'oxtusdt', 'nanousdt', 'xrtusdt', 'uipusdt', 'dcrusdt',
         'kanusdt', 'cruusdt', 'bntusdt', 'pvtusdt', 'dkausdt', 'firousdt',
         'icxusdt', 'fisusdt', 'mtausdt', 'creusdt', 'astusdt', 'bchausdt',
         'linausdt', 'loomusdt', 'blzusdt', 'dfusdt', 'dockusdt', 'cnnsusdt',
         'hitusdt', 'auctionusdt', 'ringusdt', 'api3usdt', 'yamusdt', 'hotusdt',
         'wxtusdt', 'gnxusdt', 'waxpusdt', 'yeeusdt', 'injusdt', 'hbarusdt',
         'swftcusdt', 'nhbtcusdt', 'ftiusdt', 'cvpusdt', 'nsureusdt', 'dhtusdt',
         'abtusdt', 'mlnusdt', 'xmxusdt', 'utkusdt', 'bethusdt', 'tnbusdt',
         'stptusdt']
    
    aa="5min"
    ab_time=100
    api_a="https://"
    api_b="api-aws.huobi.pro"

    exch_timee()
    
    while True:
        time.sleep(2)
        try:
            if timee_ab()%aaa[aa]>=3 and timee_ab()%aaa[aa]<12:
                for bb in bbb:
                    
                    f_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    print(f"{bb}......{f_time}")
                            
                    html=""
                    ttt=[]
                    time_start=time.time()
                    t = threading.Thread(
                        target=htmll,args=(
                            "https://api-aws.huobi.pro/market/history/kline?period="+aa+"&size=200&symbol="+bb,))
                    t.setDaemon(True)
                    t.start()
##                    t.join(13)
##                    if t.is_alive ():
##                        stop_thread(t)
##                        f_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
##                        print(f"查询K线{bb}失败！......{f_time}")
##                    else:
##                        ttt=json.loads(html)
##                        if ttt["status"]=="ok":
##                            ttt["data"].reverse()  #改成时间从小到大排序
##                            
##                            if ttt["data"][-1]["id"]//aaa[aa]==timee_ab()//aaa[aa]:
##                                ttt["data"].pop()
##                                #print(f"{bb}: 正常")
##                            else:
##                                #print(ttt["data"][-1]["id"])
##                                f_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
##                                print(f"{bb}: 不正常--------{f_time}")
##
##                            if ttt["data"][-1]["id"]//aaa[aa]==timee_ab()//aaa[aa]-1:
##                                #print(f"{bb}: 2正常")
##                                pass
##                            else:
##                                f_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
##                                print(f"{bb}: 2不正常--------{f_time}")
##                        else:
##                            f_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
##                            print(f"Data_Err:{bb}......{f_time}")
            else:
                print("==")
        except Exception as e:
            print(e)
            html=""
    print("--end--")
