# xmlEx01.py
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import ElementTree

human = Element('human')
human.attrib['birth'] = '19701225'
human.attrib['gender'] = '남자'

SubElement(human, 'name').text = '홍길동'
SubElement(human, 'age').text = '30'
SubElement(human, 'address').text = '용산구 도원동'

def indent(elem, level = 0):
    mytab = '\t'
    i = '\n' + level * mytab

    if len(elem) :
        if not elem.text or not elem.text.strip() :
            elem.text = i + mytab

        if not elem.tail or not elem.tail.strip() :
            elem.tail = i

        for elem in elem :
            indent(elem, level + 1)

        if not elem.tail or not elem.tail.strip() :
            elem.tail = i
    else :
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

indent(human)
xmlFile = 'xmlEx01.xml'
ElementTree(human).write(xmlFile, encoding='utf-8')
print(f'{xmlFile}이 생성되었습니다.')