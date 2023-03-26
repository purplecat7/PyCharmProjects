# -*- coding: utf-8 -*-
# This is just an illustration...

from elementtree.ElementTree import ElementTree
mydoc = ElementTree(file='tst.xml')
for e in mydoc.findall('/foo/bar'):
    print(e.get('title').text)