import dlt
from pyspark.sql.functions import *


#Transformation for Customers

@dlt.view(name = 'customers_enr_view')
def customer_enr_view():
  df = spark.readStream.table('customer_stg')
  df = df.withColumn('customer_name',upper(col('customer_name')))
  return df


dlt.create_streaming_table(name = 'customer_enriched')
dlt.create_auto_cdc_flow(
target = "customer_enriched",
  source = "customers_enr_view",
  keys = ["customer_id"],
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

  

  