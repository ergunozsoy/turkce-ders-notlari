#!/usr/bin/env python3
"""content.json icerigini app_template.html sablonuna gomerek index.html uretir."""
import json, sys, os
HERE=os.path.dirname(os.path.abspath(__file__))
tpl=open(os.path.join(HERE,'app_template.html'),encoding='utf-8').read()
data=open(os.path.join(HERE,'content.json'),encoding='utf-8').read()
json.loads(data)  # dogrulama
out=tpl.replace('/*__DATA__*/','window.DATA = '+data+';')
if '/*__DATA__*/' in out: sys.exit('HATA: yer tutucu bulunamadi')
open(os.path.join(HERE,'index.html'),'w',encoding='utf-8').write(out)
print('index.html uretildi (%.1f KB)'%(len(out.encode())/1024))
