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

DAX=[ac/DAX[0] for ac in DAX]


# print(len(tdax),len(DAX))
# exit()


plt.figure(figsize=(12,6))

plt.plot(times,values,label="My code")
plt.plot(tdax,DAX,"o",label="DAX")

alldays=[datetime.datetime(2020,12,i) for i in range(15,32)]
plt.plot(alldays,[1 for x in alldays],"o",color="black",alpha=0.5,label="days")

# plt.axhline(alldays[0])

# k=[plt.axhline(zw) for zw in alldays]
plt.plot(np.array(alldays),[1 for x in alldays],"o",color="black",alpha=0.5,label="days")

# for t in :
  # print(t)
  # plt.axhline(t,alpha="0.5",color="black")

plt.legend()
plt.xlabel("time")
plt.ylabel("money")
plt.savefig("moneyovertime.png",format="png")
plt.savefig("moneyovertime.pdf",format="pdf")

plt.show()



