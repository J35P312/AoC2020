import sys
input={}
import copy

for line in open(sys.argv[1]):
	container=line.split(" contain")[0].replace("bags","bag")
	contained=line.split("contain ")[-1].strip().strip(".").replace("bags","bag").split(", ")
	input[container]=set([])
	for c in contained:
		input[container].add(c.strip("1,2,3,4,5,6,7,8,9,0").strip())
	

target_containers=set(["shiny gold bag"])
containers=len(target_containers)

while True:
	for container in input:
		for target in copy.copy(target_containers):
			if target in input[container]:
				target_containers.add(container)

	print(len(target_containers),containers)
	if len(target_containers) > containers:
		containers=len(target_containers)
	else:	
		break
		

print(target_containers)
print(len(target_containers)-1)
