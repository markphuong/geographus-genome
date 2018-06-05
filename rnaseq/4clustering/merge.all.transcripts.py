import os
import sys

myfiles = [f for f in os.listdir('.') if os.path.isfile(f)]

out = open('geographus.transcripts.fa', 'w')

counter = 0
for thing in myfiles:
	if "_assemblies_clustered.fasta" in thing and not ".clstr" in thing:
		os.system('python makesomethingNotInterleaved.py ' + thing + ' ' + thing + '.NI')
		myfasta = open(thing + '.NI', 'r')

		for line in myfasta:
			if ">" in line:
				out.write(">transcript" + str(counter) + '\n')
				out.write(next(myfasta).strip() + '\n')
				counter += 1
