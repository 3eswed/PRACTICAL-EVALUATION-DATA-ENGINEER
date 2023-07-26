import sqlite3
import pandas as pd

# Connect to the database
db_path = "/Users/naseralausud/Desktop/Data Engineer/acs-1-year-2015.sqlite"
conn = sqlite3.connect(db_path)

# Read the table into a DataFrame
df = pd.read_sql_query('SELECT * FROM congressional_districts', conn)

# Close the connection
conn.close()

# Filter the DataFrame based on the district name and year
district_name = "Congressional District 2 (114th Congress), Arkansas"
year = 2015
filtered_df = df[(df['name'] == district_name) & (df['year'] == year)]

# Retrieve the total population of Hispanic for the filtered district and year
total_hispanic_population = filtered_df['hispanic'].values[0]

print("Total Hispanic population in {} for the year {}: {}".format(district_name, year, total_hispanic_population))

# Find the minimum and maximum median household income
min_median_income = df['median_household_income'].min()
max_median_income = df['median_household_income'].max()

print("Minimum Median Household Income: {}".format(min_median_income))
print("Maximum Median Household Income: {}".format(max_median_income))

