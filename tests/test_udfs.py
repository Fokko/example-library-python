import pytest
from pyspark.sql.types import FloatType

def test_distance_to_schiphol(spark):
    from godatadriven.helpers import udfs
    spark.udf.register("distanceToShiphol", udfs.distance_to_schiphol, FloatType())
    result = spark.sql("""
        SELECT distanceToShiphol(lat, lon) as dist
        FROM locations
    """).first()
    assert round(result.dist) == 9
