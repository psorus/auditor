import csv
import datetime

timestruct="%d:%m:%y %H:%M:%S"

times=[]
values=[]

print("reading")
with open("bankinghistory.csv") as cf:
  reader=csv.reader(cf,delimiter=" ")
  for row in reader:
    timestr=row[0]+" "+row[1]
    t=datetime.datetime.strptime(timestr,timestruct)
    
    times.append(t)
    values.append(float(row[2]))

print("read")

falling=0
growing=0

last=values[0]
for v in values:
  if not last==v:
    if last<v:
      growing+=1
    else:
      falling+=1

  last=v


print("falling",falling,"times")
print("growing",growing,"times")
