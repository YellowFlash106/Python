# # import os 

# # print('Current directory:', os.getcwd())

# # data_path = "../day-03/data/paris_weather.csv"
# # if os.path.exists(data_path):
# #     print(f"Found {data_path}")
# # else:
# #     print(f"Cannot found {data_path}")
# #     print("Make sure you're running from the sales-analysis folder")
          


# import pandas as pd
# import json
# import os

# # Read the CSV file
# df = pd.read_csv('data/sales.csv')
# print("CSV Data:")
# print(df)
# print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")

# # Quick operation: calculate total for each row
# df['total'] = df['quantity'] * df['price']
# print("\nWith totals:")
# print(df)

# # Create output directory
# os.makedirs('output', exist_ok=True)

# # Save as different formats
# # 1. JSON format (good for web APIs)
# df.to_json('output/sales_data.json', orient='records', indent=2)

# # 2. Excel format (good for sharing)
# df.to_excel('output/sales_data.xlsx', index=False)

# # 3. Updated CSV (with our new total column)
# df.to_csv('output/sales_with_totals.csv', index=False)

# print("\nFiles saved:")
# print("- output/sales_data.json")
# print("- output/sales_data.xlsx") 
# print("- output/sales_with_totals.csv")


import pandas as pd
from healpers import cal_total, format_currency

df = pd.read_csv('data/sales.csv')

totals = []
for i, r in df.iterrows():
    total = cal_total(r['quantity'], r['price'])
    totals.append(total)


df['total'] = totals

print("Sales Data:")
for i, r in df.iterrows():
    formatted_total = format_currency(r['total'])
    print(f"{r['product']}: {formatted_total}")


grand_total = df['total'].sum()
formatted_grand_total = format_currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")

