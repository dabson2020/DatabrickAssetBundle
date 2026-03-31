# import dlt

#  # Creating Streaming Table
# @dlt.table(
#     name = 'first_stream_table'
# )

# def first_stream_table():
#     df = spark.readStream.table('dlt_databrick.source.orders')
#     return df

# # Create Materialized Table

# @dlt.table(
#     name = 'first_mat_view'
# )

# def first_mat_view():
#     df =spark.read.table('dlt_databrick.source.orders')
#     return df
                             
