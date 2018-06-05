#!/usr/bin/env python

#this concatenates all read files into read1 and read2 files [if you get multiple read files per index from illumina]

import os
import sys
import argparse
import multiprocessing



def get_args():
        parser = argparse.ArgumentParser(description="run blastx")


        required = parser.add_argument_group("required arguments")
        required.add_argument("--map", help="textfile with samples to run and what fasta file to match it to", required=True) #A map file with the sample ID and the fasta file it goes to

        return parser.parse_args()


def concat(element):
	


	variables = dict(
	sampleID = element,
	read1 = element + '_150129_D00294_0156_AC6E82ANXX_3_1.txt.gz',
	read2 = element + '_150129_D00294_0156_AC6E82ANXX_3_2.txt.gz')




	commands = """
	cp /pylon2/bi4s86p/phuong/geographus.genome/0data/matepair/{read1} ./
	cp /pylon2/bi4s86p/phuong/geographus.genome/0data/matepair/{read2} ./
	zcat {read1} | grep -A 3 '^@.* [^:]*:N:[^:]*:' | grep -v "^--$" | sed 's/ 1:N:0:.*/\\/1/g' | sed 's/ 2:N:0:.*/\\/2/g' > {sampleID}.R1.renamed.fq
	zcat {read2} | grep -A 3 '^@.* [^:]*:N:[^:]*:' | grep -v "^--$" | sed 's/ 1:N:0:.*/\\/1/g' | sed 's/ 2:N:0:.*/\\/2/g' > {sampleID}.R2.renamed.fq
	cp {sampleID}.R1.renamed.fq /pylon2/bi4s86p/phuong/geographus.genome/matepair/1rename/
	cp {sampleID}.R2.renamed.fq /pylon2/bi4s86p/phuong/geographus.genome/matepair/1rename/
	""".format(**variables)

	cmd_list = commands.split("\n")
	for cmd in cmd_list:
		os.system(cmd)

mylist = []
args = get_args() #this is where the arguments from the def args code gets called upon

with open(args.map) as rfile:
	for line in rfile:
		line = line.strip()
		mylist.append(line)


pool = multiprocessing.Pool(40)
pool.map(concat, mylist)


