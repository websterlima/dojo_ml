import csv

dimensions = {}

with open('lymphography.tab', 'rb') as data:
	reader = csv.reader(data, delimiter='\t')

	headers = reader.next()

	for header in headers:
		dimensions[header] = []

	for line in reader:
		for i, dim in enumerate(line):
			if dim not in dimensions[headers[i]]:
				dimensions[headers[i]].append(dim)

	data.seek(0)
	reader.next()

	print dimensions

	with open('output.csv', 'wb') as output:
		writer = csv.writer(output, delimiter='\t')

		for line in reader:
			rowdata = []

			for i, dim in enumerate(line):
				if i == 0:
					rowdata.append(dimensions[headers[i]].index(dim))
				else:
					rowdata.append(dimensions[headers[i]].index(dim) / float(len(dimensions[headers[i]]) - 1))

			writer.writerow(rowdata)