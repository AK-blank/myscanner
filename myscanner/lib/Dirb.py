#coding=utf-8
import requests
import warnings,os

warnings.filterwarnings("ignore") #忽略警告

path = []

head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'
}

def dirburst(url):
    result = requests.get(url, headers=head, verify=False, timeout=5)
    if result.status_code == 200:
        path.append(url)
        print(url)
        # sys.stdout.write(url)

def readdict(_dict):
    # filepath = os.path.abspath(os.path.dirname(os.getcwd()))
    # print(filepath)
    filepath = os.getcwd()
    f = open("{}/dict/{}.txt".format(filepath, _dict), "r")
    dirpath = f.readlines()
    f.close()
    return dirpath

def result():
    return path