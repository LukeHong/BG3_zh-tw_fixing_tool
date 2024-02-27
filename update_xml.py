import csv
import html
import os
import sys
import xml.etree.ElementTree as ET

BASE_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))

# load translated
translated_files = os.listdir(os.path.join(BASE_PATH, 'translated'))

translated = {}
for filename in translated_files:
    if '.csv' not in filename:
        continue
    file_path = os.path.join(BASE_PATH, 'translated', filename)
    with open(file_path, 'r', encoding='UTF-8') as read_file:
        reader = csv.reader(read_file, delimiter=',')
        for row in reader:
            translated[row[0]] = html.unescape(row[1])

print(f'Translated: {len(translated)} rows.')

tree = ET.parse(os.path.join(BASE_PATH, 'source', 'chinesetraditional.xml'))
root = tree.getroot()

not_found = []
update_count = 0
for child in root:
    row_id = child.attrib['contentuid']
    if row_id not in translated:
        not_found.append([row_id, child.text])
        continue

    if child.text != translated[row_id]:
        # print(child.text)
        # print(f' -> {translated[row_id]}')
        update_count += 1
        child.text = translated[row_id]

# print(f'{len(not_found)} rows not found.')
print(f'{update_count} rows updated.')

tree.write(os.path.join(BASE_PATH, 'translated', 'chinesetraditional.xml'), encoding='utf-8', xml_declaration=True)
print(f"Write to {os.path.join(BASE_PATH, 'translated', 'chinesetraditional.xml')}")

print('Press <ENTER> to exit')
input()