import requests
from lxml import etree
import json


def clear_element(e):
    e.clear()
    while e.getprevious() is not None:
        del e.getparent()[0]


def parse_file(filename, tag):
    with open(filename, "rb") as f:
        context = etree.iterparse(f, tag=tag)
        for action, elem in context:
            parse_record(elem)
            clear_element(elem)


def parse_record(elem):
    print(elem.tag)


BULK_SIZE = 10000
INDX = 0
assets = requests.get(
    'http://primo.nli.org.il/PrimoWebServices/xservice/search/brief?institution=NNL&loc=local,scope:(NNL_IETV)&query=any,contains,IETV&sortField=&indx=%d&bulkSize=%d&json=true' % (
    INDX, BULK_SIZE))
with open('assets_file.xml','wb') as f:
    f.write(assets.content)

with open("assets_file.xml", encoding='utf-8') as f:
    d = json.load(f)

'''d = json.loads(str(assets.content), encoding='utf-8')'''


docs = d['sear:SEGMENTS']['sear:JAGROOT']['sear:RESULT']['sear:DOCSET']['sear:DOC']

records = []
for i, d in enumerate(docs):
    records.append(d['PrimoNMBib']['record']['display'])


clean_records=[]
for i, record in enumerate(records):
    print(i,record['lds08'])
    clean_record={'system_id':record['lds08']}
    clean_record['year']=''.join([_ for _ in record.get('creationdate',record.get('lds04','')) if ord(_)>=48 and ord(_)<=57])
    clean_record['series']=record.get('ispartof',record.get('lds09',''))
    clean_record['episode']=record.get('lds31','')[record.get('lds31','').find("פרק")+4:record.get('lds31','').find(":")].strip()
    clean_record['title']=record.get('lds31','')[record.get('lds31','').find(":")+1:].strip()
    clean_record['full_name']=record.get('title')
    if record.get('language')=='heb':
        clean_record['language']='עברית'
    elif record.get('language')=='ara':
        clean_record['language']='ערבית'
    else:
        clean_record['language']=record.get('language')
    clean_record['synopsys']=record.get('description',record.get('lds03',''))
    clean_record['audience']=record.get('lds23')
    clean_record['genres']=[_.strip() for _ in record.get('subject','').split(sep=';')]
    clean_record['primo_url']=record.get('lds21')
    clean_record['thumbnail_url']=record['lds41']
    entry_id=record['lds41'][record['lds41'].find('entry_id/')+9:]
    entry_id=entry_id[:entry_id.find('/')]
    clean_record['entry_id']=str(entry_id)
    clean_record['video_url']='https://cdnapisec.kaltura.com/html5/html5lib/v2.36/mwEmbedFrame.php/p/1829221/uiconf_id/28733761/entry_id/%s?wid=_1829221&iframeembed=true&playerId=kaltura_player&entry_id=%s'%(entry_id,entry_id)
    clean_records.append(clean_record)

with open("assets_file.json", "w") as f:
    json.dump(clean_records, f, indent=4)

print("OK")