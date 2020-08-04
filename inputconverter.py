import utm
import glob
import os
import csv
import datetime
import math

savior = []
it = 0
flag = False
path = '/*.txt'
files = glob.glob(path)
for name in files:
	with open(name, 'r') as f1:
		a = f1.readlines()
		for line in a:
			savior.append([os.path.basename(name)[:-4],str(datetime.datetime(100,1,1,11,34,59)+datetime.timedelta(0,round(float(line.split()[2]))))+"+03", utm.to_latlon(round(float(line.split()[0])),round(float(line.split()[1])),34,'S')[0], utm.to_latlon(round(float(line.split()[0])),round(float(line.split()[1])),34,'S')[1], 20])
			if flag == True:
				if (utm.to_latlon(round(float(line.split()[0])),round(float(line.split()[1])),34,'S')[1] - savior[it-1][3]) != 0:
					temp = (utm.to_latlon(round(float(line.split()[0])), round(float(line.split()[1])), 34, 'S')[0] - savior[it-1][2])/(utm.to_latlon(round(float(line.split()[0])),round(float(line.split()[1])),34,'S')[1] - savior[it-1][3])
					if temp < -1 or temp > 1:
						if math.degrees(math.asin(temp%1))>=0:
							savior[it - 1].append(math.degrees(math.asin(temp%1)))
						else:
							savior[it - 1].append(360+ math.degrees(math.asin(temp % 1)))
					else:
						if math.degrees(math.asin(temp))>=0:
							savior[it-1].append(math.degrees(math.asin(temp)))
						else:
							savior[it - 1].append(360 + math.degrees(math.asin(temp)))
				else:
					if utm.to_latlon(round(float(line.split()[0])), round(float(line.split()[1])), 34, 'S')[0] - savior[it-1][2] > 0:
						savior[it-1].append(90)
					else:
						savior[it - 1].append(180)

			it += 1
			flag = True
	savior[-1].append(0)
	flag = False


file = open('kharita_input.csv', 'w+', newline='')

# writing the data into the file
with file:
	write = csv.writer(file)
	write.writerows(savior)

