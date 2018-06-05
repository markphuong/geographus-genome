import os
import sys

myfile = open('test', 'r')

out = open('filtered-blast-files', 'w')

for line in myfile:
	info = line.strip().split('\t')

	if 'post' in line:
		continue
	elif int(info[3]) > 400 and 'geographus' in line:
		out.write(line)
	else:
		continue

	
