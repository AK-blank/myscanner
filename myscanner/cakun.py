#coding=utf-8
import threading,warnings,os,queue,time
from optparse import OptionParser
from lib import Dirb,process,Webscan,Subdomain
from IPy import IP

warnings.filterwarnings("ignore") #忽略警告

class START:
        def __init__(self,options):
            self._url = options.url
            self._dict = options.dict
            self._threadnum = options.threadnum
            self._port = options.port

        class do(threading.Thread):
            def __init__(self,queue,size):
                threading.Thread.__init__(self)
                self._queue = queue
                self._size = size

            def run(self):
                while not self._queue.empty():
                    url = self._queue.get()
                    process.main(self._queue.qsize(), self._size)
                    try:
                        #--------------------------模块选择
                        if options.Dirb :
                            Dirb.dirburst(url)
                        elif options.Webscan :
                            Webscan.scan(url)
                        elif options.Subdomain :
                            Subdomain.subdomainB(url)
                    except:
                        pass

        def main(self):
            if options.Dirb and options.Webscan and options.Subdomain :
                parser.print_help()
                print("1")
                print("\nFormat error!Only one module can be used at a time")
                return
             # 保存扫描结果
            threads = []
            t = time.time()  # 计时
            q = queue.Queue()  # 设置一个queue对象
            protocols = ["http://", "https://"]

            #----------------------------------------模块选择
            if options.Dirb:
                dirpath = Dirb.readdict(self._dict)
                print("Welcome to  Dirburst module")
                print("-"*50)
                for protocol in protocols:
                    for i in range(len(dirpath)):
                        p = dirpath[i].strip("\n")
                        q.put("{}{}/{}".format(protocol,self._url,p))  #将整个字典以完整url形式压入
                        # print("{}{}/{}".format(protocol,self._url,p))
            elif options.Webscan:
                print("Welcome to  Webscan module")
                print("-" * 50)
                ips = IP("{}".format(self._url))
                port = self._port.split(",")
                for protocol in protocols:
                    for ip in ips:
                        for i in port:
                            q.put("{}{}:{}".format(protocol,str(ip),i))
                            # print("{}{}:{}".format(protocol,str(ip),i))
            elif options.Subdomain:
                print("Welcome to  SubdomainBurst module")
                print("-" * 50)
                dictionary = Subdomain.readdict(self._dict)
                for i in range(len(dictionary)):
                    d = dictionary[i].strip("\n")
                    q.put(d+"."+self._url)
            size = q.qsize()
            for i in range(self._threadnum): #将线程压入列表，便于多线程的进行
                threads.append(self.do(q,size))
            print("初始化完成(Initialization is complete)")
            for i in range(self._threadnum): #启动线程
                threads[i].start()
            for i in range(self._threadnum): #同步所有线程
                threads[i].join()
                time.sleep(0.01)
            tt = time.time() - t
            print("\nMission over,spend time：%s" % tt)

            #----------------------结果导出：
            filepath = os.getcwd()
            if options.Dirb:
                result = Dirb.result()
                f = open("{}/result/{}.txt".format(filepath,self._url), "w")
                for rst in result:
                    f.write(rst+"\n")
                f.close()
                print("File saved in {}/result/{}.txt".format(filepath,self._url))
            elif options.Webscan:
                result = Webscan.result()
                f = open("{}/result/{}.txt".format(filepath,self._url[:-3]),"w")
                for rst in result:
                    f.write(rst+"\n")
                f.close()
                print("File saved in {}/result/{}.txt".format(filepath, self._url[:-3]))
            elif options.Subdomain:
                result = Subdomain.result()
                f = open("{}/result/{}.txt".format(filepath,self._url),"w")
                for rst in result:
                    f.write(rst+"\n")
                f.close()
                print("File saved in {}/result/{}.txt".format(filepath, self._url))
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("--dirb",dest="Dirb",type="int",default=0,help="Dirburst Moudle input 1 if you want to use")
    parser.add_option("--webscan",dest="Webscan",type="int",default=0,help="Webscan Moudle input 1 if you want to use")
    parser.add_option("--subdomain",dest="Subdomain",type="int",default=0,help="SubdomainBurst  Moudle input 1 if you want to use")
    parser.add_option("-u", "--url", dest="url",help="target (www.baidu.com;127.0.0.0/24;baidu.com)")
    parser.add_option("-d", "--dict",dest="dict", default="path",help="choice dict(Had dictionary:path,dic)")
    parser.add_option("-t","--threads",dest="threadnum",type="int",default=10,help="number of threads")
    parser.add_option("-p","--port",dest="port",default="80,443,3306,8080",help="Specify  ports separated by ',' ")
    (options,args) = parser.parse_args()
    # print(options.url,options.num,options.dict)
    if options.url and (options.Dirb  or options.Webscan or options.Subdomain):


        print('''
  _  _
 / )/_| /__//  //| )
(__(  |/  )(__// |/
                ''')
        # main(options.url,options.threadnum,options.dict)
        s = START(options)
        s.main()

    else:
        print('''
  _  _
 / )/_| /__//  //| )
(__(  |/  )(__// |/
        ''')
        parser.print_help()
        print("Lack of Moudle or target")
