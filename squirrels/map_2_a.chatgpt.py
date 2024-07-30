import pandas as pd
import folium

# Load the CSV data into a DataFrame
data = pd.read_csv('path_to_your_file/squirrel-data.csv', encoding='ISO-8859-1')

# Calculate the average latitude and longitude for the initial map center
average_lat = data['Squirrel Latitude (DD.DDDDDD)'].mean()
average_lon = data['Squirrel Longitude (-DD.DDDDDD)'].mean()

# Create a Folium map centered around the average coordinates
squirrel_map = folium.Map(location=[average_lat, average_lon], zoom_start=15)

# Add markers for each squirrel sighting
for _, row in data.iterrows():
    folium.Marker(
        location=[row['Squirrel Latitude (DD.DDDDDD)'], row['Squirrel Longitude (-DD.DDDDDD)']],
        popup=f"Squirrel ID: {row['Squirrel ID']}<br>Primary Fur Color: {row['Primary Fur Color']}<br>Activities: {row['Activities']}"
    ).add_to(squirrel_map)

# Save the map to an HTML file
squirrel_map.save('squirrel_map_all.html')

# Optionally, display the map in a Jupyter notebook
# squirrel_map
