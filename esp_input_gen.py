f = open("./tst2", "r")
o = open("./out", "w")

o.write('.i 608\n.o 32\n')

for i in f:
	o.write('{0:0608b} {1:032b}\n'.format(int(i[0:152], 16), int(i[152:], 16)))
	#t = '{0:0640b}'.format(int.from_bytes(bytes.fromhex(i), 'little'))
	#o.write(t[0:608]+ " "+ t[608:]+'\n')

o.write('.e')
