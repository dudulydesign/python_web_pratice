#執行緒
'''
import requests
portlist = [80,443,7001,7002,8000,8080,8081,8888,9000,9001]
ips = [t.replae("\n","") for t in open('ip.txt',"r").readlines()]
for ip in ips
    for port in portlist:
        url = "http://" + ip + ':' + str(port)
        try:
            resp = requests.get(url=url, timeout=2)
            print url, "mabey normal...."
        except:
            print url, "unknown wrong..."
import requests 
portlist=[80,443,7001,7002,8000,8080,8081,8888,9000,9001] 
ips=[t.replace("\n","") 
for t in open('ip.txt',"r").readlines()] 
    for ip in ips: 
        for port in portlist: 
            url="http://"+ip+':'+str(port) 
            try: 
                resp=requests.get(url=url,timeout=2) 
                print url,"mabey normal..." 
            except: print url,"unknown wrong..." 
            #原文網址：https://itw01.com/HN7NEP3.html
'''

import requests
import threading

def req(url):
    try:
        resp=requests.get(url=url,timeout=2)
        print url, "mabey normal..."
    except:
        print url, "unknown wrong..."

def main():
    portlist = [80,443,7001,7002,8000,8080,8081,8888,9000,9001]
    ips = [t.replace("\n","") for t in open('ip.txt',"r").readlines()]
    urllist=[]
    threads=[]
    for ip in ips:
        for port in portlist:
            urllist.append("http://"+ip+':'+str(port))

    for url in urllist:
        t=threading.Thread(target=req,args=(url,))
        threads.append(t)
    for t in threads:
        t.start()
        while True:
            if(len(threading.enumerate())<100):
                break

if __name__ == '__main__':
    main()
