import pandas as pd
import geopandas as gpd
import folium
from folium.features import Choropleth

# Load your CSV data
csv_file = 'pls_fy22_outlet_pud22i.csv'
df = pd.read_csv(csv_file, encoding='ISO-8859-1')

# Load the US counties shapefile
shapefile = 'cb_2019_us_county_20m/cb_2019_us_county_20m.shp'
gdf = gpd.read_file(shapefile)

# Convert the merge keys to lowercase
df['CNTY'] = df['CNTY'].str.lower()
gdf['NAME'] = gdf['NAME'].str.lower()

# Aggregate the data by county (e.g., summing up the values)
# Replace 'your_data_column' with the column you want to aggregate
df_aggregated = df.groupby('CNTY')['SQ_FEET'].sum().reset_index()

# Merge the GeoDataFrame with your DataFrame on the county column
merged = gdf.merge(df_aggregated, left_on='NAME', right_on='CNTY', how='left')

# Create a Folium map centered around the US
m = folium.Map(location=[37.8, -96], zoom_start=4)

# Add the Choropleth layer
Choropleth(
    geo_data=merged,
    name='choropleth',
    data=merged,
    columns=['CNTY', 'SQ_FEET'],
    key_on='feature.properties.NAME',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Square Feet'
).add_to(m)

# Add layer control
folium.LayerControl().add_to(m)

# Save the map as an HTML file
m.save('map_interactive.html')
