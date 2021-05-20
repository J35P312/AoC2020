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
	found_ok=set([])

	#print ("pass {}".format(i))
	#print(p)
	ok=True
	
	for elem in p_list:
		key=elem.split(":")[0]
		try:
			entry=elem.split(":")[1]
		except:
			continue

		if key == "byr":
			try:
				if int(entry) > 1919 and int(entry) < 2003:
					 found_ok.add("byr")
			except:
				pass

		elif key == "iyr":
			try:
				if int(entry) > 2009 and int(entry) < 2021:
					 found_ok.add("iyr")
			except:
				pass

		elif key == "eyr":
			try:
				if int(entry) > 2019 and int(entry) < 2031:
					 found_ok.add("eyr")
			except:
				pass
		elif key == "hgt":
			try:
				if entry.endswith("cm"):
					entry=entry.replace("cm","")
					if int(entry) > 149 and int(entry) < 194:
						found_ok.add("hgt")
				elif entry.endswith("in"):
					entry=entry.replace("in","")
					if int(entry) > 58 and int(entry) < 77:
						found_ok.add("hgt")
			except:
				pass
		elif key == "hcl":
			if len(entry) == 7:
				if entry[0] == "#":
					if "".join( (list(entry)[1:]) ).isalnum():
						found_ok.add("hcl")
		elif key == "ecl":
			if entry in set(["amb","blu","brn","gry","grn","hzl","oth"]):
				found_ok.add("ecl")
		elif key == "pid":
			if len(entry) == 9:
				try: 
					tmp=int(entry)
					found_ok.add("pid")
				except:
					pass
		else:
			print(key)


	if not found_ok == required:
		invalid+=1
		print(p)

		print("error")
		print(found_ok)


print(i-invalid)
