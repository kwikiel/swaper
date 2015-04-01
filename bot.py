from swaper import *
amount = 0.1
cutoff = (get_cutoff()-5)



print  bitapi('swapClose',currency='BTC', id=bitapi('swapList', currency='BTC')["data"][0]["id"])
print  bitapi('swapOpen',currency='BTC', amount=amount, rate=cutoff)

