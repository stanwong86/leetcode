import math
"""

One screen per movie
Repeat movie as many times as possible during hours of operation.
Movie cannot end after theather closing time before 12am

At open, 1 hour for setup.
35 minutes between shows
Schedule as late as possible
Rounded  to nearest 5. Round down?
24 hour format

There's Something About Mary, 1998, R, 2:14




Monday - Thursday 8:00am - 11:00pm
Friday - Sunday 10:30am - 11:30pm

closing time = max (12:00am - movie time) > latest operation time (11:00pm)

20:45 - 22:59pm
20:10 -  break
17:55 - 20:09 
17:20
15:05 - 17:19
12:15
11:40 - break
9:26 start
8am start 

"""


print('hi')


def read_file(filename):
	data = []
	with open(filename, 'r') as f:
		for line in f.read().split('\n'):
			row = line.split(',')
			# Movie Title, Release Year, Rating, Run Time
			data.append(row)

	return data


def convertTimeToMinutes(strTime):
	hours, minutes = strTime.split(':')
	return int(hours)*60 + int(minutes)


def getFormattedShowTimes(runTime, theaterStart, theaterEnd):
	runTime = convertTimeToMinutes(runTime)
	theaterStart = convertTimeToMinutes(theaterStart)
	theaterEnd = convertTimeToMinutes(theaterEnd)

	showTimes = []

	currentTime = theaterEnd
	while True:
		currentTime -= runTime

		startTime = currentTime = 5 * math.floor(currentTime / 5)

		if currentTime < theaterStart + 60:
			break

		endTime = startTime + runTime
		showTimes.insert(0, formatShowTimes(startTime, endTime))
		currentTime -= 35
	return showTimes

def intToStringTime(totalMinutes):
	minutes = totalMinutes % 60
	if minutes < 10:
		minutes = '0' + str(minutes)
	return f'{math.floor(totalMinutes/60)}:{str(minutes)}'

def formatShowTimes(startMinutes, endMinutes):
	return f'{intToStringTime(startMinutes)} - {intToStringTime(endMinutes)}'



movies = read_file('input.txt')

# TODAY = datetime.datetime.now().format('MM/DD/YYYY')
TODAY = '12/31/2015'

# 0 = Monday
theater_hours = [
	['Monday', '8:00', '23:00'],
	['Thursday', '10:30', '23:30']
]


for theater in theater_hours:
	print(f'{theater[0]} {TODAY}\n')

	for movie in movies[1:]:
		print(f'{movie[0]} - Rated {movie[2]}, {movie[3]}')

		times = getFormattedShowTimes(movie[3], theater[1], theater[2])
		for time in times:
			print(f'{time}')
		print()
