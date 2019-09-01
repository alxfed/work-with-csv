import pandas


df = pandas.read_csv(csvfile)
df.to_sql(table_name, conn, if_exists='append', index=False)