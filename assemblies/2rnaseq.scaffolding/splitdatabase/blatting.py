#!/usr/bin/env python


import os
import sys
import argparse
import multiprocessing


def get_args(): 
	parser = argparse.ArgumentParser(description="run novoalign")

	#forces required argument to let it run
	required = parser.add_argument_group("required arguments") 

	return parser.parse_args()

def align(element):



	variables = dict(
	element = element,
	number = element.split('.fasta')[-1]
	) #name your output


	commands = """
	blat geographus.genome.v2.fixed.fa {element} -noHead geographus.blat.output.{number}.psl
	""".format(**variables)



	cmd_list = commands.split("\n")
	for cmd in cmd_list:
		os.system(cmd)
mylist = []
def main():


	files = [f for f in os.listdir('.') if os.path.isfile(f)]
	for f in files:
		if 'transcripts.blat.split.fasta' in f:
			mylist.append(f)

		

	pool = multiprocessing.Pool(60)
	pool.map(align, mylist)#run the function with the arguments

if __name__ == "__main__": #run main over multiple processors
	main()







