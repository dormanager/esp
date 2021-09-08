f = open("./tst2", "r")
o = open("./out", "w")

#o.write('.i 608\n.o 32\n')
o.write('.i 608\n.o 1\n')
t = 0
for i in f:
	if t > 600000:
		#o.write('{0:0608b} {1:032b}\n'.format(int(i[0:152], 16), int(i[152:], 16)))
		o.write('{0:0608b} 1\n'.format(int(i[0:152], 16)))
	t += 1
	#t = '{0:0640b}'.format(int.from_bytes(bytes.fromhex(i), 'little'))
	#o.write(t[0:608]+ " "+ t[608:]+'\n')

o.write('.e')
