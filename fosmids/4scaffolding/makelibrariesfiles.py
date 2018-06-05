


counter = 2
while counter < 11:
	mybatch = open('11756X1.libraries.txt', 'r')
	myID = '11756X' + str(counter) + '.libraries.txt'

	out = open(myID, 'w')

	for line in mybatch:
		if '11756X1' in line:
			line = line.replace('11756X1', '11756X' + str(counter))
			out.write(line)
		else:
			out.write(line)
	out.close()
	counter += 1
