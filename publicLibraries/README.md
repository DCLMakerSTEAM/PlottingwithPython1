# Dataset: Public Library Survey

The Institute of Museum and Library Services provides a dataset of [public libraries](https://www.imls.gov/research-evaluation/data-collection/public-libraries-survey). Download the [CSV](https://www.imls.gov/sites/default/files/2024-06/pls_fy2022_csv.zip) file and create a visualization showing the total square footage of library space in each US county.

```text
I have a dataset in a CSV file. I would like to plot it on a map,
grouped by county. I want to run this on my own computer.
Can you write the Python code for me?
```

The AI will likely just go ahead and write an example program with instructions for us to finish it. We want the AI to do all of the coding, so we need to give it more information.

One of the key things missing is that the AI does not know what our data looks like. Give the AI a few lines of your file so it knows what the column headers are and what some representative values are. Often we do not want to upload the entire file. Maybe it is very large of maybe it has sensitive data in it. Upload just the first few lines or even only just the first line (the column names).

```text
May I give you the first few lines of my data file?
```

The AI went ahead and wrote the program, ran it, generated the output, and gave the output to me to download. While that was very generous, we want to get the actual code. Also, the output it generated wasn't exactly what we were looking for. We should give it more information.

```text
Can you aggregate square footage data by county and then
display each county on a map?
Also, instead of running it yourself can you give me the code
so I can run it on my computer?
```

Note that the code it generates wants you to fill in your file name. Tell the AI your local file name so that you don't have to keep making this change any time you ask for a new version of the program.

```text
My local CSV file is called imls/pls_fy22_outlet_pud22i.csv
```

Download this program and run it. It will fail with a `UnicodeDecodeError` message. Paste the entire message into the AI. The AI will update the program for you. Download and run it.

This time the program will generate the map. Yay! You will get a warning, but if you paste that warning into the AI it will tell you it can be ignored.

The map that the AI generated looks like it is probably correct, but it does not tell us much. To see each county we would need to click on its pin. We really want to shade in each county with a color that represents the square footage in relation to other counties.

```text
Thank you for that map. It worked fine. Instead of putting pins on the map, could
you shade in the county with a color that represents how much square footage there
is relative to other counties?
```

Follow the instructions to download the [GeoJSON](https://geojson.org/) shapes file. This tells the program where to draw the boundaries for each county.

Once you have the shapes file downloaded, ask the AI to generate the code. Save that code and run it.

Note that some of the counties will be shaded in black. These are counties for which there is no data.
* Is it because the county has no library?
* Is it because the county name is misspelled?
* Or something else?
* Who knows! You have to go digging in the data to figure that out. Welcome to the wonderful world of using someone else's data. :)
