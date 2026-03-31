import dlt
from pyspark.sql.functions import *

# CREATING A BUSINESS MAT VIEW

@dlt.table(name = 'business_sales')

def business_sales():
    df_facts = spark.read.table('fact_sales')
    df_prod = spark.read.table('dim_products')
    df_customer = spark.read.table('dim_customers')

    df_join = df_facts.join(df_prod, df_facts.product_id == df_prod.product_id, "inner")\
                     .join(df_customer, df_facts.customer_id == df_customer.customer_id,"inner")
    df_prun = df_join.select('region','category','total_amount')
    df_agg = df_prun.groupBy('region','category').agg(sum('total_amount').alias('total_sales'))

    return df_agg