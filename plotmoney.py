import csv
import datetime
import matplotlib.pyplot as plt
import numpy as np

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

tdax=[datetime.datetime(2020,12,i) for i in [15,16,17,18,21,22,23,28,29,30]]
DAX=[13362.87,13565.98,13667.25,13630.51,13246.30,13418.11,13587.23,12790.29,12761.38,13718.78]

tdax2=[datetime.datetime(2021,1,i) for i in [4,5,6,7,8,11,12,13,14,15,18,19,20,21,22,25,26,27,28,29]]
DAX2=[13726.74,13651.22,13891.97,13968.24,14049.53,13936.66,13925.06,13939.71,13988.70,13787.73,13848.35,13815.16,13921.73,13906.67,13873.97,13643.95,13870.99,13620.46,13665.93,13432.87]
for zw in tdax2:tdax.append(zw)
for zw in DAX2:DAX.append(zw)

tdax3=[datetime.datetime(2021,2,i) for i in [1,2,3,4]]
DAX3=[13622.02,13835.16,13933.63,13982.96]
for zw in tdax3:tdax.append(zw)
for zw in DAX3:DAX.append(zw)


DAX=[ac/DAX[0] for ac in DAX]


# print(len(tdax),len(DAX))
# exit()


plt.figure(figsize=(12,6))

plt.plot(times,values,label="My code")
plt.plot(tdax,DAX,"o",label="DAX")

#alldays=[datetime.datetime(2020,12,i) for i in range(15,32)]
#plt.plot(alldays,[1 for x in alldays],"o",color="black",alpha=0.5,label="days")

# plt.axhline(alldays[0])

# k=[plt.axhline(zw) for zw in alldays]
#plt.plot(np.array(alldays),[1 for x in alldays],"o",color="black",alpha=0.5,label="days")

# for t in :
  # print(t)
  # plt.axhline(t,alpha="0.5",color="black")

plt.legend()
plt.xlabel("time")
plt.ylabel("money")
plt.savefig("moneyovertime.png",format="png")
plt.savefig("moneyovertime.pdf",format="pdf")

plt.show()



