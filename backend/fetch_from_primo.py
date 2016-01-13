import json

import requests


def parse_record(elem):
    print(elem.tag)


BULK_SIZE = 10000
INDX = 0
assets = requests.get(
        'http://primo.nli.org.il/PrimoWebServices/xservice/search/brief?institution=NNL&loc=local,scope:(NNL_IETV)&query=any,contains,IETV&sortField=&indx=%d&bulkSize=%d&json=true' % (
            INDX, BULK_SIZE))
assets.raise_for_status()

with open('assets_file.json', 'wb') as f:
    f.write(assets.content)

print("Done.")