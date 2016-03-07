import csv

# open input and output files
csvfile = open('./cleanme.csv','r')
outfile = open('./clean-cleanme.csv','w')

# dictreader and writer
reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, reader.fieldnames)

#headers
writer.writeheader()

#clean
for row in reader:
    row['first_name'] = row ['first_name'].upper()
    row['zip'] = row['zip'].zfill(5)
    # I checked my code with Mary, but for some reason it's not fixing the zip codes. Not sure what's going wrong here.
    row['city'] = row['city'].replace('&nbsp;',' ')
    if int(row['amount']) > 1000:
        writer.writerow(row)