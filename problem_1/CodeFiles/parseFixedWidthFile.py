import csv

def parseFWF(dir_path, file_name, spec, encoding):
    
    # Function to parse a single line based on the fixed column widths
    def parseFixedWidthLine(line, widths):
        parsed = []
        position = 0
        for width in widths:
            width = int(width)
            # Extracting the field using position and specified width
            field = line[position:position + width].strip()  # Strip any extra spaces
            parsed.append(field)
            # Update position to next column in the file
            position += width
        return parsed

    # Path to fixed width file
    fwf_path = dir_path + '/' + file_name

    # Path to delimited file
    dlf_path = dir_path + "/delimitedFile.csv"

    # Reading the fixed width file
    with open(fwf_path, 'r', encoding = encoding) as fixedWidthFile, open(dlf_path, 'w', newline = '', encoding = encoding) as csvFile:
        writer = csv.writer(csvFile)

        # Processing each line in the fixed-width file
        for line in fixedWidthFile:
            # Parsing the line into a list of fields
            parsedLine = parseFixedWidthLine(line, spec['Offsets'])
        
            # Writing the parsed line to the CSV file
            writer.writerow(parsedLine)