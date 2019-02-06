file=open('running-config.cfg')
def list_ifname_ip(f):
	d={}
	k=[]
	v=[]
	for line in f:
		line=line.strip()
		word=line.split()
		for i in range (len(word)-1):
			if ('nameif'==word[i]):
				k.append(word[i+1])
			elif ('.' in word[i]):
				v.append((word[i],word[i+1]))
	for i in range(len(k)):
		d.update({k[i]:v[i]})
	return d

dic = list_ifname_ip(file)
print (dic)

#task2
f=open('running-config.cfg')
def replace_ip(fin):
	for line in fin:
		line=line.strip()
		line=line.replace("192","10")
		line=line.replace("255.255.0.0","255.0.0.0")
		line=line.replace("172","10")
		line=line.replace("255.255.255.0","255.0.0.0")
		print (line)

replace_ip(f)


#task3
fil=open('running-config.cfg')
def access_list(f):
	transit_access_in=[]
	fwmanagement_access_in=[]
	global_access =[]
	for line in f:
		line=line.strip()
		word=line.split()
		if "transit_access_in" in word:
			transit_access_in.append(line)
		if "fw-management_access_in" in word:
                        fwmanagement_access_in.append(line)
		if "global_access" in word:
                        global_access.append(line)
	print (transit_access_in)
	print(fwmanagement_access_in)
	print(global_access)

access_list(fil)
