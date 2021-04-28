import sys

valid=0
for line in open(sys.argv[1]):
	content=line.strip().split()
	minimum=int(content[0].split("-")[0])
	maximum=int(content[0].split("-")[1])
	letter=content[1].split(":")[0]
	seq=content[-1]
	if (seq.count(letter) < minimum or seq.count(letter) > maximum):
		continue

	valid+=1
	

print(valid)
