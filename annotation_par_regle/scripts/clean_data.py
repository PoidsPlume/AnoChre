import re
from pathlib import Path

def remove_punctuation(text):
    # Use a regular expression to remove all punctuation characters
    cleaned_text = re.sub(r'[^\w\s\n\'’ʼ]', '', text)
    return cleaned_text

def clean_files():
    for p in Path('./raw_data/').glob('*.txt'):
        with open(p, 'r', encoding="utf-8") as f:
            raw_text = f.read()
        title_file = "./clean_data/" + str(p)[8:len(str(p))]
        with open(title_file, 'w') as f:
            f.write(remove_punctuation(raw_text))

