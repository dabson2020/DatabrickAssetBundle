import dlt

# Create Expectation
sales_rules = {"rule1" : "sales_id IS NOT NULL"}

# Create empty streaming table
dlt.create_streaming_table(name = "sales_stg", expect_all_or_drop=sales_rules)

# Create a streaming table with append mode"

# Creating East Sales
@dlt.append_flow(target="sales_stg")
def east_sales():
  df = spark.readStream.table('sales_dwh.source.sales_east')
  return df

# Creating West Sales
@dlt.append_flow(target="sales_stg")
def west_sales():
  df = spark.readStream.table('sales_dwh.source.sales_west')
  return df