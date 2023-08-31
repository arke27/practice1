import pyspark as ps
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("example").getOrCreate()

df = spark.read.csv('Bengaluru_House_Data.csv',header=True,inferSchema=True)



