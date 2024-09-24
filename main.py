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
import matplotlib.pyplot as plt
import requests

#api key
API_KEY = ''

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


# For loop to request API information on the exchange rate for the baseCurrency
# for the last 30 days in lastThirtyDays dictionary

for dateString, dateInfo in datesLastThirtyDays.items():
    year = dateInfo['year']
    month = dateInfo['month']
    day = dateInfo['day']

    fullURL = f'{url}{baseCurrency}/{year}/{month}/{day}'

    # API Request for each specific date
    response = requests.get(fullURL)
    data = response.json()

    # Check if request was successful and if we can access certain fields from the request
    # The API request returns a lot of information, and we only want to access the
    # 'conversion_rates' information for our exchangeCurrency
    if response.status_code == 200 and "conversion_rates" in data:
        #pull the specific exchange rate, in our case AUD
        rate = data['conversion_rates'].get(exchangeCurrency)
        if rate:
            # If we can get the rate, append the date and the AUD exchange rate to the list
            exchangeData.append({'date' : dateString, 'rate' : rate})
        else:
            print('No exchange rates available for ' + dateString)
    else:
        print('Failed to retrieve exchange rates ' + dateString)


# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(exchangeData)
print(df)

# I want to see the max conversion rate for the last 30 days, and the min for the last 30 days


# Gets the index, date, and rate for the corresponding max
maxRateIndex = df['rate'].idxmax()
maxRateDate = df.loc[maxRateIndex, 'date']
maxRateValue = df.loc[maxRateIndex, 'rate']

# Gets the index, date, and rate for the corresponding min val of 'rate'
minRateIndex = df['rate'].idxmin()
minRateDate = df.loc[minRateIndex, 'date']
minRateValue = df.loc[minRateIndex, 'rate']


print("Max rate:", maxRateValue, "on date:", maxRateDate)
print("Min rate:", minRateValue, "on date:", minRateDate)

#Plotting the Data
df.plot(x='date', y='rate')

#plt.axis(())
#plt.plot(df['Date'], df['Rate'])
#plt.show()
plt.scatter(minRateDate, minRateValue, color='blue', marker='o', label='Min Rate', zorder=3)
plt.scatter(maxRateDate, maxRateValue, color='red', marker='o', label='Max Rate', zorder=3)

plt.xlabel('Date')
plt.ylabel('Rate')

# Displays all dates with 45-degree rotation for readability
plt.xticks(df['date'], rotation=45)
plt.title(f'Exchange Rates between {baseCurrency} and {exchangeCurrency} for last 30 days')
#plt.plot((minRateDate, minRateValue), (maxRateDate, maxRateValue), marker='o', linestyle='none')
plt.show()

