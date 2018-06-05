import os
import sys



out = open('geographus.blat.output.combined', 'w')

counter = 0

while counter <63:
	mypsl = open('geographus.blat.output.' + str(counter) + '.psl', 'r')

	
	startnow = 'no'
	for line in mypsl:
		if '---------------------------------------------------------------------------------------------------------------------------------------------------------------' in line:
			startnow = 'yes'
		elif startnow == 'yes':
			out.write(line)
		else:
			continue

	mypsl.close()
	counter += 1
