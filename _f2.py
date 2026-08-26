import json, urllib.request
key = [l.split('=',1)[1].strip() for l in open('.env',encoding='utf-8') if l.startswith('FRED_API_KEY')][0]
def fred(sid, start='2015-01-01'):
    u = ('https://api.stlouisfed.org/fred/series/observations?series_id=' + sid +
         '&api_key=' + key + '&file_type=json&observation_start=' + start)
    try:
        j = json.load(urllib.request.urlopen(u, timeout=60))
        return [(o['date'], float(o['value'])) for o in j['observations'] if o['value'] != '.']
    except Exception as e:
        return [('ERR', str(e)[:60])]
out = {}
for sid in ('U6RATE','NILFWJN','LNS15026639','JTSQUR','JTSHIR','LNS13026511'):
    s = fred(sid); out[sid] = s
    tail = ' | '.join(dd + ' ' + str(vv) for dd,vv in s[-3:]) if s and s[0][0] != 'ERR' else str(s[0][1])
    print(sid.ljust(13), 'n=' + str(len(s)).rjust(4), tail)
json.dump(out, open(r'C:\Users\test\AppData\Local\Temp\claude\C--Users-test\2de140b3-6395-43fe-877c-4e5d66f5015c\scratchpad\fred2.json','w'), ensure_ascii=False)
