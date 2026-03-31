import dlt

# Create Product Expectations
product_rules = {
                "valid_product_id":"product_id IS NOT NULL",
                "valid_price":"price >= 0"}

# Create Streaming Table for Products

@dlt.table(name = 'product_stg')
@dlt.expect_all_or_drop(product_rules)
def product_stg():
    df = spark.readStream.table('sales_dwh.source.products')
    return df
  




