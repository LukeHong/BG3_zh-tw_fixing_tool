import csv
import xml.etree.ElementTree as ET
import html

contexts = {}
tree = ET.parse('english.xml')
root = tree.getroot()

for child in root:
    contexts[child.attrib['contentuid']] = html.escape(child.text, quote=True)
del(tree)
del(root)


data = []
with open('TS.csv', 'r', encoding='UTF-8') as read_file:
    reader = csv.reader(read_file, delimiter=',')
    for row in reader:
        row.append('')
        if row[0] in contexts:
            row[-1] = contexts[row[0]]

        data.append(row)

with open('TS_contexted.csv', 'w', newline='', encoding='UTF-8') as write_file:
    writer = csv.writer(write_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for row in data:
        writer.writerow(row)