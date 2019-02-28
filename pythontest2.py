'''
Created on 2019. 2. 14.

@author: student
'''
import os

print(os.getcwd())
#print(os.access("C:\java_class\workspace\samplypy"),os.X_OK)
'''
if os.access("C:/a/b/c/d",os.X_OK) ==False:
    os.makedirs("C:/a//c/d")
else:
    print("이미있으")
'''
#파일삭제

#os.remove("C:/a")

if os.access("moduletest1.py",os.X_OK)==True:
    os.remove("moduletest1.py")
else:
    print("삭제할 파일 없옹... ")
    

import sys

print(sys.path)
print(sys.version)
print(sys.getdefaultencoding())
print(sys.getwindowsversion())
print(sys.modules)

import time

print(time.gmtime())
print(time.localtime())
print(time.strftime("%Y %m %d %H %M %S",time.localtime()))
#help(time.strftime)
a=1234.56789
print(format(a,"4.2f"))
print(format(a,"10.2f"))
print(format(a,"2.3f"))

print(len(sys.argv))
for arg in enumerate(sys.argv):
    print(arg)
    
import mymodule
import bs4.BeautifulSoup
html='<html><body><h1>test</h1></body></html'
b=bs4.BeautifulSoup(html,'html.parser')
print(b.find("h1"))

