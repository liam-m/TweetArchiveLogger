import csv

username = 'jobbogamer'
csv_path = '/Users/Josh/Downloads/tweets/tweets.csv'
output_path = '/Users/Josh/Downloads/tweets.md.txt'

tweet_format = '''
{{text}}

[{{date}}]({{url}})

---

'''

date_format = '{{month}} {{day}}, {{year}} at {{hour_12}}:{{minute}}{{am}}'

base_url = 'http://twitter.com/' + username + '/status/'

def get_12_hour(hour):
	if int(hour) == 0 or int(hour) == 12:
		return '12'
	elif int(hour) > 12:
		h = str(int(hour) - 12)
		while len(h) < 2:
			h = '0' + h
		return h
	else:
		while len(hour) < 2:
			hour = '0' + hour
		return hour

def get_month(n):
	if n == 1:
		return "January"
	elif n == 2:
		return "February"
	elif n == 3:
		return "March"
	elif n == 4:
		return "April"
	elif n == 5:
		return "May"
	elif n == 6:
		return "June"
	elif n == 7:
		return "July"
	elif n == 8:
		return "August"
	elif n == 9:
		return "September"
	elif n == 10:
		return "October"
	elif n == 11:
		return "November"
	elif n == 12:
		return "December"

def format_date(date, format):
	year = date[:4]
	month = date[5:7]
	day = date[8:10]
	hour = date[11:13]
	minute = date[14:16]
	second = date[17:19]
	am = "AM" if int(hour) < 12 else "PM"
	hour12 = get_12_hour(hour)
	
	out = format
	out = out.replace("{{year}}", year)
	out = out.replace("{{month_num}}", month)
	out = out.replace("{{month}}", get_month(int(month)))
	out = out.replace("{{month_short}}", get_month(int(month))[0:3])
	out = out.replace("{{day}}", day)
	out = out.replace("{{hour}}", hour)
	out = out.replace("{{hour_12}}", get_12_hour(hour))
	out = out.replace("{{minute}}", minute)
	out = out.replace("{{second}}", second)
	out = out.replace("{{am}}", am)
	
	return out
	

def format_tweet(tweet, format):
	tweet_id = 0
	in_reply_to_status_id = 1
	in_reply_to_user_id = 2
	timestamp = 3
	source = 4
	text = 5
	retweeted_status_id = 6
	retweeted_status_user_id = 7
	retweeted_status_timestamp = 8
	expanded_urls = 9
	
	out = format
	out = out.replace("{{id}}", tweet[tweet_id])
	out = out.replace("{{date}}", format_date(tweet[timestamp], date_format))
	out = out.replace("{{text}}", tweet[text])
	out = out.replace("{{url}}", base_url + tweet[tweet_id])
	
	return out

output = ''

with open(csv_path, 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		if (row[0] != "tweet_id"):
			output += format_tweet(row, tweet_format)

output_file = open(output_path, 'wb')
output_file.write(output)