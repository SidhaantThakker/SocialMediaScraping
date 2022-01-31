import csv
with open('input_data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
            print(row['Name'], row['Email'])