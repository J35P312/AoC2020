import sys

input=[]
mult=1000


for line in open(sys.argv[1]):
	input.append(line.strip()*mult)

#print(input)

x=0
y=0

dx=1
dy=2

tree="#"
trees=0
print(len(input))

while y < len(input):
	if input[y][x] == tree:
		trees+=1
	x+=dx
	y+=dy

print(trees)
