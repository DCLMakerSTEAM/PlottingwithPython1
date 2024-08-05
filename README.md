# Data Visualization using Python

## Intro to Python

Python is the most popular language for data visualization. It has a very rich set of tools and documentation.

For this class you do not need to write any Python code. ChatGPT is going to write code for you. But, you may run into problems with the code. To solve the problems it will be useful to have a feel for what the code is doing.

Key things to understand:
* Variables
  * x = 4
  * y = x+1
  * What does y equal?
* Loops
  * Do something for every record in my data
* Conditionals
  * Sometimes you don't want to do something for EVERY record
  * Do something ONLY if this condition is met

See the [intro to Python](./intro) examples.

## Visualization Module: Matplotlib for graphs

Matplotlib makes graphs. There is a great [matplotlib tutorial](https://thepythoncodingbook.com/basics-of-data-visualisation-in-python-using-matplotlib/) about using matplotlib to create graphs. We are going to look at just a few of the examples. Feel free to go through the rest of it at your own pace if you want to learn more about matplotlib.

See the [matplotlib](./matplotlib) examples.

![Matplotlib example graph](./images/matplotlib.png)

## Visualization Module: Folium for points on a map

[Folium](https://python-visualization.github.io/folium/latest/#) makes it easy to put spatial data onto a map. If you have a dataset with GPS coordinates for each record, Folium will put pins on the map for each record.

See the Folium [squirrel sightings](./squirrels) examples.

![Folium example map](./images/folium.png)

## Visualization Module: GeoPandas for regions on a map

[GeoPandas](https://geopandas.org/en/stable/) makes it easy to plot spatially-aggregated data on a map (for instance, number of schools per county).

See the GeoPandas [library total square footage by county](./publicLibraries) examples.

![GeoPandas example map](./images/geopandas.png)

## Visualization Modules: further exploration

There are many other data visualization modules. Here are some [popular modules](https://mode.com/blog/python-data-visualization-libraries).

## Datasets

To get started looking for datasets, Google: interesting data sets.

Regional datasets
* [Durham OpenData](https://live-durhamnc.opendata.arcgis.com/)
* [data.gov (Durham, NC)](https://catalog.data.gov/dataset/?tags=durham&page=1)
* [NC State GIS datasets](https://www.lib.ncsu.edu/gis/datalist)

Various other datasets
* [Fun datasets](https://www.springboard.com/blog/data-science/15-fun-datasets-to-analyze/)
* [Beginner-friendly](https://www.kaggle.com/code/rtatman/fun-beginner-friendly-datasets)
* [Awesome public datasets](https://github.com/awesomedata/awesome-public-datasets)
* [NYC OpenData](https://opendata.cityofnewyork.us/)

## Scrubbing Data

Also called: cleaning, preprocessing.

Datasets are great. They have wonderful information in them. But, they may also have some errors, blanks, or garbage. Before you can get a finished visualization of your data you may need to clean up the dataset. [Types of cleaning](https://www.tableau.com/learn/articles/what-is-data-cleaning) your data might need. If your data has gaps, it can be useful to [identifying missing values](https://github.com/ResidentMario/missingno).
