'''
Created on 2019. 2. 15.

@author: student
'''
from selenium import webdriver
chromedriver_path = "C:/java_class/workspace/samplypy/chromedriver.exe"
driver = webdriver.Chrome(chromedriver_path)

driver.get("https://www.istarbucks.co.kr/store/store_map.do")

import time
time.sleep(3)

#서울 지역 전체 구 매장 찾은 결과 주소
loca = driver.find_element_by_class_name('loca_search')
loca.click()
time.sleep(3)
#서울지역 선택
sido=driver.find_element_by_class_name("sido_arae_box")


sido_list=sido.find_elements_by_tag_name("li")

sido_list[0].click()
time.sleep(3)

#전체구 가져오기
gugun=driver.find_element_by_class_name("gugun_arae_box")
gugun_list=gugun.find_elements_by_tag_name("li")
gugun_list[0].click()
time.sleep(3)

#변경된 소스 가져오기
source=driver.page_source

from bs4 import BeautifulSoup
result_bs=BeautifulSoup(source,"html.parser")
li=result_bs.find_all("li",class_="quickResultLstCon")

print("___")
for i in li:
    print(i.find("p").text)