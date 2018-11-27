path = 'Virsh.txt'
import re
import xml.etree.ElementTree as ET

def function (start_list):
    for i in range(0, len(start_list)):
        if isinstance(start_list[i], list):
            function(start_list[i])
        else:
            finish_list.append(start_list[i])


file = open(path, 'r')
read_words = []

read_file = file.readlines()
file.close()

for i in range(0, len(read_file)):
    read_file[i] = re.sub('[!?.,—\']', '', read_file[i])
    read_words.append(read_file[i].split())


finish_list = []
function(read_words)

for i in range(0, len(finish_list)):
    finish_list[i] = str(finish_list[i]).lower()

from collections import Counter
counter = Counter(finish_list)

root = ET.Element("root")
wordEl = ET.SubElement(root, "counter")

for word, count in counter.items():
    ET.SubElement(wordEl, "word", name = word).text = str(count)
tree = ET.ElementTree(root)
tree.write("c.xml")