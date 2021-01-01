from connect import *
import json


def updates():
    k=loadsite(page)
    k=k[k.find("{"):]
    k=k[:k.find("});")+1]

    return json.loads(k)

def transform(q):
    q=q["identifierList"]
    ret=[]
    for w in q:
        #print(json.dumps(w,indent=2))
        idd=w["identifier"]
        #print(w.keys())
        if "tickList" in w.keys() and not w["tickList"] is None:
            for tick in w["tickList"]:
                tim=tick["timestamp"]
                las=tick["last"]
                if las is None:continue
                ret.append({"id":idd,"t":tim,"q":las})
        else:
            tim=w["timestamp"]
            las=w["last"]
            if las is None:continue
            ret.append({"id":idd,"t":tim,"q":las})
    return ret

if __name__=="__main__":
    print(json.dumps(transform(updates()),indent=2))

