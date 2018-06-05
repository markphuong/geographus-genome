import os
import sys
from collections import defaultdict
import multiprocessing
from os import listdir
from os.path import isfile, join




counter = 0
mapfilenum = 0

mymap = open('mapfile', 'r')



for line in mymap:
	out = open('mapfile' + str(mapfilenum), 'w')
	out.write(line.strip() + '\n')
	counter += 1
	mapfilenum += 1
