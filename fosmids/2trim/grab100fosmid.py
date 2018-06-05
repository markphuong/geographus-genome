import os
import sys
from Bio.Seq import reverse_complement

myfile = open('fosmid.vector.fa', 'r')


out = open('fosmid.trimmed.fa', 'w')


for line in myfile:
	if ">" in line:
		seq = next(myfile).strip()
		out.write('>fosmid|first100' + '\n')
		out.write(seq[0:100]+'\n')
		out.write('>fosmid|last100' + '\n')
		out.write(seq[-100:] + '\n')
		out.write('>fosmid_first100_rev' + '\n')
		out.write(reverse_complement(seq[0:100])+'\n')
		out.write('>fosmid_last100_rev' + '\n')
		out.write(reverse_complement(seq[-100:]) + '\n')

