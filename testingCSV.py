import csv

rows = []

# Open the CSV file in read mode
with open('output.csv', 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        rows.append(row)
    
    for r in range(0,15):
        print((r+1),"\t",rows[r])