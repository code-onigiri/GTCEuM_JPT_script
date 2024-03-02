import json

# ja_jp.jsonからデータを読み込む
with open('ja_jp.json', 'r', encoding='utf-8') as file:
    ja_jp_data = json.load(file)

# en_us.langからデータを読み込む
with open('en_us.lang', 'r', encoding='utf-8') as file:
    en_us_lang_lines = file.readlines()

# ja_jp.langからデータを読み込む
with open('ja_jp.lang', 'r', encoding='utf-8') as file:
    ja_jp_lang_lines = file.readlines()

# en_us.langとja_jp.langの翻訳キーと文章の辞書を作成する
en_us_lang_dict = {}
ja_jp_lang_dict = {}
for line in en_us_lang_lines:
    if '=' in line and not line.strip().startswith('#'):
        key, value_e = line.split('=', 1)
        en_us_lang_dict[key.strip()] = value_e.strip()

for line in ja_jp_lang_lines:
    if '=' in line and not line.strip().startswith('#'):
        key, value_j = line.split('=', 1)
        ja_jp_lang_dict[key.strip()] = value_j.strip()

# ja_jp.jsonからen_us.langをマッチさせてja_jp.langから翻訳する
t = 0
for key , value in ja_jp_data.items():
    if 2 < len(value):
        mae = ""
        ato = ""
        if value[0] == "§":
            mae = value[:2]
            value = value[2:]
        #print(value[len(value)-2])
        if value[len(value)-2] == '§':
            t = t + 1
            ato = value[len(value)-2:]
            value = value[:(len(value)-3)]
        for en_us_key, en_us_value in en_us_lang_dict.items():
            if value == en_us_value:
                #print(ato)
                ja_jp_data[key] = ( mae + ja_jp_lang_dict[en_us_key] + ato )
#print(t)


# ja_jp.jsonに書き込み
with open('ja_jp.json', 'w', encoding='utf-8') as file:
    json.dump(ja_jp_data, file, ensure_ascii=False, indent=4)