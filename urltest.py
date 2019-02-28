'''
Created on 2019. 2. 13.

@author: student
'''

'''
import urllib.request
req = urllib.request

req.urlopen("http://localhost:8000/rtest/pythontest.jsp");

q = input("이름입력 : ")
import urllib.parse
parse = urllib.parse
q= parse.quote_plus(q)

#q='name='+q
print("http://localhost:8000/rtest/pythontest.jsp?"+q)
server=req.urlopen("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query="+q)
print(server.read().decode())
'''
#POST 

from urllib.parse import urlencode
from urllib.request import Request,urlopen

url="http://localhost:8000/rtest/pythontest.jsp"

post_Data={'name':'홍'}
server=Request(url,urlencode(post_Data).encode())
response=urlopen(server).read().decode()
print(response)