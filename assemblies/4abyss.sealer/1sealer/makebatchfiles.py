


counter = 0
while counter < 5:
	mybatch = open('abyss.sealer.batch17', 'r')

	out = open('abyss.sealer.batch17.' + str(counter), 'w')

	for line in mybatch:
		if '.fasta' in line:
                        line = line.replace('.fasta', '.fasta' + str(counter))
                        out.write(line)

		else:
			out.write(line)
	out.close()
	counter += 1
