# Extract data from a website using web scraping and request APIs process it using NumPy and Pandas libraries

import numpy as np
import pandas as pd

URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29" # Data source

# Extract the data
tables = pd.read_html(URL) # Extract tables from webpage using Pandas
df = tables[3] # Retain table 3 as the required dataframe
df.columns = range(df.shape[1]) # Replace the column headers with column numbers
df = df[[0,2]] # Retain columns with index 0 and 2 (name of country and value of GDP as quoted in the source)
df = df.iloc[1:11,:] # Retain the rows with index 1 to 10, indicating the top 10 economies of the world
df.columns = ['Country','GDP (Million USD)'] # Assign column names as "Country" and "GDP (Million USD)"

# Modify the data
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int) # Change the data type of the 'GDP (Million USD)' column to integer using astype()
df[['GDP (Million USD)']] = df[['GDP (Million USD)']]/1000 # Convert the GDP value in Million USD to Billion USD
df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']], 2) # Use numpy.round() to round the value to 2 decimal places
df.rename(columns = {'GDP (Million USD)' : 'GDP (Billion USD)'}) # Rename the column header from 'GDP (Million USD)' to 'GDP (Billion USD)'

# Load the dataframe to a csv file named "largest_economies.csv"
df.to_csv('./largest_economies.csv')
