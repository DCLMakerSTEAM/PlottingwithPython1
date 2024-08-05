# Dataset: NYC Park Squirrel Census

NYC took an [informal census](https://www.thesquirrelcensus.com/) of squirrels in some of its parks. They have made this [squirrel dataset](https://www.dropbox.com/s/b97hxtsthbidl34/squirrel-data.csv?dl=0) available for [download](https://www.dropbox.com/scl/fi/is2yaa5gz1of32xo1xwvd/squirrel-data.csv?rlkey=sao5wj2tqd98nzs6rsi5k7ot6&e=1&dl=1).

We do not know anything about this data, so let's just plot a few rows to see what we have.
* [ChatGPT](https://chatgpt.com/): Hello! I would like to graph some location data on a map.
* Paste the header and the first 4 rows of sightings
* Copy the code into your own `map_1.first4rows.py` file
* Run it
  * python3 `map_1.first4rows.py`

That worked great and is just what we want to visualize. Now let's visualize the entire file. Since the file could be extremely large we want ChatGPT to write us a program that will read directly from the CSV file.
* [ChatGPT](https://chatgpt.com/): Hello! I would like to graph some location data on a map. I have a CSV file that I would like to read the data from.
* Upload the CSV file (or a smaller version with only a few lines)
* Copy the code into your own `map_2.readfile.py` file
* Run it!
  * `python3 map_2.readfile.py`
* Oops... it crashes :(

Read the error message from the crash.

```text
FileNotFoundError: [Errno 2] No such file or directory: 'path_to_your_file/squirrel-data.csv'
```

The program needs you to update the path to the CSV file. Do that.
* [ChatGPT](https://chatgpt.com/): My CSV file is in the same directory as the program. Can you update the program to read from the current directory?
* Save it as `map_3.fixname.py` and run it
  * `python3 map_3.fixname.py`
* Oops... it crashes again :(

Read the error message from the crash.

```text
ValueError: Location values cannot contain NaNs.
```

Google for: `python what is nan`

NaN stands for 'Not a Number'. Look at the CSV file. Some of the records are missing the latitude or longitude values. Ask ChatGPT to add error handling.
* [ChatGPT](https://chatgpt.com/): Some of the records in my CSV file are missing latitude or longitude. Can you update the program to handle missing location data?
* Save it as `map_4.fixNaN.py` and run it
  * `python3 map_4.fixNaN.py`
* It worked!

Zoom out until you can see the whole world. Note that there is a sighting over near India. What's that!? Look in the data file. One of the records has coordinates in Asia. How did that happen? Look at the CSV data and find that one of the negative signs is missing.

How would you fix this error?
* Is it an error? Maybe someone saw a squirrel there.
* Edit the CSV file.
* Have the program ignore any coordinates outside of the NYC area.
* Other?

Let's try ignoring any coordinates outside of NYC.
* [ChatGPT](https://chatgpt.com/): This is working great. Thanks! Can you also ignore any coordinates that fall outside of the greater NYC area?
* Save it as `map_5.limitcoords.py` and run it
  * `python3 map_5.limitcoords.py`
* Did it work?

What other changes would you make? Can you think of how to describe what you want to ChatGPT?
