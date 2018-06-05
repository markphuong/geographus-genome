import os
import sys

myfasta = open(sys.argv[1], 'r')

out = open(sys.argv[2], 'w')

for line in myfasta:
	if ">" in line:
		header = line.strip()
		seq = next(myfasta).strip()

		if len(seq) < 1000:
			continue

		else:
			out.write(header + '\n')
			out.write(seq + '\n')

out.close()
myfasta.close()
