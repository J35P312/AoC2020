import sys

input=""
for line in open(sys.argv[1]):
	input+=line

passports=input.split("\n\n")

i=0
required=set(["byr","iyr","eyr","hgt","hcl","ecl","pid"])
invalid=0
for p in passports:
	i+=1
	p=p.replace("\n", " ").strip()
	p_list=p.split(" ")
	found_required=set([])

	print ("pass {}".format(i))
	print(p)

	for elem in p_list:
		key=elem.split(":")[0]
		if key in required:
			found_required.add(key)
		print(elem)

	if not found_required == required:
		print("error")
		invalid+=1


print(i-invalid)
