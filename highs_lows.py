import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        high = int(row[1])
        highs.append(high)
        dates.append(current_date)
    

first_date = datetime.strptime('2014-1-1', '%Y-%m-%d')

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
fig.autofmt_xdate()

plt.title('Daily high temperatures, 2014', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()