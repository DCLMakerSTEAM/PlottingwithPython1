import pandas as pd
import geopandas as gpd
import folium
from folium.features import Choropleth

# Load your CSV data
csv_file = 'your_data.csv'
df = pd.read_csv(csv_file)

# Load the US counties shapefile
shapefile = 'path_to_your_shapefile/cb_2019_us_county_20m.shp'
gdf = gpd.read_file(shapefile)

# Merge the GeoDataFrame with your DataFrame on the county column
merged = gdf.merge(df, left_on='NAME', right_on='county', how='left')

# Create a Folium map centered around the US
m = folium.Map(location=[37.8, -96], zoom_start=4)

# Add the Choropleth layer
Choropleth(
    geo_data=merged,
    name='choropleth',
    data=merged,
    columns=['county', 'your_data_column'],
    key_on='feature.properties.NAME',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Your Data Label'
).add_to(m)

# Add layer control
folium.LayerControl().add_to(m)

# Save the map as an HTML file
m.save('map.html')
