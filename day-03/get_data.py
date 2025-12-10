import requests
import pandas as pd

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

