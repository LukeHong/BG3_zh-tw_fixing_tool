import csv
import xml.etree.ElementTree as ET
import html
import os

contexts = {}
tree = ET.parse(os.path.join('source', 'english.xml'))
root = tree.getroot()

for child in root:
    contexts[child.attrib['contentuid']] = child.text # html.escape(child.text, quote=True)
del(tree)
del(root)

print(f'English contexts: {len(contexts)} rows')

translated_files = os.listdir('translated')

translated = {}
for filename in translated_files:
    if '.csv' not in filename:
        continue
    path = os.path.join('translated', filename)
    with open(path, 'r', encoding='UTF-8') as read_file:
        reader = csv.reader(read_file, delimiter=',')
        for row in reader:
            translated[row[0]] = html.unescape(row[1])


tree = ET.parse(os.path.join('source', 'chinesetraditional.xml'))
root = tree.getroot()

new_translations = []
for child in root:
    row_id = child.attrib['contentuid']
    if row_id in translated:
        continue
    row = [row_id, child.text, '', '']
    if row_id in contexts:
        row[3] = contexts[row_id]
    new_translations.append(row)

print(f'New translation: {len(new_translations)} rows.')

with open('zh_tw_new_translations.csv', 'w', newline='', encoding='UTF-8') as write_file:
    writer = csv.writer(write_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for row in new_translations:
        writer.writerow(row)

print('write to file: zh_tw_new_translations.csv')