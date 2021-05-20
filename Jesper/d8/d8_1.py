import sys

operations=[]
steps=[]

for line in open(sys.argv[1]):
	content=line.split()
	operations.append(content[0])
	steps.append(int(content[1]))

print(steps)
acc=0
current=0
visited=set([])
while True:
	if current in visited:
		break
	print([operations[current],steps[current],current,acc])
	visited.add(current)

	if abs(current)  > len(operations):
		break

	if operations[current] == "acc":
		acc+=steps[current]
		current+=1

	elif operations[current] == "nop":
		current+=1
	elif operations[current] == "jmp":
		current+=steps[current]


print(acc)
