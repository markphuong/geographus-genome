


counter = 10
while counter < 15:
	mybatch = open('trim.merge.fosmid.batch', 'r')

	out = open('trim.merge.fosmid.batch' + str(counter), 'w')

	for line in mybatch:
		if 'mapfile' in line:
			line = line.replace('mapfile', 'mapfile' + str(counter))
			out.write(line)
		else:
			out.write(line)
	out.close()
	counter += 1
