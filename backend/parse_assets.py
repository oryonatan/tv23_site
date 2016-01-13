import json

VIDEO_URL = 'https://cdnapisec.kaltura.com/html5/html5lib/v2.36/mwEmbedFrame.php/p/1829221/uiconf_id/28733761/entry_id/%s?wid=_1829221&iframeembed=true&playerId=kaltura_player&entry_id=%s'

with open("primo.json", encoding='utf-8') as f:
    d = json.load(f)

docs = d['SEGMENTS']['JAGROOT']['RESULT']['DOCSET']['DOC']

records = []
for i, d in enumerate(docs):
    records.append(d['PrimoNMBib']['record']['display'])

clean_records = []


def parse_record(record):
    d = {'system_id': record['lds08']}
    d['year'] = ''.join(
            [_ for _ in record.get('creationdate', record.get('lds04', '')) if
             ord(_) >= 48 and ord(_) <= 57])
    d['series'] = record.get('ispartof', record.get('lds09', ''))
    d['episode'] = record.get('lds31', '')[
                   record.get('lds31', '').find(
                           "פרק") + 4:record.get('lds31', '').find(
                           ":")].strip()
    d['title'] = record.get('lds31', '')[
                 record.get('lds31', '').find(":") + 1:].strip()
    d['full_name'] = record.get('title')
    if record.get('language') == 'heb':
        d['language'] = 'עברית'
    elif record.get('language') == 'ara':
        d['language'] = 'ערבית'
    else:
        d['language'] = record.get('language')
    d['synopsys'] = record.get('description',
                               record.get('lds03', ''))
    d['audience'] = record.get('lds23')
    d['genres'] = [_.strip() for _ in
                   record.get('subject', '').split(sep=';')]
    d['primo_url'] = record.get('lds21')
    entry_id = record['lds41'][record['lds41'].find('entry_id/') + 9:]
    entry_id = entry_id[:entry_id.find('/')].strip()
    d['entry_id'] = entry_id
    return d


for i, record in enumerate(records):
    if "videoid=hadar" in record['lds42']:
        continue
    clean_records.append(parse_record(record))

with open("assets_file.json", "w", encoding='utf-8') as f:
    d = json.dump(clean_records, f, indent=2)

print("OK", len(clean_records))
