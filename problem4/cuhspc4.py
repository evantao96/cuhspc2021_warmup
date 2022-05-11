line1 = input()
notes = input()

score = 0
combo = 0

for note in notes:
	if (note == '*'):
		score += 100
		score += combo
		combo += 1

	if (note == 'o'):
		score += 50
		score += combo
		combo += 1

	if (note == 'x'): 
		combo = 0

print(score)
