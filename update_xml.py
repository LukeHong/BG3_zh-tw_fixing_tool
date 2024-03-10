import argparse
import csv
import html
import json
import os
import sys
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument("--csv", help="use translation in csv format", action="store_true")
parser.add_argument("--json", help="use translation in json format",
                    action="store_true", default=True)
args = parser.parse_args()

BASE_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))

# load translated
translated_files = os.listdir(os.path.join(BASE_PATH, 'json'))

translated = {}
for filename in translated_files:
    file_path = os.path.join(BASE_PATH, 'translated', filename)
    if args.csv:
        if '.csv' not in filename:
            continue
        with open(file_path, 'r', encoding='UTF-8') as read_file:
            reader = csv.reader(read_file, delimiter=',')
            for row in reader:
                translated[row[0]] = html.unescape(row[1])
    else:
        if '.json' not in filename:
            continue
        with open(file_path, 'r', encoding='utf-8') as rf:
            rows = json.load(rf)
            for row in rows:
                text = html.unescape(row['translation'])
                if text == '':
                    text = html.unescape(row['original'])
                translated[row['key']] = text


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
        update_count += 1
        child.text = translated[row_id]

# print(f'{len(not_found)} rows not found.')
print(f'{update_count} rows updated.')

tree.write(os.path.join(BASE_PATH, 'translated', 'chinesetraditional.xml'),
           encoding='utf-8', xml_declaration=True)
print(f"Write to {os.path.join(BASE_PATH, 'translated', 'chinesetraditional.xml')}")

print('Press <ENTER> to exit')
input()
