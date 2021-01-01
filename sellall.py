from investor import *
import time

data=loadset()
assets=loadassets()

def pricebykey(key):
    return data[key][sorted(data[key].keys())[-1]]

money=0.0
for key in assets.keys():
    if key=="money":
        money+=assets[key]
        continue
    money+=pricebykey(key)*assets[key]

print(money)

with open("bankinghistory.csv","a") as f:
    f.write(str(time.strftime("%d:%m:%y %H:%M:%S",time.localtime()))+" "+str(money)+"\n")



