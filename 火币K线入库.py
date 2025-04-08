# -*- coding: UTF-8 -*-

from urllib import request, parse
from urllib.parse import quote

import time
import json
import pyodbc

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
    global htmll
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    try:
        req = request.Request(urll, headers=headers)
        with request.urlopen(req, timeout=125) as resp:
            htmll=resp.read().decode("utf-8")
    except Exception as e:
        htmll=""


if __name__ == "__main__":
    htmll=""

    #aa=["5min", "15min", "30min", "60min", "4hour", "1day", "1mon", "1week", "1year"]
    aa=["5min", "15min", "30min", "60min", "4hour", "1day"]
    
    bb=["usdthusd","nasusdt","hb10usdt","omgusdt","btsusdt","ctxcusdt",\
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
    #venu对没有数据，所以删除
    bb+=["cvcbtc", "ruffbtc", "zecbtc", "newbtc", "trxbtc", "ethbtc", \
         "linkbtc", "nanobtc", "wavesbtc", "gxcbtc", "xembtc", "vetbtc", \
         "dashbtc", "hitbtc", "smtbtc", "ctxcbtc", "wtcbtc", "lambbtc", \
         "adabtc", "nulsbtc", "itcbtc", "bixbtc", "bsvbtc", "bchbtc", \
         "btsbtc", "irisbtc", "zrxbtc", "sntbtc", "qtumbtc", "letbtc", \
         "elabtc", "gntbtc", "xmrbtc", "cmtbtc", "btmbtc", "xlmbtc", \
         "zilbtc", "elfbtc", "wiccbtc", "paibtc", "nasbtc", "xrpbtc", \
         "lbabtc", "ttbtc", "rsrbtc", "kanbtc", "actbtc", "omgbtc", \
         "neobtc", "iostbtc", "htbtc", "eosbtc", "aebtc", "socbtc", \
         "venbtc", "ocnbtc", "dtabtc", "atombtc", "dogebtc", "storjbtc", \
         "bttbtc", "thetabtc", "etcbtc", "hptbtc", "ontbtc", "steembtc", \
         "mdsbtc", "ltcbtc", "topbtc", "dcrbtc", "iotabtc", "hcbtc"]
    
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1;DATABASE=kline;UID=aaa_all;PWD=chaoxian102')
    cursor = cnxn.cursor()

    while True:
        for a in aa:
            for b in bb:
                time_start=time.time()
                numm=0
##                t = threading.Thread(target=get_htmll,args=("https://api.huobi.pro/market/history/kline?symbol="+b+"&period="+a+"&size=2000",))
                t = threading.Thread(target=get_htmll,args=("http://198.176.54.17:5000/huobi/?symbol="+b+"&period="+a+"&size=2000",))
                t.setDaemon(True)
                t.start()
                t.join(130)
                if t.isAlive ():
                    stop_thread(t)
                    print("查询K线失败！......"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                else:
                    try:
                        dd=json.loads(htmll)
                        for d in dd["data"][1:]:
                            strsql="select id from huobi where symbol='"+b+"' and period='"+a+"' and id='"+str(d["id"])+"'"
                            cursor.execute(strsql)
                            row=cursor.fetchone()
                            if row is None:
                                strsql="insert into huobi(symbol,period,id,openn,closee,high,low,amount,vol,count) values \
                                ('"+b+"','"+a+"','"+str(d["id"])+"','"+str(d["open"])+"','"+str(d["close"])+"','"+str(d["high"])+"',\
                                '"+str(d["low"])+"','"+str(d["amount"])+"','"+str(d["vol"])+"','"+str(d["count"])+"')"
                                cursor.execute(strsql)
                                cursor.commit()
                                numm+=1
                            else:
                                #numm+=1
                                break
                    except Exception as e:
                        print(e)
                        pass

                time.sleep(13.01)
                time_end=time.time()
                print(a+" "+b+" +"+str(numm)+'    time cost:',time_end-time_start,'s=='+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_end)))

    print("--end--")

