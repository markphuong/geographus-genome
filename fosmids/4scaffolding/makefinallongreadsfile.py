import os
import sys

files = [f for f in os.listdir('.') if os.path.isfile(f)]

out=open('longreads.fa', 'w')

counter=0
for f in files:
	if 'scaffolds.fasta' in f:
		os.system('python makesomethingNotInterleaved.py ' + f + ' ' + f + '.NI')
		myfasta = open(f + '.NI','r')
		for line in myfasta:
			if ">" in line:
				out.write(">longread" + str(counter) + '\n')
				out.write(next(myfasta))
				counter += 1

		myfasta.close()

out.close()
