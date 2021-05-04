import sys
max_id=-1
ids=[]
for line in open(sys.argv[1]):
	row=line[0:7]
	row=row.replace("F","0")
	row=row.replace("B","1")

	col=line[7:].strip()
	col=col.replace("L","0")
	col=col.replace("R","1")

	id=8*int(row,2)+int(col,2)
	if id > max_id:
		max_id=id
	ids.append(id)
	print("{} {} {} {} {}".format(int(row,2),row,col,int(col,2),id) )

print(max_id)

ids=set(ids)

for i in range(min(ids)+1,max(ids)-1):
	if ( not i in ids ) and (i - 1 in ids)  and ( i+1 in ids): 
		print(i)
