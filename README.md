# Tweet Archive Logger

Python script which turns a Tweet Archive into a single, nicely-formatted Markdown file. Allows some (basic) custom formatting options.

At the moment, the output file contains the tweets in reverse chronological order, that is, the newest tweet at the top.

## Usage

### 1. Download your tweet archive
This can be done by going to the **Settings** page on the Twitter website, and clicking **Request your archive**. You'll get an email containing a download link for your archive. You'll need to unzip it once it's downloaded.

### 2. Change the script settings
At the top of `tweet_archive_logger.py`, there are five options you need to change for the script to work for you:
- `username` is your Twitter username, without the @ symbol.
- `csv_path` is the file path of the CSV file inside the tweet archive folder.
- `output_path` is the file path to the file you want to save the Markdown output into.
- `tweet_format` is the format each tweet should be in; see below for more info.
- `date_format` is the format timestamps should be changed into; see below for more info.

#### `tweet_format`
This is simply a string which gets replicated for each tweet in your archive. There are a few placeholders you can use which get replaced with data from the tweet:
- `id` is the long id number that Twitter gives each tweet.
- `date` is the date of the tweet, formatted according to `date_format`.
- `text` is the actual text of the tweet.
- `url` is the URL which points to the tweet on the Twitter website.
When you use a placeholder inside `tweet_format`, it must be surrounded with double curly braces.

Here is an example of `tweet_format`:
```
{{text}}

[{{date}}]({{url}})

---

```

The above formats a tweet like this:
```
Using tables for layout like it's 1996.

[March 31, 2014 at 09:36PM](http://twitter.com/jobbogamer/status/450748504517115905)

---

```

#### `date_format`
This is simply a string which gets replicated when you use the `{{date}}` placeholder. The date string itself is made up of a number of placeholders:
- `year` is the four digit year, e.g. `2014`.
- `month_num` is the month number with a leading zero, `01` through `12`.
- `month` is the month name, `January` through `December`.
- `month_short` is the first three letters of the month name, `Jan` through `Dec`.
- `day` is the day of the month with a leading zero, `01` through `31`.
- `hour` is the hour in 24-hour format with a leading zero, `00` through `23`.
- `hour_12` is the hour in 12-hour format with a leading zero, `01` through `12`.
- `minute` is the minute with a leading zero, `00` through `59`.
- `second` is the second with a leading zero, `00` through `59`.
- `am` is the AM/PM qualifier, either `AM` or `PM`.
When you use a placeholder inside `date_format`, it must be surrounded with double curly braces.

Here is an example of `date_format`:
```
{{day}} {{month}}, {{year}} at {{hour}}:{{minute}}{{am}}
```

The above formats a date like this:
```
March 31, 2014 at 09:36PM
```

### 3. Run the script
Now just run the script like you would any other Python script, either through your IDE or from the command line.

## Contributing
Feel free to fork, change things, and issue a pull request. This isn't a very robust script, and there aren't many formatting options at the moment.
