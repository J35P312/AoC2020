import sys
x=0
y=0
direction=False
position={"W":0,"E":0,"N":0,"S":0}

R={
	"N":{0:"N",90:"E",180:"S",270:"W",360:"N"},
	"E":{0:"E",90:"S",180:"W",270:"N",360:"E"},
	"S":{0:"S",90:"W",180:"N",270:"E",360:"S"},
	"W":{0:"W",90:"N",180:"E",270:"S",360:"W"}
}


direction="E"

for line in open(sys.argv[1]):
	movement=line.strip()
	number=int(movement[1:])
	movement=list(movement)
	
	if movement[0] == "R":
		direction=R[direction][number]
		continue
	elif movement[0] == "L":
		direction=R[direction][360-number]
		continue
	elif movement[0] == "F":
		movement[0]=direction

	position[movement[0]]+=number

print(position)

x=abs(position["W"]-position["E"])
y=abs(position["N"]-position["S"])

print(x+y)
