from pwn import *

NUMBER_OF_FILES = 20
n = 0
while n < NUMBER_OF_FILES:
	f = open("{}".format(n), "w+")

	#s = process('./barry')
	s = remote('125.235.240.168', 1337)
	for i in range(NUMBER_OF_FILES):
		print s.recvuntil(' number: ')
		s.sendline("111111111")
		input = s.recvline()
		print input
		input = input[22:]
		print input
		f.write("%s" % input)

	f.close()
	s.close()
	n += 1
