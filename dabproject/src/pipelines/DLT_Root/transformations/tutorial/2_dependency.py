# '''Create an End-to-End Basic pipeline'''

# import dlt

# @dlt.table(name = 'staging_orders')
# def staging_orders():
#     df = spark.readStream.table('dlt_databrick.source.orders')
#     return df

# #Creating transformed area
# @dlt.view(name = 'transformed_orders')
# def transformed_orders():
#     df = spark.readStream.table('staging_orders')
#     return df

# # Creating aggregated_orders
# @dlt.table(name = 'aggregated_orders')
# def aggregated_orders():
#     df = spark.readStream.table('transformed_orders')
#     df = df.groupBy('order_status').count()
#     return df

