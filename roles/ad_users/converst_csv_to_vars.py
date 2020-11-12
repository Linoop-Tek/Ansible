import csv

with open('NDA_sign.csv', 'r') as f:
	reader = csv.reader(f, delimiter=',')
	next(reader)
	for row in reader:
		full_name = row[0]
		f_name    = row[1].split(' ')[0].replace(' ', '')
		l_name    = row[1].split(' ')[-1].replace(' ', '')
		username  = row[2].split('@')[0].replace(' ', '')

		print('- { name: "%s", firstname: "%s", surname: "%s", email: "%s" }' % (username, f_name, l_name, row[2]))


# - { name: "adnan.sadiq", firstname: "Adnan", surname: "Sadiq" , email:"" }