enc = [0x10, 0x18, 0x43, 0x14, 0x15, 0x47, 0x40, 0x17, 0x10, 0x1D, 0x4B, 0x12, 0x1F, 0x49, 0x48, 0x18, 0x53, 0x54, 0x01, 0x57, 0x51, 0x53, 0x05, 0x56, 0x5A, 0x08, 0x58, 0x5F, 0x0A, 0x0C, 0x58, 0x09]
table = bytearray("".join(chr(i) for i in range(32, 128)))
flag = ''

for i in range(len(enc)):
	for j in range(len(table)):
		a1 = ~((0x20 + i) & table[j])
		a2 = ~(a1 & (0x20 + i))
		a3 = ~(a1 & table[j])
		a4 = ~(a3 & a2)
		if a4 == enc[i]:
			flag += chr(table[j])

print "RCTF{" + flag + "}"