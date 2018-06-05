#!/usr/bin/env python

#flash manual: http://ccb.jhu.edu/software/FLASH/MANUAL

#this script cleans reads using trimmomatic, merges reads using flash, and creates a read1 file, read2 file (these represent paired files) and an unpaired file

import os
import sys
import argparse
#import multiprocessing


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
	adfile = 'adapters.fosmid.fa',
	read1 = element + '.R1.renamed.fq',
	read2 = element + '.R2.renamed.fq',
	read1new = element + '.R1bbmap.fq',
	read2new = element + '.R2bbmap.fq',
	read1out = element + '.R1.trimmed.fq', 
	read1unpairedout = element + '.R1.trimmedunpaired.fq',
	read2out = element + '.R2.trimmed.fq',
	read2unpairedout = element + '.R2.trimmedunpaired.fq',
	sampleID = element) #name your output


	commands = """
	cp /pylon5/bi4s86p/phuong/geographus.genome/1rename/{read1} ./
	cp /pylon5/bi4s86p/phuong/geographus.genome/1rename/{read2} ./
	/home/phuong/bbmap/bbsplit.sh in1={read1} in2={read2} ref=fosmid.vector.fa,ecoli.fa basename={sampleID}.out_%.fq outu1={sampleID}.bbmap1.fq outu2={sampleID}.bbmap2.fq > {sampleID}.bbsplit 2> {sampleID}.bbspliterr
	cutadapt -b file:cutadapt.adapters.fosmid.fa -B file:cutadapt.adapters.fosmid.fa -n 5 -o {read1new} -p {read2new} {sampleID}.bbmap1.fq {sampleID}.bbmap2.fq > {sampleID}.cutadapt 2> {sampleID}.cutadaptstderr
	java -jar $TRIMMOMATIC_HOME/trimmomatic-0.36.jar PE -threads 12 -phred33 {read1new} {read2new} {read1out} {read1unpairedout} {read2out} {read2unpairedout} ILLUMINACLIP:{adfile}:2:30:10 SLIDINGWINDOW:4:20 MINLEN:36 LEADING:15 TRAILING:15 > {sampleID}.trimm 2> {sampleID}.trimmerr
	/home/phuong/flash {read1out} {read2out} -M 125 -m 5 -x 0.05 -f 550 -o {sampleID} > {sampleID}.flash 2> {sampleID}.flasherr
	cat {sampleID}.notCombined_1.fastq > {sampleID}.final1.fq
	cat {sampleID}.notCombined_2.fastq > {sampleID}.final2.fq
	cat {read1unpairedout} {read2unpairedout} {sampleID}.extendedFrags.fastq > {sampleID}.finalunpaired.fq
	cp {sampleID}.flash /pylon5/bi4s86p/phuong/geographus.genome/2trim
	cp {sampleID}.flasherr /pylon5/bi4s86p/phuong/geographus.genome/2trim
	cp {sampleID}.final1.fq /pylon5/bi4s86p/phuong/geographus.genome/2trim
	cp {sampleID}.final2.fq /pylon5/bi4s86p/phuong/geographus.genome/2trim
	cp {sampleID}.finalunpaired.fq /pylon5/bi4s86p/phuong/geographus.genome/2trim
	cp {sampleID}.trimm /pylon5/bi4s86p/phuong/geographus.genome/2trim
	cp {sampleID}.trimmerr /pylon5/bi4s86p/phuong/geographus.genome/2trim
	cp {sampleID}.bbsplit /pylon5/bi4s86p/phuong/geographus.genome/2trim
	cp {sampleID}.bbspliterr /pylon5/bi4s86p/phuong/geographus.genome/2trim
	cp {sampleID}.out*.fq /pylon5/bi4s86p/phuong/geographus.genome/2trim
	cp {sampleID}.cutadapt /pylon5/bi4s86p/phuong/geographus.genome/2trim
	cp {sampleID}.cutadapterr /pylon5/bi4s86p/phuong/geographus.genome/2trim
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
		align(line)
#		mylist.append(line)

#this bit is really not necessary. I could have done this by not having 'def main()' and just starting with the args=get_args() line, but the following code follows the logic of what preceded it.


#pool = multiprocessing.Pool(5)
#pool.map(align, mylist)






