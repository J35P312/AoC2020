import sys

valid=0
for line in open(sys.argv[1]):
	content=line.strip().split()
	minimum=int(content[0].split("-")[0])
	maximum=int(content[0].split("-")[1])
	letter=content[1].split(":")[0]
	seq=content[-1]
	if seq[minimum-1] == letter and not seq[maximum-1] == letter:
		valid+=1
	if not seq[minimum-1] == letter and seq[maximum-1] == letter:
		valid+=1
	

print(valid)
