import sys
import copy

layout=[]
for line in open(sys.argv[1]):
	layout.append(list(line.strip()))

#print(layout)
#print(layout[0][0])

new_layout=copy.deepcopy(layout)

while True:
	#print(layout)

	for i  in range(0,len(layout)):
		for j in range(0,len(layout[i])):

			if layout[i][j] == ".":
				continue

			adjacent =0

			for k in range(i+1, len(layout) ):
				if layout[k][j] == "#":
					adjacent +=1
					break
				if layout[k][j] == "L":
					break

			for k in range(i-1,-1,-1 ):
				if layout[k][j] == "#":
					adjacent +=1
					break
				if layout[k][j] == "L":
					break

			for k in range(j+1, len(layout[i]) ):
				if layout[i][k] == "#":
					adjacent +=1
					break
				if layout[i][k] == "L":
					break

			for k in range(j-1,-1,-1 ):
				if layout[i][k] == "#":
					adjacent +=1
					break
				if layout[i][k] == "L":
					break


			k=i+1
			m=j+1
			while k < len(layout) and m < len(layout[i]):
				if layout[k][m] == "#":
					adjacent +=1
					break
				if layout[k][m] == "L":
					break
				k+=1
				m+=1

			k=i-1
			m=j+1
			while k > -1 and m < len(layout[i]):
				if layout[k][m] == "#":
					adjacent +=1
					break
				if layout[k][m] == "L":
					break
				k+=-1
				m+=1
			k=i-1
			m=j-1
			while k > -1 and m >-1:
				if layout[k][m] == "#":
					adjacent +=1
					break
				if layout[k][m] == "L":
					break
				k+=-1
				m+=-1
				
			k=i+1
			m=j-1
			while k < len(layout) and m > -1:
				if layout[k][m] == "#":
					adjacent +=1
					break
				if layout[k][m] == "L":
					break
				k+=1
				m+=-1
			
			#print(adjacent)	
			if adjacent == 0:
				new_layout[i][j]="#"

			if adjacent > 4:
				new_layout[i][j]="L"

				

	different = False
	for i  in range(0,len(layout)):
		for j in range(0,len(layout[i])):
			if layout[i][j] != new_layout[i][j]:
				different=True

	if not different:
		break
	layout=copy.deepcopy(new_layout)

occupied=0
for i  in range(0,len(layout)):
	for j in range(0,len(layout[i])):
		if layout[i][j] == "#":
			occupied +=1						
			
						
print(occupied)
quit()			



