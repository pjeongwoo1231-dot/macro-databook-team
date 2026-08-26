import os, json, urllib.request
key = None
for line in open('.env', encoding='utf-8'):
    if line.startswith('FRED_API_KEY'):
        key = line.split('=',1)[1].strip()
def fred(sid, start='2015-01-01'):
    u = ('https://api.stlouisfed.org/fred/series/observations?series_id=' + sid +
         '&api_key=' + key + '&file_type=json&observation_start=' + start)
    j = json.load(urllib.request.urlopen(u, timeout=60))
    return [(o['date'], float(o['value'])) for o in j['observations'] if o['value'] != '.']
out = {}
for sid in ('UNRATE','CIVPART','CNP16OV','CLF16OV','UNEMPLOY','SAHMREALTIME'):
    s = fred(sid); out[sid] = s
    print(sid.ljust(14), 'n=' + str(len(s)).rjust(4), ' 최근3: ' + ' | '.join(dd + ' ' + str(vv) for dd,vv in s[-3:]))
json.dump(out, open(r'C:\Users\test\AppData\Local\Temp\claude\C--Users-test\2de140b3-6395-43fe-877c-4e5d66f5015c\scratchpad\fred.json','w'), ensure_ascii=False)
