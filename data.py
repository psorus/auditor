from updates import *

import os



def assureint2(q):
    ret={}
    for key in q.keys():
        ret[int(key)]=q[key]
    return ret

def assureint(q):
    ret={}
    for key in q.keys():
        ret[key]=assureint2(q[key])
    return ret

def loadset():
    q="{}"
    if os.path.isfile("base.json"):
        with open("base.json","r") as f:
            q=f.read()
    return json.loads(q)

def saveset(q):
    with open("base.json","w") as f:
        f.write(json.dumps(q,sort_keys=True,indent=2))

def savejobs(j):
    with open("jobs.json","w") as f:
        f.write(json.dumps(j,sort_keys=True,indent=2))

def sizer(q):
    return len(list(q.keys()))

def loadtime():
    q="{}"
    if os.path.isfile("time.json"):
        with open("time.json","r") as f:
            q=f.read()
    return json.loads(q)

def loadjobs():
    q="[]"
    if os.path.isfile("jobs.json"):
        with open("jobs.json","r") as f:
            q=f.read()
    return json.loads(q)

def savetime(q):
    with open("time.json","w") as f:
        f.write(json.dumps(q,sort_keys=True,indent=2))

def addmore(what):
    data=loadset()
    tims=loadtime()

    jobs=[]

    for w in what:
        if not w["id"] in data.keys():
            data[w["id"]]={}
        data[w["id"]][int(w["t"])]=w["q"]
        if not w["id"] in tims.keys():
            tims[w["id"]]=0
        if tims[w["id"]]<int(w["t"]):
            if not w["id"] in jobs:jobs.append(w["id"])

    print("adding",len(what),"elements: ",sizer(data))

    savejobs(jobs)
    saveset(data)
    savetime(tims)
    return data

def timestep():
    return addmore(transform(updates()))

if __name__=="__main__":
    timestep()

