import pandas as pd
import folium
import json

# Load your CSV file
file_path = 'imls/pls_fy22_outlet_pud22i.csv'  # Updated CSV file path
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Aggregate data by 'CNTY' (County)
grouped_by_county = df.groupby('CNTY').agg({
    'SQ_FEET': 'sum'  # Sum of square footage for each county
}).reset_index()

# Load the GeoJSON file containing county boundaries with a different encoding
geojson_path = 'gz_2010_us_050_00_500k.json'  # Updated GeoJSON file path
with open(geojson_path, encoding='ISO-8859-1') as f:
    geojson_data = json.load(f)

# Create a base map
map_center = [39.8283, -98.5795]  # Center of the US
mymap = folium.Map(location=map_center, zoom_start=5)

# Add the choropleth layer
folium.Choropleth(
    geo_data=geojson_data,
    name='choropleth',
    data=grouped_by_county,
    columns=['CNTY', 'SQ_FEET'],
    key_on='feature.properties.CNTY',  # Adjust if your GeoJSON uses a different property for counties
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Total Square Footage by County'
).add_to(mymap)

# Save the map as an HTML file
output_path = 'county_square_footage_choropleth.html'  # Path to save the map
mymap.save(output_path)

print(f"Choropleth map saved to {output_path}")
