# 웹에서 제공되는 강남구 도서관 정보 XML 읽기
import urllib.request as req
from bs4 import BeautifulSoup

urls = 'http://openapi.seoul.go.kr:8088/sample/xml/SeoulLibraryTime/1/5/'
plainText = req.urlopen(urls).read().decode()   # decode도 가능
#print(plainText)

xmlObj = BeautifulSoup(plainText, 'lxml')
libData = xmlObj.select('row')  # row에 해당 데이터들이 들어있다.
#print(libData)

for data in libData:
    name = data.find('lbrry_name').text
    addr = data.find('adres').text
    tel = data.find('tel_no').text
    print('도서관명 : ', name)
    print('주소 : ', addr)
    print('전화 : ', tel, '\n')









