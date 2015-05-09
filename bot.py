from swaper import *
import time
import datetime
while True:
    if swap_list()[0]["rate"]>get_cutoff():
        cancel_all()
        make_best()
    if (swap_list()[0]["rate"]+1)>get_cutoff():
        print "Raise rate"
    time.sleep(6000)
    print swap_list()
