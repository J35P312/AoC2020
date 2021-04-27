import sys


val=[]
for line in open(sys.argv[1]):
	val.append( int(line.strip()))

v=2020
for i in range(0,len(val)):
	for j in range(0,len(val)):
		if i == j:
			continue
		if val[i] + val[j] == v:
			print("{} {} {}".format(val[i],val[j],val[i]*val[j]))
