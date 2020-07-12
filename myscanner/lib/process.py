#coding=utf-8
import sys


def main(current,total):
    percent = (1 - float(current / total)) * 100
    s = "\r当前进度:%.2f%s\t" % (percent, "%")
    sys.stdout.write(s)