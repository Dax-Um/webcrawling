from bs4 import BeautifulSoup
from openpyxl import Workbook
from selenium import webdriver
import time

# 한글 읽어오기
options = webdriver.ChromeOptions()
options.add_argument("lang=ko_KR")


# 엑셀 저장 세팅
wb = Workbook()
sheet = wb.active
sheet.title = "#top100"
sheet.append(["순위", "#해시태그", "피드수"])


# 크롤링 카운트
count = 1


# 주소 입력
browser = webdriver.Chrome("../../chrome/chromedriver90.exe")
url_base = "http://cocotag.kr/index.html"
browser.get(url_base)
time.sleep(2)


# 정보블럭 선택
req = browser.page_source
html = BeautifulSoup(req, 'html.parser')
container = html.select("body > div > div > div > div > div > div.table100-body.js-pscroll > table > tbody > tr")


# 크롤링 진행
for c in container:
    try:
        # 순위
        rank = c.select_one("body > div > div > div > div > div > div.table100-body.js-pscroll > table > tbody > tr > td.cell100.column1").text.strip()
        # 해시태그
        hashtag = c.select_one("body > div > div > div > div > div > div.table100-body.js-pscroll > table > tbody > tr > td.cell100.column2 > a").text.strip()
        # 피드수
        num = c.select_one("body > div > div > div > div > div > div.table100-body.js-pscroll > table > tbody > tr > td.cell100.column3").text.strip()

        print("count = ", count)
        sheet.append([rank, hashtag, num])
        count += 1

    except:
        pass
print("크롤링 마침")


# 데이터 엑셀파일로 저장
wb.save('한글 #top100.xlsx')





