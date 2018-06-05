#!/usr/bin/env python

#REQUIRES: novoalign and samtools
#REQUIRES: a map file, with first column as sample ID, and second file as which fasta it goes to. The reason you have different fastas for different samples is because of divergent mtDNA genomes
#elements in the map file are separated by a tab

#This script aligns your paired and unpaired reads to a reference using novoalign, and makes a pileup file using samtools

import os
import sys
import argparse
import multiprocessing

#this is a wrap around for novoalign and samtools where each sample identifier was "index#" where # was a number between 1 - 50

def get_args(): #arguments needed to give to this script
	parser = argparse.ArgumentParser(description="run novoalign")

	#forces required argument to let it run
	required = parser.add_argument_group("required arguments") 
	required.add_argument("--map", help="textfile with samples to run and what fasta file to match it to", required=True) #A map file with the sample ID and the fasta file it goes to

	return parser.parse_args()

def align(element):


	variables = dict(
	sample = element,
	read1 = element + '.trinity.left.fq',
	read2 = element + '.trinity.right.fq'
	) #name your output

	commands = """
	cp /pylon5/bi4s86p/phuong/geographus.genome/rnaseq/2trimmed/{read1} ./
	cp /pylon5/bi4s86p/phuong/geographus.genome/rnaseq/2trimmed/{read2} ./
	Trinity --seqType fq --max_memory 576G --left {read1} --right {read2} --output {sample}_trinity --CPU 12 --full_cleanup
	mv *{sample}* /pylon5/bi4s86p/phuong/geographus.genome/rnaseq/3assembly
	""".format(**variables)

	cmd_list = commands.split("\n")
	for cmd in cmd_list:
		os.system(cmd)

mylist = []
args = get_args() 
with open(args.map) as rfile:
	for line in rfile:
		line = line.strip()
		#align(line)


                mylist.append(line)

#this bit is really not necessary. I could have done this by not having 'def main()' and just starting with the args=get_args() line, but the following code follows the logic of what preceded it.


pool = multiprocessing.Pool(5)
pool.map(align, mylist)

