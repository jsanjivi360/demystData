def genFWF(dir_path, spec, encoding):

    # Function to format the data to fixed-width format
    def formatFixedWidth(text, width):
        width = int(width)
        return str(text).ljust(width)[:width]       # Slicing the string to remove any extra characters at the end

    # Sample data
    data = [
        {"f1": "001" , "f2": "Male", "f3": 10, "f4": "Y", "f5": "Mobile", "f6": "", "f7": "Home", "f8": "Sydney", "f9": "Australia", "f10": "001001001"},
        {"f1": "002" , "f2": "Female", "f3": 9, "f4": "N", "f5": "Landline", "f6": 1, "f7": "", "f8": "Paris", "f9": "France", "f10": "002002002"},
        {"f1": "003" , "f2": "Female", "f3": 8, "f4": "Y", "f5": "Landline", "f6": "", "f7": "Work", "f8": "London", "f9": "England", "f10": "003003003"},
        {"f1": "004" , "f2": "Male", "f3": 7, "f4": "N", "f5": "Mobile", "f6": 1, "f7": "Home", "f8": "New York", "f9": "USA", "f10": "004004004"},
        {"f1": "005" , "f2": "Female", "f3": 6, "f4": "Y", "f5": "Mobile", "f6": 1, "f7": "Home", "f8": "Tokyo", "f9": "Japan", "f10": ""}
    ]

    # Path to fixed width file
    fwf_path = dir_path + "/fixedWidthFile.txt"

    # Creating the fixed-width file
    with open(fwf_path, "w", newline = '', encoding = encoding) as file:
        # Writing the header row
        for column, width in zip(spec['ColumnNames'], spec['Offsets']):
            file.write(formatFixedWidth(column, width))
        file.write("\n")  # New line

        # Writing each row of data
        for row in data:
            for column, width in zip(spec['ColumnNames'], spec['Offsets']):
                file.write(formatFixedWidth(row[column], width))
            file.write("\n")  # New line

    return "fixedWidthFile.txt"