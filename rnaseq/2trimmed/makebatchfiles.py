


counter = 0
while counter < 10:
	mybatch = open('trim_merge', 'r')

	out = open('trim_merge' + str(counter), 'w')

	for line in mybatch:
		if 'mapfile' in line:
			line = line.replace('mapfile', 'mapfile' + str(counter))
			out.write(line)
		else:
			out.write(line)
	out.close()
	counter += 1
