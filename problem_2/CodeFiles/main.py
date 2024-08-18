import generateCSVFile as gen
import combineCSVFiles as comb
import anonymiseCSVFile as anon


def main():

        num_rows = int(1.5 * 10**7)     # Approximate number of rows to generate a 1GB file
        encoding = 'utf-8'

        file1 = "sampleData_1.csv"
        file2 = "sampleData_2.csv"
        combinedFile = "sampleData.csv"

        # Generating 2 1GB files and combining them
        gen.generateFile(num_rows, encoding, file1)
        gen.generateFile(num_rows, encoding, file2)
        comb.combineFiles(file1, file2, combinedFile, num_rows)

        anonymisedFile = 'anonymised_sampleData.csv'

        # Generating an anonymised CSV file from the 2GB CSV file
        anon.anonymiseFile(combinedFile,anonymisedFile, encoding)


if __name__ == "__main__":
        main()