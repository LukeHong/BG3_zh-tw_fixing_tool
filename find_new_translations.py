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

contexts = {}
tree = ET.parse(os.path.join(BASE_PATH, 'source', 'english.xml'))
root = tree.getroot()

for child in root:
    contexts[child.attrib['contentuid']] = child.text # html.escape(child.text, quote=True)
del tree, root

print(f'English contexts: {len(contexts)} rows')

translated_files = os.listdir(os.path.join(BASE_PATH, 'translated'))

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

if len(new_translations) > 0:
    with open(os.path.join(BASE_PATH, 'zh_tw_new_translations.csv'), 'w',
              newline='', encoding='UTF-8') as write_file:
        writer = csv.writer(write_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for row in new_translations:
            writer.writerow(row)

    print(f'write to file: {os.path.join(BASE_PATH, "zh_tw_new_translations.csv")}')
else:
    print('Skip writing file')

print('Press <ENTER> to exit')
input()
