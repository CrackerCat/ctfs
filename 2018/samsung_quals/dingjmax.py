l = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'j', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'j', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'j', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'j', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'j', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'j', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'j', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'j', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'j', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'j', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'j', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'j', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'j', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'j', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'j', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', 'k', ' ', ' ', ' ', 'd', ' ', ' ', ' ', 'j', ' ', ' ', ' ', 'd', ' ', ' ', ' ', 'f', ' ', ' ', ' ', 'd', ' ', ' ', ' ', 'f', ' ', ' ', ' ', 'd', ' ', ' ', ' ', 'j', ' ', ' ', ' ', 'd', ' ', ' ', ' ', 'k', ' ', ' ', ' ', 'd', ' ', 'k', ' ', 'd', ' ', 'j', ' ', 'd', ' ', 'f', ' ', 'd', ' ', 'd', ' ', 'd', ' ', 'f', ' ', 'd', ' ', 'j', ' ', 'd', 'k', 'd', 'j', 'd', 'f', 'd', 'f', 'd', 'j', 'd', 'k', 'j', 'f', 'd', ' ', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'j', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'j', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', 'd', ' ', 'k', 'j', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', 'd', ' ', 'j', ' ', ' ', 'f', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', 'f', 'k', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', 'd', ' ', ' ', 'f', ' ', ' ', ' ', ' ', 'k', ' ', ' ', 'd', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
sbox = []
var1 = 0
var2 = 0
s = bytearray('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_!')
flag = bytearray('qN7BuRx4rElDv84dgNaaNBanZf0HSHFjqOvbkFfgTRg3r')

def update_sbox(a1):
	global var1, var2
	for i in range(a1):
		var1 = (var1 + 1) % 64
		var2 = (var2 + sbox[var1]) % 64
		sbox[var1], sbox[var2] = sbox[var2], sbox[var1]
		v3 = sbox[(sbox[var1] + sbox[var2]) % 64]
	return s[v3]

def get_idx(a):
	for i in range(0x40):
		if a == s[i]:
			return i

def get_table(a1, a2):
	return s[(get_idx(a2) ^ get_idx(a1)) % 64]

def calculate_flag():
	for i in range(len(flag)):
		v1 = update_sbox(1)
		flag[i] = get_table(flag[i], v1)

for i in range(64):
	sbox.append(i)

for i in range(0, len(l) * 20, 20):
	cur = l[i / 20]
	if cur == ' ':
		continue
	else:
		update_sbox(ord(cur) * (i + 380))
		calculate_flag()
		print flag, i

print flag