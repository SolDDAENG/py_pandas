from selenium import webdriver

try:
    url = "http://www.daum.net"
    browser = webdriver.Chrome(r'/Users/choehansol/Downloads/chromedriver')
    browser.implicitly_wait(3)
    browser.get(url);
    browser.save_screenshot("daum_img.png")
    browser.quit()
    print('성공')

except Exception:
    print('에러')
