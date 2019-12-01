from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, col
spark = SparkSession.builder.getOrCreate()

# Extract
df = spark.read.format("csv").option("header", "true").load("/databricks-datasets/asa/planes")
# Transform
df = df.withColumn("NewCol", lit(0)).filter(col("model").isNotNull())
# Load
df.write.format("delta").mode("overwrite").saveAsTable("planes")

# Verify
resDf = spark.sql("SELECT * FROM planes")
resDf.show()