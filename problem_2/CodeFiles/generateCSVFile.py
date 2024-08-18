from faker import Faker
from pyspark.sql import SparkSession
from pyspark.sql import Row
from concurrent.futures import ProcessPoolExecutor, as_completed


# Initialising Faker
fake = Faker()

# Function to generate fake data
def generate_fake_data(n):
    data = []
    for _ in range(n):
        data.append(Row(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            address=fake.address().replace("\n", " "),
            date_of_birth=fake.date_of_birth()
        ))
    return data        

def generateFile(num_rows, encoding, file_name):

    # Creating Spark session using all available cores
    spark = SparkSession.builder \
        .appName("GenerateCSVWithPySpark") \
        .master("local[*]") \
        .getOrCreate()

    # Function to generate fake data parallely
    def parallel_data_generation(total_rows, num_workers):
        rows_per_worker = total_rows // num_workers
        with ProcessPoolExecutor(max_workers=num_workers) as executor:
            futures = [executor.submit(generate_fake_data, rows_per_worker) for _ in range(num_workers)]
            results = []
            for future in as_completed(futures):
                results.extend(future.result())
        return results

    data = parallel_data_generation(num_rows, 32)

    # Calculation for number of partitions
    numOfPartitions = int ( max(9, 9 * ( num_rows//(0.75 * 10 ** 7) ) ) ) 

    # Parallelizing the data
    rdd = spark.sparkContext.parallelize(data, numSlices = numOfPartitions)

    # Converting RDD to DataFrame and repartitioning it
    df = spark.createDataFrame(rdd)
    df = df.repartition(numOfPartitions)

    # Writing the DataFrame to a single CSV file
    df.coalesce(1).write.csv(file_name, header=True, mode = "overwrite", encoding = encoding)

    # Stopping the Spark session
    spark.stop()

