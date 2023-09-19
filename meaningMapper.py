import csv
import requests

def getMeaning(s):
    # Define the API endpoint
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+s

    # Make the API request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Extract the relevant information from the response
        word = data[0]["word"]
        meanings = data[0]["meanings"]
        
        # Initialize synonyms, meaning_text, and example as empty strings
        synonyms = []
        meaning_text = ""
        example = ""
        part_of_speech = ""
        
        # Check for preferred part of speech: verb, adjective
        preferred_pos = ["verb", "adjective"]
        
        for pos in preferred_pos:
            for meaning in meanings:
                if meaning["partOfSpeech"] == pos:
                    for mean in meaning["definitions"]:
                        if "example" in mean:
                            meaning_text = mean["definition"]
                            example = mean["example"]
                            synonyms = meaning.get("synonyms", "")
                            part_of_speech = pos
                            break
            if meaning_text:
                break  # Stop searching if a preferred meaning is found
        
        # If no preferred meanings are found, use the first meaning with an example
        if not meaning_text:
            for meaning in meanings:
                if "example" in meaning["definitions"][0]:
                    meaning_text = meaning["definitions"][0]["definition"]
                    example = meaning["definitions"][0]["example"]
                    synonyms = meaning.get("synonyms", "")
                    part_of_speech = meaning["partOfSpeech"]
                    break
            if meaning_text == "":
                meaning_text = meanings[0]["definitions"][0]["definition"]
                part_of_speech = meanings[0]["partOfSpeech"]
                example = "No example"
        
        # Create the output string
        if synonyms:
            meaning_or_synonyms = "; ".join(synonyms)
        else:
            meaning_or_synonyms = meaning_text
        
        output = [word,part_of_speech,meaning_or_synonyms,example]
        
        # Print the output
        return output
    else:
        return f"Error: {response.status_code}"

rows = []
with open("output.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    i = 0
    for row in csv_reader:
            rows.append(row)

with open('betterOutput.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Word','Part of speech', 'Meaning', 'Example'])
    i = 970
    for r in rows:
         csv_writer.writerow(getMeaning(r[0]))
         i-=1
         print("done with",r[0],". ",i,"words left")