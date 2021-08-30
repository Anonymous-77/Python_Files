import csv
from csv import writer
from csv import reader
with open('sample.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ', quotechar='|')
 for row in data:
   print(', '.join(row))
print('')

default_text = 'new Coloumn'
with open('sample.csv', 'r') as read_obj, \
        open('sample2.csv', 'w', newline='') as write_obj:
    csv_reader = reader(read_obj)
    csv_writer = writer(write_obj)
    for row in csv_reader:
        row.append(default_text)
        csv_writer.writerow(row)

print(' Adding new Coloumn')
print('')
with open('sample2.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ', quotechar='|')
 for row in data:
   print(' '.join(row))
