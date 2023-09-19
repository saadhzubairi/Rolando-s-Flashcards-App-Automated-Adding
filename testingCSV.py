import csv

rows = []

# Open the CSV file in read mode
with open("MoreWords.csv", "r", encoding="utf-8") as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        rows.append(row)

print(rows[4])
    
