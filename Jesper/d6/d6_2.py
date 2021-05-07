import sys

input=[]
for line in open(sys.argv[1]):
	input.append(line)

groups="".join(input).split("\n\n")

counts=0
for group in groups:
	
	individuals=group.strip().split("\n")
	answers={}
	for individual in individuals:
		for answer in individual:
			if not answer in answers:
				answers[answer]=0
			answers[answer]+=1

	for answer in answers:
		if answers[answer] == len(individuals):
			counts+=1

print(counts)
