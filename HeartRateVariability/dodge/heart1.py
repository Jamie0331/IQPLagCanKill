import sys
import string
import csv

time_array = []
type_array = []
ping_array = []
heart_array = []

# length need to be 65
inputName = sys.argv[1]

outputName = 'p' + inputName

inlist = inputName.split('_')
uid = inlist[0]

f1 = open(sys.argv[1], "r")

skip1 = f1.readline()
line = f1.readline()
startT = line[0] + line[1] + line[2]

startTime = int(float(startT))
print(startTime)
while line:
    length = len(line)
    alist = []
    if length > 65:
        alist = line.split(',')
        hrv = alist[len(alist) - 1].replace('\n', '')
        hrvint = int(float(hrv))
        currentT = line[0] + line[1] + line[2]
        currentTime = int(float(currentT)) - startTime
        ping = (currentTime//30)*100
        
        if hrvint != 0 and ping <= 500:
            time_array.append(currentTime)
            ping_array.append(ping)
            type_array.append("Heart")
            heart_array.append(hrvint)
            #print(alist[len(alist)-1])
    line = f1.readline()

f1.close()

with open(outputName, mode='w', newline='') as out_csv:
    csv_writer = csv.writer(out_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['Time', 'Type', 'Ping', 'HRV', 'ID'])
    for x in range(0, len(time_array)):
        csv_writer.writerow([time_array[x], 'Heart', ping_array[x], heart_array[x], uid])