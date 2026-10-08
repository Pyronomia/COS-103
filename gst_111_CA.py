import pandas as pd

df = pd.read_csv("gst_111_CA.csv")
print(df)
print(df[df['Institution'] == 'Computing'])
computing_df = df[df['Institution'] == 'Computing']
# computing_df.to_excel('Computing GST 111 CA.xlsx', sheet_name='Sheet 1')