import sys
import copy

layout=[]
for line in open(sys.argv[1]):
	layout.append(list(line.strip()))

print(layout)
print(layout[0][0])

new_layout=copy.deepcopy(layout)

while True:
	print(layout)

	for i  in range(0,len(layout)):
		for j in range(0,len(layout[i])):

			if layout[i][j] == ".":
				continue

			adjacent =0

			#venster


			try:
				if layout[i-1][j] == "#" and not i == 0:
					adjacent +=1
			except:
				pass
			#hogre
			try:
				if layout[i+1][j] == "#":
					adjacent +=1
			except:
				pass

			#upp
			try:
				if layout[i][j-1] == "#" and not j == 0:
					adjacent +=1
			except:
				pass

			#ner
			try:
				if layout[i][j+1] == "#":
					adjacent +=1
			except:
				pass

			#snett upp
			try:
				if layout[i-1][j-1] == "#" and not i == 0 and not j == 0:
					adjacent +=1
			except:
				pass
			#snett ner
			try:
				if layout[i-1][j+1] == "#" and not i == 0:
					adjacent +=1
			except:
				pass

			#snett upp
			try:
				if layout[i+1][j-1] == "#" and not j == 0:
					adjacent +=1
			except:
				pass
			#snett ner
			try:
				if layout[i+1][j+1] == "#":
					adjacent +=1
			except:
				pass


			print(adjacent)	
			if adjacent == 0:
				new_layout[i][j]="#"

			if adjacent > 3:
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



