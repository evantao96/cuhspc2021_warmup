n = input()
n = int(n)

blocks = {}
for i in range(n):
	hash, prehash = input().split()
	blocks[prehash] = hash

curr = 'NULL'
for i in range(n):
	print(blocks[curr])
	curr = blocks[curr]

# blocks = []
# for i in range(n):
# 	hash, prehash = input().split()
# 	blocks.append((prehash, hash))

# curr = 'NULL'
# for i in range(n):
# 	for b in blocks:
# 		if (b[0] == curr):
# 			print(b[1])
# 			curr = b[1]
