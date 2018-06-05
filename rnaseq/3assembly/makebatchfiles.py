


counter = 0
while counter < 10:
	mybatch = open('trinitybatch', 'r')

	out = open('trinitybatch' + str(counter), 'w')

	for line in mybatch:
		if 'mapfile' in line:
			line = line.replace('mapfile', 'mapfile' + str(counter))
			out.write(line)
		else:
			out.write(line)
	out.close()
	counter += 1
