import csv
import numpy as np
from sklearn import svm

X = []
Y = []

with open('output4.csv', 'rb') as data:
	reader = csv.reader(data, delimiter='\t')

	rowcount = 0

	for line in reader:
		X.append([1.0] + map(lambda x: float(x), line[1:]))
		Y.append(int(line[0]))

		rowcount += 1

		if rowcount == 105:
			break

	clf = svm.SVC(decision_function_shape='ovr', kernel="linear")
	clf.fit(X, Y)

	dec = clf.decision_function([[1]*19])

	total = 0
	hit = 0

	for line in reader:
		_line = [1.0] + map(lambda x: float(x), line[1:])
		_line = np.array(_line).reshape(1, -1)

		Z = clf.predict(_line)
		
		if  Z[0] == int(line[0]):
			hit += 1

		total += 1

	print "Resultado %d de %d (%.1f)" % (hit, total, hit / float(total) * 100)