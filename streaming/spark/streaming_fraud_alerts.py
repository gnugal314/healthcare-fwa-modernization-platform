# Placeholder Spark Structured Streaming pattern for near-real-time fraud alerts.
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StringType, DoubleType

spark = SparkSession.builder.appName("fwa-streaming-alerts").getOrCreate()

schema = StructType() \
    .add("claim_id", StringType()) \
    .add("provider_key", StringType()) \
    .add("paid_amount", DoubleType()) \
    .add("claim_timestamp", StringType())

raw = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", "claims.raw").load()
claims = raw.select(from_json(col("value").cast("string"), schema).alias("claim")).select("claim.*")
alerts = claims.filter(col("paid_amount") > 5000)
alerts.writeStream.format("console").outputMode("append").start().awaitTermination()
