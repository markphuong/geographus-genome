import os
import sys


genefamily = 'A'

myfile = open('helena.nt.fa', 'r')

out = open('supFamsubset.fa', 'w')


for line in myfile:
	if ">" in line:
		if "supFam:" + genefamily in line:
			out.write(line)
			out.write(next(myfile))
