from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open('file.html', 'r', encoding='utf-8') as html_file:
    content = html_file.read()

# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(content, 'html.parser')

# Open a CSV file for writing
with open('output.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Word', 'Meaning', 'Frequency'])

    # Find all list items with class "entry learnable"
    entries = soup.find_all('li', class_='entry')

    for entry in entries:
        word = entry['word']
        meaning = entry.find('div', class_='definition').text
        frequency = entry['freq']

        csv_writer.writerow([word, meaning, frequency])

print("Extraction and CSV creation completed.")
