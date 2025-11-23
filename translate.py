import re
import json

cjk_match = re.compile(r'[\u2E80-\u9FFF]')

# Load translations
with open("translate.json", 'r', encoding='utf-8') as f:
    trans_dict = json.load(f)

# Convert to list
translations = []
for k in trans_dict:
    translations.append((k, trans_dict[k]))
# Sort by length to prevent partial translations
translations.sort(key=lambda x: -len(x[0]))

# Translate script
with open('retarget_script2.py', 'r', encoding='utf-8') as f:
    with open('retarget_script2_en.py', 'w', encoding='utf-8', newline='\n') as of:
        for line in f:
            if cjk_match.search(line):
                for orig, trans in translations:
                    line = line.replace(orig, trans)
                if cjk_match.search(line):
                    print(f'Warning: Japanese text still found: {line}')
            of.write(line)
