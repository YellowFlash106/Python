import requests
import os
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime, timedelta
# import pandas
# calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

start_date = week_ago.strftime('%Y-%m-%d')
end_date = today.strftime('%Y-%m-%d')
print(start_date)

# print(pd.__version__)

daily_data = data['daily']

df = pd.DataFrame({
    'date' : daily_data['time'],
    'max_temp':daily_data['temperature_2m_max'],
    'min_temp':daily_data['temperature_2m_min']
})
df['date'] = pd.to_datetime(df['date'])

print(df)


plt.figure(figsize=(10,6))
plt.plot(df['date'], df['max_temp'], marker='o', lable='Max temp')
plt.plot(df['date'], df['min_temp'], marker='o', lable='Min temp')

plt.xlable('Date')
plt.ylable('Tempretur(C)')
plt.title('Paris Wather - Past 7 days')
plt.legend()

plt.xticks(ratation=45)
plt.tight_layout()

plt.savefig('waether_chart.png')
plt.show()



#Save to CSV
if not os.path.exists('data'):
    os.makedirs('data')

df.to_csv('data/paris_weather.csv', index=False)
print('Data saves to Data/paris_weather.csv')