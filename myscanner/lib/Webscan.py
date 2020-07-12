import requests,sys,re

head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'
}

host = []

def scan(url):
    # x = host[0].rfind(":")
    rst = requests.get(url,headers=head,verify=False,timeout=5)
    if rst.status_code == 200:
        try:
            title = re.findall("<title>(.*?)</title>",rst.text)
            host.append(url +"\t"+ title[0])
        except:
            title = "None"
            host.append(url+"\t"+title)
        print("%s is UP"% url)
def result():
    # x = host[0].rfind(".")  # 截取最后一个“.”所在位置
    # host.sort(key=lambda i: int(i[x + 1:]))
    return host