arr_of_entry_id = [] 
set_by_eid = []
for x in all :
    if x.entry_id not in arr_of_entry_id:
        arr_of_entry_id.append(x.entry_id)
        set_by_eid.append(x)


arr_of_url = [] 
set_by_vurl = []
for x in all :
    if x.video_url not in arr_of_url:
        arr_of_url.append(x.video_url)
        set_by_vurl.append(x)



alldata = []
url = """https://cdnapisec.kaltura.com/html5/html5lib/v2.36/mwEmbedFrame.php/p/1829221/uiconf_id/28733761/entry_id/%s?wid=_1829221&iframeembed=true&playerId=kaltura_player&entry_id=%s"""
import re
find_eid = re.compile("entry_id/(.*)\?")
for asset in set_by_vurl:
    aurl = url % (asset.entry_id,asset.entry_id)
    #print(aurl)
    response = requests.get(aurl).text
    #print(response)
    time = findms.findall(response)[0]
    print(asset.entry_id,time)
    alldata.append((asset.entry_id,time))

all_times = [(x.entry_id, findms.findall(urllib.request.urlopen(x.video_url).read().decode("utf8"))) for x in set_by_vurl]
