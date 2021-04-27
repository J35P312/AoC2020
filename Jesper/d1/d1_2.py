import sys
import random

val=[]
n=3
for line in open(sys.argv[1]):
	val.append(int(line.strip()))


target=2020
while True:
	obs=random.sample(val, k=n)
	if sum(obs) == target:
		v=obs[0]
		output=[str(obs[0])]
		for j in range(1,n):
			v=v*obs[j]
			output.append(str(obs[j]))

		print("{} {}".format(":".join(output),v) )
		break



