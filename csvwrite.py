import csv

header = ['Name','Email']
data = [['Ravi Mevcha', 'ravimevcha@gmail.com'],['Ayush Shah','shahaayush@outlook.com']]


with open('input_data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the data
    writer.writerows(data)