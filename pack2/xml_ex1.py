# XML 처리 기본 모듈
import xml.etree.ElementTree as etree

xml_f = open('my.xml', 'r', encoding='utf-8').read()  # .read() : 바로 읽는다.
print(xml_f, ' ', type(xml_f))  # <class 'str'>

root = etree.fromstring(xml_f)
print(root)  # <Element 'items' at 0x00000232E381E458>
print(root.tag)  # items
print(len(root))  # 2 => item의 개수

print('---------------------------')
xmlfile = etree.parse('my.xml')  # root의 결과랑 같음. <xml.etree.ElementTree.ElementTree object at 0x00000232E3828588>
print(xmlfile)
root = xmlfile.getroot()
print(root.tag)  # items
print(root[0].tag)  # item 0번쨰
print(root[1].tag)  # item 1번쨰
print(root[0][0].tag)  # name
print(root[0][1].tag)  # tel
print(root[0][0].attrib)  # {'id': 'ks1'}
print(root[0][0].attrib.keys())  # dict_keys(['id'])
print(root[0][0].attrib.get("id"))  # ks1

print()
myname = root.find("item").find("name").text  # item속성의 name의 값을 호출
mytel = root.find("item").find("tel").text
print(myname, ' ', mytel)  # 홍길동  111-1111

print()
for child in root:
    print(child.tag)  # item
    for child2 in child:
        print(child2.tag, ' ', child2.attrib)

print()
for e in root.iter('exam'):
    print(e.attrib)

print('-----------------------------------')
children = root.findall('item')  # item을 전부 찾아준다
for c in children:
    re_id = c.find('name').get('id')  # id출력
    re_name = c.find('name').text  # name 태그의 값
    re_tel = c.find('tel').text  # tel 태그의 값

    print(re_id, ' ', re_name, ' ', re_tel)
