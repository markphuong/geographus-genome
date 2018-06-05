#!/usr/bin/env python


import os
import sys
import argparse
import multiprocessing


def get_args(): 
	parser = argparse.ArgumentParser(description="run novoalign")

	#forces required argument to let it run
	required = parser.add_argument_group("required arguments") 
	required.add_argument("--map", help="textfile with samples to run and what fasta file to match it to", required=True) 

	return parser.parse_args()

def align(element):

	ID = element
	
	r1name = '.final1.fq'  #extension of front reads
	r2name = '.final2.fq' #extension of back reads
	uname = '.finalunpaired.fq' #extension of unpaired reads

# some names for input output files

	variables = dict(
	sample = ID,
	ref = ID + '_contigs.filtered.spades.fa',
	read1 = ID + r1name,
	read2 = ID + r2name,
	unpaired =  ID + uname,
	out_paired = ID + '_out_paired',
	out_unpaired = ID + '_out_unpaired',
	outfile = ID + '_sorted'
	) #name your output

# 1. make a bowtie2 index for your contigs
# 2. align the paired reads
# 3. align the unpaired reads
# 4. make a bam file of the paired reads
# 5. make a bam file of the unpaired reads
# 6. merge the bam files
# 7. sort the bam file
# 8. index the bam file
# 9. mark duplicates
# 10. create a VCF file

	commands = """
	cp /pylon2/bi4s86p/phuong/geographus.genome/fosmids/2trim/{read1} ./
	cp /pylon2/bi4s86p/phuong/geographus.genome/fosmids/2trim/{read2} ./
	cp /pylon2/bi4s86p/phuong/geographus.genome/fosmids/2trim/{unpaired} ./
	cp /pylon2/bi4s86p/phuong/geographus.genome/fosmids/3assembly/{ref} ./
	cp /pylon2/bi4s86p/phuong/geographus.genome/fosmids/4scaffolding/{sample}.libraries.txt ./
	perl /home/phuong/sspace_basic/SSPACE_Basic_v2.0.pl -l {sample}.libraries.txt -s {ref} -T 20 -b {sample}.scaffolds.extension
	cp *scaffolds* /pylon2/bi4s86p/phuong/geographus.genome/fosmids/4scaffolding
	""".format(**variables)



	cmd_list = commands.split("\n")
	for cmd in cmd_list:
		os.system(cmd)
mylist = []
def main():
	args = get_args() 



	with open(args.map) as rfile:
		for line in rfile:
			line = line.strip()
			mylist.append(line)

	pool = multiprocessing.Pool(1)
	pool.map(align, mylist)#run the function with the arguments

if __name__ == "__main__": #run main over multiple processors
	main()







