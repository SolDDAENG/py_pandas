from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import time

try:
    url = 'https://www.gmail.com/'
    browser = webdriver.Chrome(r'/Users/choehansol/Downloads/chromedriver')
    browser.implicitly_wait(5)
    browser.get(url)
    browser.find_element_by_id('identifierId').send_keys('chlgksthfrlahWL@gmail.com')
    browser.find_element_by_id('identifierNext').click()
    browser.implicitly_wait(10)
    browser.find_element_by_name('password').send_keys('ghktksrh11')
    browser.find_element_by_id('passwordNext').click()

    time.sleep(5)

    html = browser.page_source

    # BeautifulSoup 사용
    soup = BeautifulSoup(html, 'html.parser')

    sender = soup.select('span.bA4 > span')
    subjects = soup.select('div.y6 > span')
    contents = soup.select('span.y2')

    # 텍스트 리스트
    senders_list = []
    subjects_list = []
    contents_list = []

    # 보낸사람 공백 항목 제거 / 보낸사람 리스트
    count = 0
    for s in sender:
        if count == 0:
            count = 1

        elif count == 1:
            senders_list.append(s.text)
            count = 0

    # 제목 리스트
    for sub in subjects:
        subjects_list.append(sub.text)

    # 내용 리스트
    for con in contents:
        contents_list.append(con.text[:20])

    mail_data = {'보낸이': senders_list, '제목': subjects_list, '내용': contents_list}

    df = DataFrame(mail_data)
    print(df)

    browser.quit()
except Exception as e:
    print("Error :", e)
