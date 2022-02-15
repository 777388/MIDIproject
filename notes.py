midi = 21
note = 'A'
octave = 0
for x in range(10):
	octave = x
	if octave == 0:
		for i in range(3):
			if i == 0:
				note = 'A'
			if i == 1:
				note = 'A#'
			if i == 2:
				note = 'B'
			print(str(midi) + ' ' + note + str(octave))
			midi += 1
	else:
		for i in range(12):
			if i == 0:
				note = 'C'
			if i == 1:
				note = 'C#'
			if i == 2:
				note = 'D'
			if i == 3:
				note = 'D#'
			if i == 4:
				note = 'E'
			if i == 5:
				note = 'F'
			if i == 6:
				note = 'F#'
			if i == 7:
				note = 'G'
			if i == 8:
				note = 'G#'
			if i == 9:
				note = 'A'
			if i == 10:
				note = 'A#'
			if i == 11:
				note = 'B'
			print(str(midi) + ' ' + note + str(octave))
			midi += 1
			if midi == 129:
				exit()
			