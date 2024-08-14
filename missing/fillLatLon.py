import pandas as pd
import numpy as np

# Load the CSV file
file_path = 'squirrel-data.csv'  # Your file path
data = pd.read_csv(file_path, encoding='latin1')

# Group by Area Name and Park Name, then calculate the mean latitude and longitude
area_park_avg = data.groupby(['Area Name', 'Park Name'])[['Squirrel Latitude (DD.DDDDDD)', 'Squirrel Longitude (-DD.DDDDDD)']].mean()

# Function to fill missing lat/lon
def fill_missing_coords(row):
    if pd.isnull(row['Squirrel Latitude (DD.DDDDDD)']) or pd.isnull(row['Squirrel Longitude (-DD.DDDDDD)']):
        avg_coords = area_park_avg.loc[(row['Area Name'], row['Park Name'])]
        row['Squirrel Latitude (DD.DDDDDD)'] = avg_coords['Squirrel Latitude (DD.DDDDDD)']
        row['Squirrel Longitude (-DD.DDDDDD)'] = avg_coords['Squirrel Longitude (-DD.DDDDDD)']
    return row

# Apply the function to each row
data = data.apply(fill_missing_coords, axis=1)

# Save the updated file
data.to_csv('squirrel-data-filled.csv', index=False)
