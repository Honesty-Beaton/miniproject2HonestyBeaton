# INF601 - Advanced Programming in Python
# Honesty Beaton
# Mini Project 2
"""
 Using the Exchange Rate API and a PANDAS DataFrame to retrieve the
 exchange rate for the last 30 days (from the current day).
 Showcasing this information as a chart for the last 30 days.
"""
from calendar import month
from datetime import datetime, timedelta
import pandas as pd #pandas dataframe
import requests

#api key
API_KEY = 'ddb26c4e1d440ac62ce77fba'

#base URL for retrieving currency rate from API
url = 'https://v6.exchangerate-api.com/v6/' + API_KEY + '/history/'

# Base and exchange currencies with baseAmount of $1
baseCurrency = 'USD'
exchangeCurrency = 'AUD'
baseAmount = '1.00'

# Get the current date
currentDate = datetime.now().date()

# Dictionary to store the last 30 days worth of dates
datesLastThirtyDays = {}
for i in range(30):
    day = currentDate - timedelta(days=i)
    datesLastThirtyDays[str(day)] = {
        'year': day.year,
        'day' : day.day,
        'month': day.month
    }

# List to store dates and rates
exchangeData = []

# Testing to if API call is successful
#Current Year, Month and Day
currYear = datesLastThirtyDays[str(currentDate)]['year']
currMonth = datesLastThirtyDays[str(currentDate)]['month']
currDay = datesLastThirtyDays[str(currentDate)]['day']

fullURL = f'{url}{baseCurrency}/{currYear}/{currMonth}/{currDay}'

# API request
response = requests.get(fullURL)
data = response.json()

print(data)

# Check if request was successful and if we can access certain fields from the request
if response.status_code == 200 and "conversion_rates" in data:
    #pull the specific exchange rate, in our case AUD
    rate = data['conversion_rates'].get(exchangeCurrency)
    if rate:
        # If we can get the rate, append the date and the AUD exchange rate to the list
        exchangeData.append({'date' : currentDate, 'rate' : rate})
    else:
        print('No exchange rates available')
else:
    print('Failed to retrieve exchange rates')


# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(exchangeData)
print(df)

