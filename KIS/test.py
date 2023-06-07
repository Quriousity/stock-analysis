import os
import json

from functions.functions import getOHLC

# Import Configurations
currentPath = os.getcwd()
with open(currentPath + '/KIS/conf/conf.json') as fr:
    conf = json.load(fr)
key = conf['key']
secret = conf['secret']
token = conf['token']

# get OHLCV
symbol = '005930'
start = '20230101'
end = '20230303'
df = getOHLC(key, secret, token, symbol, start, end, 'D')
print(df)