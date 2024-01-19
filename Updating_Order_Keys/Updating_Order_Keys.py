
import pandas as pd

df_1 = pd.read_csv('CSV_Datasets_Orders/Oracle_Exported_Order_Dataset/1_orders.csv')
df_2 = pd.read_csv('CSV_Datasets_Orders/Oracle_Exported_Order_Dataset/2_orders.csv')

df = pd.concat([df_1, df_2])

df_sorted = df.sort_values(by='ORDER_ID')
df_sorted = df_sorted.reset_index(drop=True)

# Initialize ORDER_KEY with 1 for the first row
df_sorted['ORDER_KEYS'] = 1

# Iterate through the DataFrame to set ORDER_KEY based on the given logic
for i in range(1, len(df_sorted)):
    if df_sorted.at[i - 1, 'CUSTOMER_ID'] == df_sorted.at[i, 'CUSTOMER_ID']:
        df_sorted.at[i, 'ORDER_KEYS'] = df_sorted.at[i - 1, 'ORDER_KEYS']
    else:
        df_sorted.at[i, 'ORDER_KEYS'] = df_sorted.at[i - 1, 'ORDER_KEYS'] + 1

# Display the result
print(df_sorted[['ORDER_ID', 'ORDER_KEYS', 'CUSTOMER_ID']].head(25))

# This is just the Order of Columns I prefer.
df_sorted = df_sorted[['ORDER_ID', 'ORDER_KEYS', 'ORDER_DATE', 'SHIP_MODE', 'SHIP_DATE', 'CUSTOMER_ID',
       'POSTAL_ID', 'PRODUCT_ID', 'PRODUCT_PRICE_ID', 'PRODUCT_UNIT_PRICE',
       'PRODUCT_COST_PRICE', 'PRODUCT_DISCOUNT_PERCENTAGE',
       'PRODUCT_DISCOUNT_AMOUNT', 'PRODUCT_DISCOUNTED_UNIT_PRICE', 'QUANTITY',
       'TOTAL_DISCOUNT_AMOUNT', 'TOTAL_UNIT_AMOUNT',
       'GROSS_PROFIT_UNIT_AMOUNT', 'TOTAL_DISCOUNTED_UNIT_AMOUNT',
       'GROSS_PROFIT_DISCOUNTED_UNIT_AMOUNT']]

# Export to csv file called updated_orders.csv
# df_sorted.to_csv('updated_orders.csv', encoding='utf-8',  index=False)

full_df = pd.read_csv('updated_orders.csv')
full_df


