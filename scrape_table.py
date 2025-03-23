import pandas as pd
URL = 'https://en.wikipedia.org/wiki/List_of_the_most_common_passwords'
tables = pd.read_html(URL)
df = tables[1]
print(df)
