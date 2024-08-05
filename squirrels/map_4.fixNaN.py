import pandas as pd
import folium

# Load the CSV file
file_path = 'squirrel-data.csv'
data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Convert latitude and longitude to numeric, forcing errors to NaN
data['Squirrel Latitude (DD.DDDDDD)'] = pd.to_numeric(data['Squirrel Latitude (DD.DDDDDD)'], errors='coerce')
data['Squirrel Longitude (-DD.DDDDDD)'] = pd.to_numeric(data['Squirrel Longitude (-DD.DDDDDD)'], errors='coerce')

# Drop rows with NaN values in latitude or longitude
data = data.dropna(subset=['Squirrel Latitude (DD.DDDDDD)', 'Squirrel Longitude (-DD.DDDDDD)'])

# Initialize a map centered around an average location from the data
center_lat = data['Squirrel Latitude (DD.DDDDDD)'].mean()
center_lon = data['Squirrel Longitude (-DD.DDDDDD)'].mean()
squirrel_map = folium.Map(location=[center_lat, center_lon], zoom_start=12)

# Add points to the map
for idx, row in data.iterrows():
    folium.Marker(
        location=[row['Squirrel Latitude (DD.DDDDDD)'], row['Squirrel Longitude (-DD.DDDDDD)']],
        popup=row['Squirrel ID'],
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(squirrel_map)

# Save the map to an HTML file
squirrel_map.save('squirrel_map.html')

# Display the map in the notebook (if you're running this in a Jupyter notebook)
squirrel_map
