import pandas as pd
import folium

# Creating a DataFrame from the provided data
data = {
    'Area Name': ['UPPER MANHATTAN']*4,
    'Area ID': ['A']*4,
    'Park Name': ['Fort Tryon Park']*4,
    'Park ID': ['01']*4,
    'Squirrel ID': ['A-01-01', 'A-01-02', 'A-01-03', 'A-01-04'],
    'Primary Fur Color': ['Gray']*4,
    'Highlights in Fur Color': ['White']*4,
    'Color Notes': ['']*4,
    'Location': ['Ground Plane']*4,
    'Above Ground (Height in Feet)': ['']*4,
    'Specific Location': ['']*4,
    'Activities': ['Foraging', 'Foraging', 'Eating, Digging something', 'Running'],
    'Interactions with Humans': ['Indifferent']*4,
    'Other Notes or Observations': ['', 'Looks skinny', '', ''],
    'Squirrel Latitude (DD.DDDDDD)': [40.85941, 40.859436, 40.859416, 40.859418],
    'Squirrel Longitude (-DD.DDDDDD)': [-73.933936, -73.933937, -73.933894, -73.933895]
}

df = pd.DataFrame(data)

# Create a map centered around the average latitude and longitude
map_center = [df['Squirrel Latitude (DD.DDDDDD)'].mean(), df['Squirrel Longitude (-DD.DDDDDD)'].mean()]
squirrel_map = folium.Map(location=map_center, zoom_start=17)

# Add markers to the map
for i, row in df.iterrows():
    folium.Marker(
        location=[row['Squirrel Latitude (DD.DDDDDD)'], row['Squirrel Longitude (-DD.DDDDDD)']],
        popup=f"Squirrel ID: {row['Squirrel ID']}<br>Activities: {row['Activities']}<br>Interactions: {row['Interactions with Humans']}<br>Notes: {row['Other Notes or Observations']}"
    ).add_to(squirrel_map)

# Save the map to an HTML file
squirrel_map.save('squirrel_map.html')
squirrel_map
