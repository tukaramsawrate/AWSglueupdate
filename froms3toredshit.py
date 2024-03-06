path="s3://my-bucket/asl.csv"


dfasl=glueContext.create_dynamic_frame.from_options(
"s3",
{"paths":["s3://my-bucket/asl.csv"]},
"csv",{"withHeader", True},)


df=dfasl.toDF()

df=df.withColumn("id1",lit("a")).withColumn("id2",
lit("b"))

dfas2=glueContext.create_dynamic_frame.from_options(
"s3",
{"paths":["s3://my-bucket/asl1.csv"]},
"csv",{"withHeader", True},)


df2=dfas2.toDF()

df3=df1.union(df2)

df3.write.format("JDBC").option("user",user).
option("password","my_password").
option("dbtable","my_table").option("driver","my_driver").
load()