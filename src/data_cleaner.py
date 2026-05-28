import pandas as pd


df_unclean = pd.read_csv('data/raw/cats_data_filtered.csv')
print('------------------------------------------------------------------')
print('unclean:')
df_unclean.info()

print('------------------------------------------------------------------')
print('clean:')
df_clean = df_unclean[(df_unclean['length_of_stay'].notna()) & (df_unclean['length_of_stay'] >= 0)]
df_clean.info()

# check for negative days
sorted_df = df_clean['length_of_stay'].sort_values()
print(sorted_df)

# make the cleaned dataframe into a csv, and put it into the cleaned data folder
df_clean.to_csv('data/clean/clean_cats_data.csv')