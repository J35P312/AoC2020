import sys
import copy
import random

operations=[]
steps=[]
nop=[]
jump=[]
i=0
for line in open(sys.argv[1]):
	content=line.split()
	operations.append(content[0])
	steps.append(int(content[1]))
	if content[0] == "nop":
		nop.append(i)

	elif content[0] == "jmp":
		jump.append(i)

	i+=1
print(steps)

p=False
while True:
	acc=0
	current=0
	new_operations=copy.copy(operations)

	if not p:
		p=True
		new_operations[random.choice(nop)]="jmp"
	else:
		p=False
		new_operations[random.choice(jump)]="nop"

	max_it=len(steps)*10
	it=0
	ok=True

	while True:
		it+=1
		if it > max_it:
			ok=False
			break

		if abs(current)  >= len(operations):
			break

		print([new_operations[current],steps[current],current,acc])


		if new_operations[current] == "acc":
			acc+=steps[current]
			current+=1

		elif new_operations[current] == "nop":
			current+=1
		elif new_operations[current] == "jmp":
			current+=steps[current]

	if ok:
		break

print(acc)
