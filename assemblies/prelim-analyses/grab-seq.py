import os
import sys


out = open('my-subset-seq.fa', 'w')

myfasta = open('geographus.genome.v3.fasta', 'r')


for line in myfasta:
	if "scaffold_6602" in line:
		out.write(line)
		out.write(next(myfasta))

		break
