# -*- coding: utf8 -*-

import csv

 
user_list = ['anise', 'bluehero', 'carriewang', 'jesse0218', 'meijuily', 'meiko1101', 'millychun', 'nellydyu','paine0602', 'sezna627']

for user in user_list:
	csv_input_name = '{}.csv'.format(user)
	csv_output_name = '{}1.csv'.format(user)
	with open(csv_input_name, 'r') as csvinput:
		with open('new\\'+csv_output_name, 'w') as csvoutput:
			writer = csv.writer(csvoutput, lineterminator='\n')
			reader = csv.reader(csvinput)

			all = []
			row = next(reader)
			row.append('tag_count')
			all.append(row)

			for row in reader:
				#算row[9]有多少tag
				row_split = row[9].split('/')
				print(row_split)
				tag_count = len(row_split)-1
				print(tag_count)

				row.append(tag_count)
				all.append(row)

			writer.writerows(all)