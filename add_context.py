import csv
import html
import os
import sys
import xml.etree.ElementTree as ET

BASE_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))

contexts = {}
tree = ET.parse(os.path.join(BASE_PATH, 'source', 'english.xml'))

root = tree.getroot()

for child in root:
    contexts[child.attrib['contentuid']] = child.text #html.escape(child.text, quote=True)
del tree, root

print(f'English contexts: {len(contexts)} rows')

data = []
update_count = 0
with open(os.path.join(BASE_PATH, 'translated', 'TS.csv'), 'r', encoding='UTF-8') as read_file:
    reader = csv.reader(read_file, delimiter=',')
    for row in reader:
        row.append('')
        row[1] = html.unescape(row[1])
        if row[0] in contexts:
            update_count += 1
            row[-1] = contexts[row[0]]

        data.append(row)

print(f'{update_count} rows of context added.')

with open('TS.csv', 'w', newline='', encoding='UTF-8') as write_file:
    writer = csv.writer(write_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for row in data:
        writer.writerow(row)
