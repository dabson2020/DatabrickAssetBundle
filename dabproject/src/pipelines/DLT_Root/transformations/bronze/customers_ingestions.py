import dlt


# Create Customers Expectations

customers_rules = {"valid_customer_id":"customer_id IS NOT NULL",
                    "valid_customer_name":"customer_name IS NOT NULL"}

# Create Streaming Table for Customers

@dlt.table(name = 'customer_stg')
@dlt.expect_all_or_drop(customers_rules)

def customer_stg():
    df = spark.readStream.table('sales_dwh.source.customers')
    return df