#!/usr/bin/env python

#this concatenates all read files into read1 and read2 files [if you get multiple read files per index from illumina]

import os
import sys
import argparse
import multiprocessing

#manip these variables

ID = '.gz' #An ID common to all fastq files

### the script

directory = '/pylon5/bi4s86p/phuong/geographus.genome/4abyss.sealer/0bloomfilter'


def concat(element):
	
	newname = element.split('/')
	newname = newname[-1]
#	oldfile = newname
#	newname = newname.split('_')
#	if "geographus" in oldfile:
#		myfilename = 'UU0018MY.' + newname[2] + '.fq'
#	else:
#		myfilename = newname[0] +'.' + newname[-1][0] + '.fq'
#	print oldfile
#	print myfilename

	variables = dict(
	myfile=newname)




	commands = """
	gzip {myfile}
	""".format(**variables)

	cmd_list = commands.split("\n")
	for cmd in cmd_list:
		os.system(cmd)

mylist = []

for root, dirs, files in os.walk(directory):
	for filename in files:
		path = os.path.join(root, filename)
		if '.fq' in filename or '.fastq' in filename:
			mylist.append(path)
		else:
			continue

pool = multiprocessing.Pool(38)
pool.map(concat, mylist)


