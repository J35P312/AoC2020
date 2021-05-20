import sys

input=[]
for line in open(sys.argv[1]):
	input.append(line)

groups="".join(input).split("\n\n")
counts=0
for group in groups:
	answers=set(list(group.replace("\n","")))
	counts+=len(answers)

print(counts)
