


counter = 0
while counter < 14:
	mybatch = open('scaffoldbatch', 'r')

	out = open('scaffoldbatch' + str(counter), 'w')

	for line in mybatch:
		if 'mapfile' in line:
			line = line.replace('mapfile', 'mapfile' + str(counter))
			out.write(line)
		else:
			out.write(line)
	out.close()
	counter += 1
