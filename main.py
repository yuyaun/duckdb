import duckdb

con = duckdb.connect(database=':memory:', read_only=True)


result = con.execute("""
    CREATE TABLE my_table AS
    SELECT * FROM read_csv_auto('invoices.csv')
""")

for i in range(0, 2000000, 2000):
    print(i)
    data = con.execute(f"SELECT * FROM my_table where column0 = '{i}'").fetch_df()
