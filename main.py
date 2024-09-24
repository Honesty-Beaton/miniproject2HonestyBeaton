# INF601 - Advanced Programming in Python
# Honesty Beaton
# Mini Project 2
"""
 Using the Exchange Rate API and a PANDAS DataFrame to retrieve the
 exchange rate for the last 30 days (from the current day).
 Showcasing this information as a chart for the last 30 days.
"""

from datetime import timedelta
import pandas as pd #pandas dataframe
import requests
import datetime

#api key
API_KEY = ''
#base URL for retrieving currency pair from API
url = 'https://v6.exchangerate-api.com/v6/' + API_KEY + '/pair/'

# Base and exchange currencies
baseCurrency = 'USD'
exchangeCurrency = 'AUD'

#Gets the current date, day, month, and year
currentDate = datetime.date.today()
currentYear = currentDate.year
currentMonth = currentDate.month
currentDay = currentDate.day

#

# Dictionary to store the last 30 days worth of dates
datesLastThirtyDays = {}
for i in range(30):
    day = currentDate - timedelta(days=i)
    datesLastThirtyDays[str(day)] = {
        'year': day.year,
        'day' : day.day,
        'month': day.month
    }
    #datesLastThirtyDays.append(day)

for date_str, date_info in datesLastThirtyDays.items():
    print(f"Date: {date_str}, Year: {date_info['year']}, Month: {date_info['month']}, Day: {date_info['day']}")


fullURL = url + baseCurrency + '/' + exchangeCurrency + '/' #+ str(amount)


# Making the request
#response = requests.get(fullURL)
#data = response.json()
# print(data)

#dr = pd.DataFrame(
#    {}


#)