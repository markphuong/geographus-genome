#!/usr/bin/env python

#flash manual: http://ccb.jhu.edu/software/FLASH/MANUAL

#this script cleans reads using trimmomatic, merges reads using flash, and creates a read1 file, read2 file (these represent paired files) and an unpaired file

import os
import sys
import argparse
import multiprocessing


# an arguments portion in the code represents necessary inputs to give to the script. I usually use this to give the program a file that contains all the unique sample IDs which should be in the read file names
def get_args():
	parser = argparse.ArgumentParser(description="run blastx")


	required = parser.add_argument_group("required arguments") 
	required.add_argument("--map", help="textfile with samples to run and what fasta file to match it to", required=True) #A map file with the sample ID and the fasta file it goes to

	return parser.parse_args()


def align(element):


	#the adapters file should have both forward and reverse, and the universal adapters
	
	#this variables dict species the names for the input/out files
	variables = dict(
	sampleID = element) #name your output


	commands = """
	cp /pylon2/bi4s86p/phuong/geographus.genome/regular/2trim/*final*.fq ./
	cp /pylon2/bi4s86p/phuong/geographus.genome/fosmids/4scaffolding/longreads.fa ./
	cp /pylon2/bi4s86p/phuong/geographus.genome/matepair/2trim/*.fastq ./
	abyss-pe np=60 k=44 name={sampleID}_kmer44 lib='pe1 pe2 pe3 pe4' mp='mp1 mp2 mp3 mp4' pe1='UU0018MY.final1.fq UU0018MY.final2.fq' pe2='10361X3.final1.fq 10361X3.final2.fq' pe3='10361X1.final1.fq 10361X1.final2.fq' pe4='9988X1.final1.fq 9988X1.final2.fq' se='UU0018MY.finalunpaired.fq 10361X3.finalunpaired.fq 10361X1.finalunpaired.fq 9988X1.finalunpaired.fq' mp1='11308X4_A_R1.fastq 11308X4_A_R2.fastq' mp2='11308X4_B_R1.fastq 11308X4_B_R2.fastq' mp3='11308X4_C_R1.fastq 11308X4_C_R2.fastq' mp4='11308X4_D_R1.fastq 11308X4_D_R2.fastq'
	cp -r *{sampleID}_kmer* /pylon2/bi4s86p/phuong/geographus.genome/assemblies/abyss
	""".format(**variables)

	#this bit of code executes the command

	cmd_list = commands.split("\n")
	for cmd in cmd_list:
		os.system(cmd)

mylist = []


args = get_args() #this is where the arguments from the def args code gets called upon

with open(args.map) as rfile:
	for line in rfile:
		line = line.strip()
		mylist.append(line)

#this bit is really not necessary. I could have done this by not having 'def main()' and just starting with the args=get_args() line, but the following code follows the logic of what preceded it.


pool = multiprocessing.Pool(1)
pool.map(align, mylist)






