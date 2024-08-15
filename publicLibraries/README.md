# Dataset: Public Library Survey

The Institute of Museum and Library Services provides a dataset of [public libraries](https://www.imls.gov/research-evaluation/data-collection/public-libraries-survey). Download the [CSV](https://www.imls.gov/sites/default/files/2024-06/pls_fy2022_csv.zip) file and create a visualization showing the total square footage of library space in each US county.

```text
I have a dataset in a CSV file. I would like to plot it on a map,
grouped by county. I want to run this on my own computer.
Can you write the Python code for me?
```

Give the AI a few lines of your file so it knows what the column headers are and what some representative values are.

```text
May I give you the first few lines of my data file?
```

Follow the instructions to download the shapes file. You will need this so the program knows where to draw the boundaries for each county.


* Copy to map_1.py file
* Run it
  * python3 map_1.py
* Note that it does not look right; it is not aggregating data by county
* [ChatGPT](https://chatgpt.com/): My data has multiple rows for each county. Can you show me the code that would also sum those rows by county before plotting?
* Update your code and run it again

Note that some of the counties will be shaded in black. These are counties for which there is no data.
* Is it because the county has no library?
* Is it because the county name is misspelled?
* Or something else?
* Who knows! You have to go digging in the data to figure that out. Welcome to the wonderful world of using someone else's data. :)
