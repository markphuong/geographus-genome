import os
import sys

myfasta = open(sys.argv[1], 'r')

out = open(sys.argv[1] + '0', 'w')

counter = 0
filecounter = 0

for line in myfasta:
	if ">" in line:
		if counter < int(sys.argv[2]):
			out.write(line)
			out.write(next(myfasta))
			counter += 1
		else:
			out.close()
			filecounter += 1
			out = open(sys.argv[1] + str(filecounter), 'w')
			counter = 0
			out.write(line)
			out.write(next(myfasta))
		


