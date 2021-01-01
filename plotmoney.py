import csv
import datetime
import matplotlib.pyplot as plt

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
plt.legend()
plt.xlabel("time")
plt.ylabel("money")
plt.savefig("moneyovertime.png",format="png")
plt.savefig("moneyovertime.pdf",format="pdf")

plt.show()



