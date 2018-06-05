import os
import sys

counter = 0

myfile = open('adapters.fosmid.fa', 'r')

out = open('cutadapt.adapters.fosmid.fa', 'w')



for line in myfile:
	if 'fosmid' in line or 'Reverse_adapter' in line or 'TruSeq_Universal_Adapter' in line:
		counter += 1
		out.write('>' + str(counter) + '\n')
		seq = next(myfile).strip()
		out.write(seq[0:14] + '\n')
		counter += 1
		out.write('>' + str(counter) + '\n')

		out.write(seq[-14:] + '\n')
