import requests
import pandas as pd

from datetime import datetime

def strToDatetime(t):
    return datetime.strptime(t, '%Y%m%d')

# Get OHLC
def getOHLC(key: str, secret: str, token: str, symbol: str, start: str, end: str, interval: str):
    endpoint = '/uapi/domestic-stock/v1/quotations/inquire-daily-itemchartprice'
    url = 'https://openapi.koreainvestment.com:9443/' + endpoint

    headers = {
        'content-type': 'application/json; charset=utf-8',
        'authorization': 'Bearer {}'.format(token),
        'appkey': key,
        'appsecret': secret,
        'tr_id': 'FHKST03010100'
    }
    params = {
            'FID_COND_MRKT_DIV_CODE': 'J',
            'FID_INPUT_ISCD': symbol,
            'FID_INPUT_DATE_1': start,
            'FID_INPUT_DATE_2': end,
            'FID_PERIOD_DIV_CODE': interval,
            'FID_ORG_ADJ_PRC': '0'
    }
    res = requests.get(url, headers=headers, params=params)
    results = res.json()['output2']
    results2 = []
    time = []
    for result in results:
        time.append(strToDatetime(result['stck_bsop_date']))
        item = {}
        item['open'] = int(result['stck_oprc'])
        item['high'] = int(result['stck_hgpr'])
        item['low'] = int(result['stck_lwpr'])
        item['close'] = int(result['stck_clpr'])
        item['volume'] = int(result['acml_vol'])
        results2.append(item)
        
    df = pd.DataFrame(results2, index=time)

    return df