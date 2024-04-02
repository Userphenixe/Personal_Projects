import urllib.request
import urllib.parse
import json
# Using a web API To access the Geographical data for a specific location.
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'
while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break
    address = address.strip()
    parms = dict()
    parms['q'] = address
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    js = json.loads(data)
    plus_code = js['features'][0]['properties']['plus_code']
    print(plus_code)