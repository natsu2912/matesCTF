from pwn import *
n = 0 #number of connections we tried
NUMBER_OF_FILES = 20
while True:
	right = 0
	lines = []
	#s = process('./barry')
	s = remote('125.235.240.168', 1337)

	print s.recvuntil(' number: ')
	s.send('1\n')
	input = s.recvline()[22:]
	for i in range(NUMBER_OF_FILES):
		f = open("{}".format(1), "r")
		lines = f.readlines()
		if lines[0].startswith(input):
			break
		f.close()
	if i == NUMBER_OF_FILES:
		continue

	for x in lines[1:]:
		print s.recvuntil(' number: ')
		s.send(x)
		input = s.recvline()
		print input
		if input.startswith('Wrong!'):
			break
		elif input.startswith('Corret!'):
			right = 1

	if right == 1:
		break
	else:
		n += 1
		s.close()
print 'Numeber of connections = ' + str(n)
s.interactive()
