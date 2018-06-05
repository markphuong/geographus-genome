import os
import sys

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
	if '-contigs.fa' in f or '-scaffolds.fa' in f:
		myfasta = open(f, 'r')

		out = open(f[:-3] + '.filtered.fa', 'w')

		for line in myfasta:
			if ">" in line:
				header = line.strip()
				seq = next(myfasta).strip()

				if len(seq) < 500:
					continue
				else:
					out.write(header + '\n')
					out.write(seq + '\n')

		out.close()
		myfasta.close()
