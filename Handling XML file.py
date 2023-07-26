import xml.etree.ElementTree as ET

# Define the file path of the dataset 
xml_file_path = "/Users/naseralausud/Desktop/Data Engineer/data.cityofnewyork.us_api_views_c3uy-2p5r_rows.xml_accessType=DOWNLOAD.xml"

# Import the dataset and check if it's available
try:
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
except FileNotFoundError as e:
    raise Exception("XML file not found. Please ensure the file path is correct.") from e


total_o3 = 0
o3_count = 0

# Calculate and display the average Ozone (O3) measure for the geo_place_name Bronx
for row in root.findall(".//row"):
    geo_place_name = row.findtext("geo_place_name")
    start_date = row.findtext("start_date")
    o3_value = row.findtext("data_value")
    measure_name = row.findtext("name")

    # Check if the data is for the Bronx, within the specified date range, and for O3 measure
    if geo_place_name == "Bronx" and start_date is not None and "2011-01-01" <= start_date <= "2015-12-31" and o3_value is not None and measure_name == "Ozone (O3)":
        total_o3 += float(o3_value)
        o3_count += 1

if o3_count > 0:
    average_o3 = total_o3 / o3_count
    print(f"Average Ozone (O3) measure for Bronx between 2011-01-01 and 2015-12-31: {average_o3:.2f}")
else:
    print("No Ozone (O3) measurements found for Bronx in the specified date range.")

highest_no2_measurement = 0
place_name_with_highest_no2 = ""
place_geo_id_with_highest_no2 = ""

# Find the place with the highest Nitrogen Dioxide (NO2) measurement 
for row in root.findall(".//row"):
    geo_place_name = row.findtext("geo_place_name")
    no2_value = row.findtext("data_value")
    measure_name = row.findtext("name")

    # Check if the NO2 value is available, is the highest so far, and for NO2 measure
    if no2_value is not None and measure_name == "Nitrogen Dioxide (NO2)" and float(no2_value) > highest_no2_measurement:
        highest_no2_measurement = float(no2_value)
        place_name_with_highest_no2 = geo_place_name
        place_geo_id_with_highest_no2 = row.findtext("geo_join_id")

# Display the place with the highest NO2 measurement
if place_name_with_highest_no2:
    print(f"Place with the highest Nitrogen Dioxide (NO2) measurement: {place_name_with_highest_no2}")
    print(f"Geo ID of the place: {place_geo_id_with_highest_no2}")
    print(f"Highest NO2 measurement: {highest_no2_measurement}")
else:
    print("No Nitrogen Dioxide (NO2) measurements found.")
