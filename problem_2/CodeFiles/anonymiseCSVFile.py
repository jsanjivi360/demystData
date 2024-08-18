import csv
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace

def anonymiseFile(input_file_name, output_file_name, encoding):
    # Creating a Spark session
    spark = SparkSession.builder \
            .appName('AnonymiseCSV') \
            .master("local[*]") \
            .getOrCreate()

    # Reading the input CSV File
    df = spark.read.csv(input_file_name, header = True, inferSchema = True, encoding = encoding)

    # Masking the data
    anonymise_df = df.withColumn("first_name", regexp_replace("first_name", r".", "*")) \
                    .withColumn("last_name", regexp_replace("last_name", r".", "*")) \
                    .withColumn("address", regexp_replace("address", r".", "*"))
    
    # Writing the masked data to an output file
    anonymise_df.coalesce(1).write.csv(output_file_name, mode = 'overwrite',header = True, encoding = encoding)
    spark.stop()
