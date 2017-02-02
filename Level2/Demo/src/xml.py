# -*- coding: utf-8 -*-

from lxml import etree

tree = etree.parse("../config/test.py")

root = tree.getroot()
print (root.tag)

for child in root.getchildren():
    print(child.tag)
    print(child.text)
    print(child.attrib)
    for grandchild in child.getchildren():
        print(grandchild.tag)
        print(grandchild.text)
        print(grandchild.attrib)
    


