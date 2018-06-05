#!/usr/bin/env python

#this concatenates all read files into R1 and R2 files [if you get multiple read files per index from illumina]

import os
import sys
import argparse
import multiprocessing



def get_args(): #arguments needed to give to this script
	parser = argparse.ArgumentParser(description="concatenate reads")

	#forces required argument to let it run
	required = parser.add_argument_group("required arguments") 
#	required.add_argument("--map", help="textfile with ID that relate to read files you want to concatenate. for ex., index1, index2, index3 (with new lines after each thing)", required=True) #A map file with the sample ID and the fasta file it goes to

	return parser.parse_args()

def concat(element):
	
	variables = dict(
	index = element)


	commands = """
	/home/phuong/CAP3/cap3 geographus.transcripts.fa > all.cap3.out
	cat geographus.transcripts.fa.cap.contigs geographus.transcripts.fa.cap.singlets > geographus.transcripts.cap3.fasta
	cd-hit-est -i geographus.transcripts.cap3.fasta -o geographus.transcripts.clustered.fasta -c 0.99 > geographus.cd-hit-est
	cp -p * /pylon5/bi4s86p/phuong/geographus.genome/rnaseq/5clusterall/RESULTS
	""".format(**variables)

	cmd_list = commands.split("\n")
	for cmd in cmd_list:
		os.system(cmd)


concat('tes')
#def main():
#	args = get_args() 

	#Make a list with the indexes you want to process
#	mylist = []
#	with open(args.map) as rfile:
#		for line in rfile:
#			line = line.strip()
#			mylist.append(line)


	#start the multiprocessing
#	pool = multiprocessing.Pool(10)
#	pool.map(concat, mylist)#run the function with the arguments

#if __name__ == "__main__": #run main over multiple processors
#	main()
