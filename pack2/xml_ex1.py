# XML 처리 기본 모듈
import xml.etree.ElementTree as etree

xml_f = open('../testdata/my.xml', 'r', encoding='utf-8').read()  # .read() : 바로 읽는다.
print(xml_f, ' ', type(xml_f))  # <class 'str'>

root = etree.fromstring(xml_f)
print(root)  # <Element 'items' at 0x10fb91b30>
print(root.tag)  # items
print(len(root))  # 2 ==> item의 개수

print('-------------------')
xmlfile = etree.parse('../testdata/my.xml')
# root의 결과랑 같음. <xml.etree.ElementTree.ElementTree object at 0x00000232E3828588>:
print(xmlfile)
root = xmlfile.getroot()
print(root.tag)  # items
print(root[0].tag)  # item의 0번쨰
print(root[1].tag)  # item의 1번째
print(root[0][0].tag)  # name
print(root[0][1].tag)  # tel
print  # 기상청 날씨 정보 XML 자료 읽기
import urllib.request
import xml.etree.ElementTree as etree

# ***웹에서 xml데이터를 받아서 출력한 후 그 데이터들을 현재 작업공간에 xml파일로 저장한다.***
# ===============================================================================
# try:
#     webdata = urllib.request.urlopen('http://www.kma.go.kr/XML/weather/sfc_web_map.xml')
#     webxml = webdata.read()
#     #print(webxml)
#     webxml = webxml.decode('utf-8')
#     print(webxml)
#     webdata.close()
#
#     with open('myweather.xml', mode='w', encoding='utf-8') as f:    # web에서 받은 데이터를 xml파일로 저장
#         f.write(webxml)
# except Exception as e:
#     print('err : ', e)
# ===============================================================================


xmlfile = etree.parse('../testdata/myweather.xml')
print(xmlfile)
root = xmlfile.getroot()  # root Element를 읽음
print(root.tag)  # {current}current
print(root[0].tag)  # {current}weather
child = root.findall("{current}weather")
child = root.findall(root[0].tag)  # 위랑 같은 결과다.
print(child)

for i in child:
    y = i.get('year')
    m = i.get('month')
    d = i.get('day')
    h = i.get('hour')
    print(y + '년 ' + m + '월 ' + d + '일 ' + h + '시 현재')

datas = []
for ch in root:
    # print(ch.tag)   # {current}weather
    for i in ch:
        # print(i.tag)    # {current}local .....
        local_name = i.text  # 속성을 잡는것이 아니라 값을 잡아야하니 text다.
        # print(local_name)
        ta = i.get('ta')
        desc = i.get('desc')
        datas += [[local_name, ta, desc]]  # DataFrame에 집어넣으려고 list타입에 넣었다.

print(datas)

from pandas import DataFrame

df = DataFrame(datas, columns=['지역', '온도', '기상상태'])
print(df.head())  # 앞에서 몇개만 출력
print(df['지역'])  # 모든 행의 지역만 출력
print(df.tail(3))  # 뒤에서 3개만 읽는다

# ===================위에서 두단계로 나뉜 작업을 하나로 간편하게 하는 방법 =================================================================
print('\n\n웹자료 읽어 바로 출력===============================================================')
# import urllib.request

webdata2 = urllib.request.urlopen('http://www.kma.go.kr/XML/weather/sfc_web_map.xml')
xmlFile = etree.parse(webdata2)
root = xmlFile.getroot()
ndate = list(root[0].attrib.values())  # values값만 읽는다.
print(ndate)
print(ndate[0] + '년 ' + ndate[1] + '월 ' + ndate[2] + '일 ' + ndate[3] + '시')

for child in root:
    for subChild in child:
        print(subChild.text + ' : ' + subChild.attrib.get('ta'))

# 웹 이미지 읽기
imgUrl = "http://www.livingpick.com/shopimages/partysale/0170010000222.jpg?1589439293"
saveName = 'myimage.jpg'
urllib.request.urlretrieve(imgUrl, saveName)
