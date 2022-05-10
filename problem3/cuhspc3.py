x1, y1, x2, y2 = input().split()

delta_x = abs(int(x2) - int(x1))
delta_y = abs(int(y2) - int(y1))

# queen horizontal or vertical
if (delta_x == 0 or delta_y == 0):
	print('YES')

# queen diagonal
elif (delta_x == delta_y): 
	print('YES')

# knight 
elif ((delta_x == 1 and delta_y == 2) or (delta_x == 2 and delta_y == 1)):
	print('YES')

else: 
	print('NO')
