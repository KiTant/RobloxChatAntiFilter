import os
import argparse
import json

special_replacements_applied = None

parser = argparse.ArgumentParser()

parser.add_argument('-replacements', type=str, help="Takes your replacements in file.")

args = parser.parse_args()

if args.replacements:
    file_path = args.replacements
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                DEFAULT_REPLACEMENTS = json.load(file)
                special_replacements_applied = True
                print('File with replacements loaded')
            except Exception as err:
                special_replacements_applied = False
                print(f'File with replacements was NOT loaded. Program will use default replacements\nError: {err}')
    else:
        special_replacements_applied = False
        print('File with replacements was NOT found. Program will use default replacements')
else:
    special_replacements_applied = False

if special_replacements_applied is False:
    DEFAULT_REPLACEMENTS = {
        "ru": {
            "о": "ό", "О": "Ό", "К": "K", "к": "κ", "У": "Ꭹ",
            "с": "c", "С": "C", "у": "ẏ", "р": "p", "Р": "P",
            "а": "a", "А": "A", "е": "e", "Е": "E",
            "х": "x", "Х": "X", "М": "M", "ё": "ë",
            "Ё": "Ë", "Т": "T", "В": "B", "Н": "Ĥ",
            "и": "ͷ", "П": "Π", "Г": "Γ", "ч": "ӵ",
            "н": "ӈ"
        },
        "eng": {
            "o": "ὁ", "O": "Ò", "K": "К",
            "c": "с", "C": "С", "y": "у",
            "p": "р", "P": "Р", "a": "а",
            "A": "А", "e": "е", "E": "Е",
            "x": "х", "X": "Х", "M": "М",
            "S": "Š", "t": "ť", "h": "ĥ",
            "H": "Ĥ", "d": "ď", "f": "f",
            "i": "i"
        }
    }

current_language = "Non-Assigned"


def choose_language():
    global current_language
    current_language = "Non-Assigned"
    while current_language not in list(DEFAULT_REPLACEMENTS.keys()):
        print(f"Available languages: {list(DEFAULT_REPLACEMENTS.keys())}")
        current_language = input("Enter your language of your texts: ")


def anti_filter():
    global current_language
    while True:
        text = input("Enter text for anti filter (or command): ")
        replaced_text = ""
        if text.strip() == "/exit":
            break
        elif text.strip() == "/change_language":
            choose_language()
        else:
            for letter in text.strip():
                if letter in list(DEFAULT_REPLACEMENTS[current_language].keys()):
                    replaced_text += DEFAULT_REPLACEMENTS[current_language][letter]
                else:
                    replaced_text += letter
            print(replaced_text)

choose_language()
anti_filter()
