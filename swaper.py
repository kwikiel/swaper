import hmac
import time
import urllib 
import hashlib
import requests

import config

class BitapiException(Exception): pass

def bitapi(method, **params):
    """Main method for bitmarket API"""
    times = int(time.time())
    params.update({
        "method": method,
        "tonce": times,
        "currency": "BTC"
        })

    post = urllib.urlencode(params)
    sign = hmac.HMAC(config.secret, post, digestmod=hashlib.sha512).hexdigest()
    headers = {"API-Key": config.key, "API-Hash": sign}
    raw = requests.post("https://www.bitmarket.pl/api2/",data = post, headers = headers)
    
    if 'error' in raw.json():
        raise BitapiException(raw.json())

    return raw.json()

def get_cutoff():
    """Returns max profit for swaps """
    raw = requests.get("http://bitmarket.pl/json/swapBTC/swap.json")
    return raw.json()["cutoff"]

def cancel_all():
    """Powerful: cancels all open swaps """
    swap_list = bitapi("swapList")["data"]
    for swap in swap_list:
        bitapi("swapClose", id=swap["id"])
