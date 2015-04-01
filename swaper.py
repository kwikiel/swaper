import hmac
import time
import urllib 
import hashlib
import requests

import config

class BitapiException(Exception): pass

def bitapi(method, **params):
    times = int(time.time())
    params.update({
        "method": method,
        "tonce": times
        })

    post = urllib.urlencode(params)
    sign = hmac.HMAC(config.secret, post, digestmod=hashlib.sha512).hexdigest()
    headers = {"API-Key": config.key, "API-Hash": sign}
    raw = requests.post("https://www.bitmarket.pl/api2/",data = post, headers = headers)
    
    if 'error' in raw.json():
        raise BitapiException(raw.json())

    return raw.json()

def get_cutoff():
    raw = requests.get("http://bitmarket.pl/json/swapBTC/swap.json")
    return raw.json()["cutoff"]
