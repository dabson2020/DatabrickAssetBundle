import dlt
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType

#Transformation (new column named otal_amount = quantity * price)
@dlt.view(name = 'prod_enr_view')
def prod_enr_view():
  df = spark.readStream.table('product_stg')
  df = df.withColumn('price', col('price') .cast(IntegerType()))
  return df


dlt.create_streaming_table(name = 'prod_enriched')
dlt.create_auto_cdc_flow(
target = "prod_enriched",
  source = "prod_enr_view",
  keys = ["product_id"],
  sequence_by = "last_updated",
  ignore_null_updates = None,
  apply_as_deletes = None,
  apply_as_truncates = None,
  column_list = None,
  except_column_list = None,
  stored_as_scd_type = 1,
  track_history_column_list = None,
  track_history_except_column_list = None
  )

 
  