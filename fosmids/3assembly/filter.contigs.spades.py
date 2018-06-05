import os
import sys

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
	if '.fasta' in f:
		counter = 0
		os.system('python makesomethingNotInterleaved.py ' + f + ' ' + f + '.NI')

		myfasta = open(f + '.NI', 'r')

		out = open(f[:-5] + 'filtered.spades.fa', 'w')

		for line in myfasta:
			if ">" in line:
				header = line.strip()
				seq = next(myfasta).strip()

				if len(seq) < 500:
					continue
				else:
					out.write('>contig' + str(counter) + '\n')
					out.write(seq + '\n')
					counter += 1
		out.close()
		myfasta.close()
