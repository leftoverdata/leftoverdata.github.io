
import duckdb
import os

folder = "./raw_mls"

os.listdir(folder)

quack = duckdb.connect("mls.db")


table_columns = {
    "dataelement": ["dataelement_code", "dataelement_text"],
    "dataseries": ["dataseries_code", "dataseries_text"],
    "industrybase": ["industrybase_code", "industrybase_text"],
    "period": ["period", "period_abbr", "period_name"],
    "srd": ["srd_code", "srd_text", "col1", "col2", "col3"]
}

for csv in os.listdir(folder):
    csv_path = os.path.join(folder, csv)
    
    table_name = csv.split('.')[-1]
    print(table_name)
    if table_name in table_columns:
        params = f", header=False, names={table_columns[table_name]}"
    else:
        params = ""

    sql = f"""
    CREATE OR REPLACE TABLE {table_name} AS
    SELECT
        *
    FROM
        read_csv('{csv_path}', sample_size = 100_000_000 {params})

    """

    query_results = quack.sql(sql)




