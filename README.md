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

See the [intro to Python](./intro/) examples.

## Visualization Module: Matplotlib for graphs

Matplotlib makes graphs. There is a great [matplotlib tutorial](https://thepythoncodingbook.com/basics-of-data-visualisation-in-python-using-matplotlib/) about using matplotlib to create graphs. We are going to look at just a few of the examples. Feel free to go through the rest of it at your own pace if you want to learn more about matplotlib.

See the [matplotlib](./matplotlib/) examples.

## Visualization Module: Folium for points on a map

[Folium](https://python-visualization.github.io/folium/latest/#) makes it easy to put spatial data onto a map. If you have a dataset with GPS coordinates for each record, Folium will put pins on the map for each record.

See the Folium [squirrel sightings](./squirrels/) examples.

## Visualization Module: GeoPandas for counties/states on a map

[GeoPandas](https://geopandas.org/en/stable/) makes it easy to plot spatially-aggregated data on a map (for instance, number of schools per county).

See the GeoPandas [library total square footage by county](./publicLibraries/) examples.

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

Datasets are great. They have wonderful information in them. But, they may also have some errors, blanks, or garbage. Before you can get a finished visualization of your data you may need to clean up the dataset. [Types of cleaning](https://www.tableau.com/learn/articles/what-is-data-cleaning) your data might need. If your data has gaps in it it can be useful to [identifying missing values](https://github.com/ResidentMario/missingno).

## Dataset: NYC Park Squirrel Census

NYC took an [informal census](https://www.thesquirrelcensus.com/) of squirrels in some of its parks. They have made this [squirrel dataset](https://www.dropbox.com/s/b97hxtsthbidl34/squirrel-data.csv?dl=0) available for [download](https://www.dropbox.com/scl/fi/is2yaa5gz1of32xo1xwvd/squirrel-data.csv?rlkey=sao5wj2tqd98nzs6rsi5k7ot6&e=1&dl=1).

We do not know anything about this data, so let's just plot a few rows to see what we have.
* [ChatGPT](https://chatgpt.com/): Hello! I would like to graph some location data on a map.
* Paste the header and the first 4 rows of sightings
* Copy the code into your own map_1.py file
* Run it
  * python3 map_1.py

That worked great and is just what we want to visualize. Now let's look at the entire file. Since the file could be extremely large we don't want to paste it all into ChatGPT. Instead, we want ChatGPT to write us a program that will read directly from the CSV file.
* [ChatGPT](https://chatgpt.com/): Hello! I would like to graph some location data on a map. I have a CSV file that I would like to read the data from.
* Upload the CSV file
* Copy the code into your own map_2.py file
* Run it!
  * python3 map_2.py
* Oops... it crashes :(
* Fix it, run it, fix it, run it, ...

## Dataset: Public Library Survey

The Institute of Museum and Library Services provides a dataset of [public libraries](https://www.imls.gov/research-evaluation/data-collection/public-libraries-survey).

Download the [CSV](https://www.imls.gov/sites/default/files/2024-06/pls_fy2022_csv.zip) file and create a visualization showing the total square footage of library space in each US county.
* [ChatGPT](https://chatgpt.com/): I have a dataset in a CSV file. I would like to plot it on a map, grouped by county. I want to run this on my own computer. Can you write the Python code for me?
* Copy to map_1.py file
* Run it
  * python3 map_1.py
* Note that it does not look right; it is not aggregating data by county
* [ChatGPT](https://chatgpt.com/): My data has multiple rows for each county. Can you show me the code that would also sum those rows by county before plotting?
* Update your code and run it again
* Note that some of the counties will be shaded in black. These are counties for which there is no data.
  * Is it because the county has no library?
  * Is it because the county name is misspelled?
  * Or something else?
  * Who knows! You have to go digging in the data to figure that out. Welcome to the wonderful world of using someone else's data. :)
