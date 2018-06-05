import os
import sys

myfasta = open(sys.argv[1], 'r')

out = open(sys.argv[2], 'w')

counter = 0
for line in myfasta:
	if ">" in line:
		
		out.write('>contig' + str(counter)  + '\n')
		out.write(next(myfasta))
		counter += 1
