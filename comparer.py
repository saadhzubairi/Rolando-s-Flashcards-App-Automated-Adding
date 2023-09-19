import csv
rowsM = []
rowsO = []
rowsN = []

with open("MagooshWords.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        rowsM.append(row)
    
with open("output.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        rowsO.append(row[0])

i = 0
for word in rowsM:
    if word[0] in rowsO:
        print(word[0],"is common!")
        i+=1
    else:
        rowsN.append(word)

with open('more_output.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    for entry in rowsN:
        csv_writer.writerow([entry[0],entry[2],entry[1],entry[3]])
    