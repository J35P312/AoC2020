import sys
x=0
y=0
direction=False
x_ship=0
y_ship=0

x_wp=10
y_wp=1

direction="E"

for line in open(sys.argv[1]):
	movement=line.strip()
	number=int(movement[1:])
	movement=list(movement)
	dist_y=y_wp-y_ship
	dist_x=x_wp-x_ship

	if movement[0] == "L":
		movement[0] ="R"
		number=360-number

	if movement[0] == "R":

		if number == 90:
			y_wp=y_ship-dist_x
			x_wp=x_ship+dist_y

		elif number == 180:
			y_wp=y_ship-dist_y
			x_wp=x_ship-dist_x

		elif number == 270:
			y_wp=y_ship+dist_x
			x_wp=x_ship-dist_y

		continue
	elif movement[0] == "F":
		y_ship+=(y_wp-y_ship)*number
		y_wp=dist_y+y_ship

		x_ship+=(x_wp-x_ship)*number
		x_wp=dist_x+x_ship

		print([line.strip(),y_ship,x_ship,y_wp,x_wp])

		continue

	if movement[0] == "N":
		y_wp+=number
	elif movement[0] == "S":
		y_wp+=-number
	elif movement[0] == "E":
		x_wp+=number
	elif movement[0] == "W":
		x_wp+=-number

	print([line.strip(),y_ship,x_ship,y_wp,x_wp])

print([line.strip(),y_ship,x_ship,y_wp,x_wp])
print(abs(y_ship)+abs(x_ship))
print(y_ship)
