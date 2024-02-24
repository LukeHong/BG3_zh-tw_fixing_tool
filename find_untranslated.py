import csv
import xml.etree.ElementTree as ET
import html


ts_lines = {}
tree = ET.parse('chinesetraditional.xml')
root = tree.getroot()

for child in root:
    ts_lines[child.attrib['contentuid']] = html.escape(child.text, quote=True).rstrip('\n')
del(tree)
del(root)

untranslated = []
tree = ET.parse('english.xml')
root = tree.getroot()

for child in root:
    row_id = child.attrib['contentuid']
    if row_id not in ts_lines:
        print(row_id, child.text)
        untranslated.append([row_id, '', '', html.escape(child.text, quote=True)])
del(tree)
del(root)

with open('ts_untranslated.csv', 'w', newline='', encoding='UTF-8') as write_file:
    writer = csv.writer(write_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for row in untranslated:
        writer.writerow(row)
