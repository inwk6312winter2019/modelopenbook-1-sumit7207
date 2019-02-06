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
def replace_ip(f):
	for key in f:
		f=f.replace("192","10")
		f=f.replace("172","10")			#there is an error
dic = list_ifname_ip(file)
print (dic)
print(replace_ip(dic))
