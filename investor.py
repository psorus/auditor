from data import *
import math
import time

jobs=loadjobs()
data=loadset()
tims=loadtime()

print("investing*"+str(len(jobs)))
print(jobs)

alpha=0.1
deltaT=1000
srelmin=0.0001
frac=0.1
minhits=10

def mean(q):

    ret=q[0]
    for i in range(1,len(q)):
        ret=ret*(1-alpha)+alpha*q[i]
    return ret

def std(q,m=None):
    if m is None:m=mean(q)
    ret=(q[0]-m)**2
    for i in range(1,len(q)):
        ret=ret*(1-alpha)+alpha*(q[i]-m)**2
    return math.sqrt(ret)

def golist(q):
    ret=[]
    for key in sorted(q.keys()):
        ret.append(q[key])
    return ret

def loadassets():
    q='{"money":1}'
    if os.path.isfile("assets.json"):
        with open("assets.json","r") as f:
            q=f.read()
    return json.loads(q)
def saveassets(q):
    with open("assets.json","w") as f:
        f.write(json.dumps(q,indent=2))

a=loadassets()

def buy(what,price):
    global a
    dm=a["money"]*frac
    a["money"]-=dm
    if not what in a.keys():a[what]=0.0
    a[what]+=dm/price
    print("bougth",dm/price,what,"for",dm)
    with open("history.csv","a") as f:
        f.write(str(time.time())+" bougth "+str(dm/price)+" "+str(what)+" for "+str(dm)+"\n")
    

def sell(what,price):
    global a
    if not what in a.keys():return
    if a[what]==0.0:return
    a["money"]+=a[what]*price
    print("sold",a[what],what,"for",a[what]*price)
    with open("history.csv","a") as f:
        f.write(str(time.time())+" sold "+str(a[what])+" "+str(what)+" for "+str(a[what]*price)+"\n")
        
    a[what]=0.0

for job in jobs:
    l=golist(data[job])
    lkey=sorted(data[job].keys())[-1]
    update=False
    if len(l)<minhits:continue
    m=mean(l)
    s=std(l,m)
    srel=s/(m+0.001)
    las=l[-1]
    if srel<srelmin:continue
    if m-s>las:
        buy(job,las)
        update=True
    if m<las:
        sell(job,las)
        update=True
    if update:tims[job]=int(lkey)+deltaT
    print(m,s,las,srel)

saveassets(a)
jobs=[]
savejobs(jobs)
savetime(tims)

