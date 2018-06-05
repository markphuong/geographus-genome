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
	




	variables = dict(
	index = str(element))




	commands = """
	cp /pylon2/bi4s86p/phuong/geographus.genome/0data/regular/{index}* ./
	zcat 10361X3_140207_D00294_0079_BH8FVGADXX_1_1.txt.gz > 10361X3.orig.1.1.fq
	zcat 10361X3_140207_D00294_0079_BH8FVGADXX_1_2.txt.gz > 10361X3.orig.1.2.fq
	zcat 10361X3_140207_D00294_0079_BH8FVGADXX_2_1.txt.gz > 10361X3.orig.2.1.fq
	zcat 10361X3_140207_D00294_0079_BH8FVGADXX_2_2.txt.gz > 10361X3.orig.2.2.fq
	cat 10361X3.orig.1.1.fq 10361X3.orig.2.1.fq > 10361X3.R1.temp.fq
	cat 10361X3.orig.1.2.fq 10361X3.orig.2.2.fq > 10361X3.R2.temp.fq
	cat 10361X3.R1.temp.fq | grep -A 3 '^@.* [^:]*:N:[^:]*:' | grep -v "^--$" | sed 's/ 1:N:0:.*/\\/1/g' | sed 's/ 2:N:0:.*/\\/2/g' > 10361X3.R1.fq
	cat 10361X3.R2.temp.fq | grep -A 3 '^@.* [^:]*:N:[^:]*:' | grep -v "^--$" | sed 's/ 1:N:0:.*/\\/1/g' | sed 's/ 2:N:0:.*/\\/2/g' > 10361X3.R2.fq
	cp 10361X3.R1.fq /pylon2/bi4s86p/phuong/geographus.genome/regular/1rename
	cp 10361X3.R2.fq /pylon2/bi4s86p/phuong/geographus.genome/regular/1rename
	""".format(**variables)

	cmd_list = commands.split("\n")
	for cmd in cmd_list:
		os.system(cmd)

mylist = []

myID = '10361X3'

concat(myID)

