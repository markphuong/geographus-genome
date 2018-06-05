#!/usr/bin/env python

#this concatenates all read files into read1 and read2 files [if you get multiple read files per index from illumina]

import os
import sys
import argparse
import multiprocessing

#manip these variables

ID = '.gz' #An ID common to all fastq files

### the script

directory = '/pylon2/bi4s86p/phuong/geographus.genome/0data/regular'


def concat(element):
	
	newname = element.split('/')
	newname = newname[-1]
	oldfile = newname
	newname = newname.split('_')
	if "geographus" in oldfile:
		myfilename = 'UU0018MY.' + newname[2] + '.fq'
	else:
		myfilename = newname[0] +'.' + newname[-1][0] + '.fq'
	print oldfile
	print myfilename

	variables = dict(
	index = str(element),
	oldfile = str(oldfile),
	newfile = str(myfilename))




	commands = """
	echo "Processing {index}"
	echo "The newfile is {newfile}"
	cp {index} ./
	zcat {oldfile} | grep -A 3 '^@.* [^:]*:N:[^:]*:' | grep -v "^--$" | sed 's/ 1:N:0:.*/\\/1/g' | sed 's/ 2:N:0:.*/\\/2/g' > {newfile}
	cp {newfile} /pylon2/bi4s86p/phuong/geographus.genome/regular/1rename
	""".format(**variables)

	cmd_list = commands.split("\n")
	for cmd in cmd_list:
		os.system(cmd)

mylist = []

for root, dirs, files in os.walk(directory):
	for filename in files:
		path = os.path.join(root, filename)
		if ID in filename:
			if '10361X3' in filename:
				continue
			else:	
				mylist.append(path)
		else:
			continue

pool = multiprocessing.Pool(10)
pool.map(concat, mylist)


