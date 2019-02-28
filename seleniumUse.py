'''
Created on 2019. 2. 15.

@author: student
'''
# import urllib.request
# from bs4 import BeautifulSoup
# 
# #서버접속
# # server = urllib.request.urlopen("https://www.istarbucks.co.kr/store/store_map.do")
# # #응답받자
# # reponse = server.read().decode()
# #BS
# bs = BeautifulSoup("<html></html>", 'html.parser')
# #find
# li = bs.find_all('li',class_="quickResultLstCon")
# print(li)

#셀레니움 패키지 설치
#C:/java_class/hadoop_workspace/samplepy/chromedriver.exe

from selenium import webdriver
chromedriver_path = "C:/java_class/workspace/samplypy/chromedriver.exe"
driver = webdriver.Chrome(chromedriver_path)
import time

driver.get("https://logins.daum.net/accounts/loginform.do?nil_profile=login&url=https://www.daum.net")
time.sleep(3)
loginid=driver.find_element_by_id("id")
loginid.send_keys("koprise")
loginpwd=driver.find_element_by_id("inputPwd")
loginpwd.send_keys("")
loginBtn=driver.find_element_by_id("loginBtn")
loginBtn.click()
time.sleep(3)


source=driver.page_source

daum_bs=BeautifulSoup(source,"html.parser")
daum_bs.find_all("a",class_="link_basis")

for i in daum_bs:
    print(i.text)

# #서울 지역 전체 구 매장 찾은 결과 주소
# loca = driver.find_element_by_class_name('loca_search')
# loca.click()




