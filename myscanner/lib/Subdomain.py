#coding=utf-8
import dns.resolver,os

subdomain = []

def subdomainB(domain):
    a = dns.resolver.resolve(domain,"A")
    for i in a:
        if i :
            print(domain,i)
            subdomain.append(domain+"\t"+str(i))


def readdict(_dict):
    # filepath = os.path.abspath(os.path.dirname(os.getcwd()))
    # print(filepath)
    filepath = os.getcwd()
    f = open("{}/dict/{}.txt".format(filepath, _dict), "r")
    # print("{}/dict/{}.txt".format(filepath, _dict))
    dirpath = f.readlines()
    f.close()
    return dirpath

def result():
    return subdomain
