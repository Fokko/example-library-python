import pytest
import logging

from pyspark.sql import SparkSession, Row

@pytest.fixture
def spark(request):
    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("Test Example Library") \
        .getOrCreate()

    locations = [
        Row(name='Fokko and Nynke\'s awesome home', lat=52.3541534, lon=4.6536149)
    ]
    try:
        rdd = spark.sparkContext.parallelize(locations)
        df = spark.createDataFrame(rdd)
        df.createOrReplaceTempView("locations")

        # Fix the log level of Spark
        # Normally Spark is quite chatty
        logger = logging.getLogger('py4j')
        logger.setLevel(logging.WARN)

        yield spark
    finally:
        spark.stop()
