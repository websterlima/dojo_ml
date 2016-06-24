import csv
import numpy as np
from sklearn.naive_bayes import GaussianNB

X = []
Y = []

with open('output4.csv', 'rb') as data:
	reader = csv.reader(data, delimiter='\t')

	rowcount = 0

	for line in reader:
		X.append(map(lambda x: float(x), line[1:]))
		Y.append(int(line[0]))

		rowcount += 1

		if rowcount == 105:
			break

	gnb = GaussianNB()
	gnb = gnb.fit(X, Y)

	total = 0
	hit = 0

	for line in reader:
		_line = map(lambda x: float(x), line[1:])
		_line = np.array(_line).reshape(1, -1)

		Z = gnb.predict(_line)
		
		if  Z[0] == int(line[0]):
			hit += 1

		total += 1

	print "Resultado %d de %d (%.1f)" % (hit, total, hit / float(total) * 100)