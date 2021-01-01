import sys
import json

page="https://my-pull.boerse.de/pull-service/ariva/identifiers?identifiers=290@16&identifiers=290@12&identifiers=3491@37&identifiers=59794@37&identifiers=4633@174&identifiers=4325@173&identifiers=32119@126&identifiers=101622823@33&identifiers=147636698@47&identifiers=127655260@47&identifiers=137319727@47&identifiers=147636699@47&identifiers=116404471@155&identifiers=143953401@155&identifiers=148223429@155&&callback=jQuery1110001669797765209613_1606410339999&_=1606410340001"



vers=sys.version
vers=vers[:vers.find(".")]
vers=float(vers)
#vers=float(vers[:vers.find(" ")].replace(".",""))
# print(vers)

if vers<3:
  import urllib
  import urllib2
else:
  # import urllib.request as u
  import urllib.parse
  import urllib.request

def loadsite(url,values=None):
  if vers<3:
    if not values is None:
      data = urllib.urlencode(values)
      req = urllib2.Request(url, data)
    else:
      req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    return the_page.decode("utf-8")
  else:
    data = urllib.parse.urlencode(values)
    # print(data)
    req = urllib.request.Request(url, data.encode("utf-8"))
    response = urllib.request.urlopen(req)
    the_page = response.read()
    return the_page.decode("utf-8")







