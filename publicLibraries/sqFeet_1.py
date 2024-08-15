import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Load your CSV file
file_path = 'imls/pls_fy22_outlet_pud22i.csv'  # Your CSV file path
df = pd.read_csv(file_path)

# Aggregate data by 'CNTY' (County)
grouped_by_county = df.groupby('CNTY').agg({
    'LATITUDE': 'mean',  # Mean latitude for each county
    'LONGITUD': 'mean',  # Mean longitude for each county
    'SQ_FEET': 'sum'     # Sum of square footage for each county
}).reset_index()

# Create a base map centered around the average latitude and longitude
map_center = [grouped_by_county['LATITUDE'].mean(), grouped_by_county['LONGITUD'].mean()]
mymap = folium.Map(location=map_center, zoom_start=6)

# Add county markers to the map
marker_cluster = MarkerCluster().add_to(mymap)

for _, row in grouped_by_county.iterrows():
    folium.Marker(
        location=[row['LATITUDE'], row['LONGITUD']],
        popup=f"County: {row['CNTY']}<br>Total Square Footage: {row['SQ_FEET']}"
    ).add_to(marker_cluster)

# Save the map as an HTML file
output_path = 'county_square_footage_map.html'  # Path to save the map
mymap.save(output_path)

print(f"Map saved to {output_path}")
