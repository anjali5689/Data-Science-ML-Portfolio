import matplotlib.pyplot as plt
import csv
import datetime
import matplotlib.dates as mdates
from collections import defaultdict

def visualize():
    mood_by_dates=defaultdict(list)
    with open('mood_info.csv','r') as mood_info:
        reader=csv.reader(mood_info)
        next(reader)
        
        for rows in reader:
            try:
                full_date=datetime.datetime.strptime(rows[0],"%Y-%m-%d %H:%M:%S")
                date_only=full_date.date()
                mood=int(rows[1])
                mood_by_dates[date_only].append(mood)
            except ValueError:
                continue
    dates=sorted(mood_by_dates.keys())
    avg_moods=[sum(mood_by_dates[d])/len(mood_by_dates[d]) for d in dates]
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, avg_moods, marker='o')
    plt.title("Daily Mood Summary")
    plt.xlabel("Date")
    plt.ylabel("Average Mood")
    plt.yticks([1, 2, 3, 4, 5], ['Very Sad', 'Sad', 'Neutral', 'Happy', 'Very Happy'])
    plt.xticks(dates, [d.strftime("%d-%b") for d in dates], rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
        


def daily_mood_summary():
    times = []
    moods = []
    with open('mood_info.csv', 'r') as mood_info:
        reader = csv.reader(mood_info)
        next(reader)
        specific_date=input('Please enter the date(YY-MM-DD): ')
        dt=datetime.datetime.strptime(specific_date,"%Y-%m-%d")

        for row in reader:
            try:
                row_time=datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S") 
                if row_time.date()==dt.date():
                    time_only=datetime.datetime.combine(dt,row_time.time()) 
                    times.append(time_only)
                    moods.append(int(row[1]))
            except ValueError:
                continue

    plt.figure(figsize=(10, 5))
    plt.plot(times, moods, marker='o')
    plt.title(f"Mood Changes on {dt}")
    plt.xlabel("Time")
    plt.ylabel("Mood")
    plt.grid(True)
    plt.yticks([1, 2, 3, 4, 5], ['Very Sad', 'Sad', 'Neutral', 'Happy', 'Very Happy'])
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%I:%M %p'))
    plt.gcf().autofmt_xdate() 
    plt.tight_layout()
    plt.show()
