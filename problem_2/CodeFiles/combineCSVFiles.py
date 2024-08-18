from pyspark.sql import SparkSession

def combineFiles(file1, file2, combinedFile, num_rows):
    # Creating a Spark session
    spark = SparkSession.builder \
                        .appName("CombineCSVFiles") \
                        .getOrCreate()

    # Reading the 2 CSV files
    df1 = spark.read.csv(file1, header=True, inferSchema=True)
    df2 = spark.read.csv(file2, header=True, inferSchema=True)

    # Combining the DataFrames
    combined_df = df1.union(df2)

    # Repartitioning the dataframe
    numOfPartitions = int ( max(9, 9 * ( num_rows//(0.75 * 10 ** 7) ) ) ) 
    combined_df = combined_df.repartition(numOfPartitions)

    # Writing the combined dataframe to a new CSV file
    combined_df.coalesce(1).write.csv(combinedFile, mode = 'overwrite', header=True)
