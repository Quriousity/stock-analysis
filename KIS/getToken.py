import os
import json
import requests

currentPath = os.getcwd()

with open(currentPath + '/KIS/conf/conf.json') as fr:
    conf = json.load(fr)
key = conf['key']
secret = conf['secret']


endpoint = '/oauth2/tokenP'
url = 'https://openapi.koreainvestment.com:9443/' + endpoint
body = {
        'grant_type': 'client_credentials',
        'appkey': key,
        'appsecret':  secret
}
res = requests.post(url, data=json.dumps(body))
token = res.json()['access_token']
conf['token'] = token
with open(currentPath + '/KIS/conf/conf.json', 'w') as fw:
    json.dump(conf, fw)