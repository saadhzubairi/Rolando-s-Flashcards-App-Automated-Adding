csv_filename = 'betterOutput.csv'
problematic_position = 8001

with open(csv_filename, 'rb') as file:
    file.seek(problematic_position)
    byte = file.read(1)
    while byte and byte != b'\n':
        print(byte)
        byte = file.read(1)
