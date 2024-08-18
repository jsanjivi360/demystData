import os
import json
import generateFixedWidthFile as gen
import parseFixedWidthFile as parse


def main():
    # Get the path to the common directory
    os.chdir("..")
    dir_path = os.path.abspath(os.curdir)

    # Path to spec JSON file
    spec_path = dir_path + '/spec.json'

    # Reading the JSON file and converting it into a Python dictionary
    with open(spec_path, 'r') as specFile:
        spec = json.load(specFile)

    # Ensuring that both the fixed width file and delimited file have the same encoding
    encoding = "utf-8"

    # Generating the fixed width file - Returns the name of the file generated
    file_name = gen.genFWF(dir_path, spec, encoding)

    # Parsing the fixed width file and converting into a csv file
    parse.parseFWF(dir_path, file_name, spec, encoding)

if __name__ == "__main__":
    main()
