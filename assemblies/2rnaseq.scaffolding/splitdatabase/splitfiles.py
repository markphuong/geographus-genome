import os
import sys

myfasta = open(sys.argv[1], 'r')

counter = 0

filecounter = 0

out = open('transcripts.blat.split.fasta' + str(filecounter), 'w')

for line in myfasta:
	if ">" in line:
		if counter < 5000:
			out.write(line)
			out.write(next(myfasta))
			counter += 1
		else:
			counter = 0
			filecounter += 1
			out.close()
			out = open('transcripts.blat.split.fasta' + str(filecounter), 'w')
                        out.write(line)
                        out.write(next(myfasta))


			counter += 1
