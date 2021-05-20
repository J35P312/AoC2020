import sys

def reach_bottom(begining,input,c):
	n=[]
	for entry in input[begining]:
		n.append(reach_bottom(entry,input,input[begining][entry]))
	if n:					
		return(c+sum(n)*c)
	else:
		return(c)
bags={}
for line in open(sys.argv[1]):
	#print(line)
	line=line.replace("bags","bag")
	container=line.split(" contain")[0]
	contains=line.split("contain ")[-1].split(".")[0].split(",")
	bags[container]={}
	#print(contains)
	if "no other" in line:
		continue
	for c in contains:
		#print(c)
		c=c.strip()
		if not "no other" in c:
			number=int(c.split(" ")[0])
		else:
			number=0
		id=" ".join(c.split(" ")[1:])
		bags[container][id]=number

#print(bags)

print(bags["shiny gold bag"])

tree={"shiny gold bag":{}}
last_added=set([])
for entry in bags["shiny gold bag"]:
	tree["shiny gold bag"][entry]={}

count=reach_bottom("shiny gold bag",bags,1)
	
print(count-1)
