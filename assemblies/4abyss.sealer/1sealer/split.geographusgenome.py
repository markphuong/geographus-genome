import os
import sys

myfasta = open("geographus.genome.v3.fasta", 'r')


filecounter = 0

counter = 0

out = open('geographus.genome.v3.' + str(filecounter) + '.fasta', 'w')

for line in myfasta:
	if ">" in line:
		if counter < 5000:
			out.write(line)
			out.write(next(myfasta))
			counter += 1
		else:
			out.close()
			counter = 0
			filecounter += 1
			out = open('geographus.genome.v3.' + str(filecounter) + '.fasta', 'w')
                        out.write(line)
                        out.write(next(myfasta))
                        counter += 1

