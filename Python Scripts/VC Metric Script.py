import pandas as pd

# Read the data
df = pd.read_csv('1997-2023 United States Pre-Seed, Seed, and Series A Deals (Crunchbase) - 1997-2023 Pre-Seed, Seed, and Series A Deals.csv')

# Extract year from Announced Date
df['Year'] = pd.to_datetime(df['Announced Date']).dt.year

# Calculate Post-Money Valuation
df['Post-Money Valuation Currency (in USD)'] = df['Pre-Money Valuation Currency (in USD)'] + df['Money Raised Currency (in USD)']

# Group by Year and Funding Type
grouped = df.groupby(['Year', 'Funding Type'])

# Calculate averages
output = grouped['Money Raised Currency (in USD)', 'Pre-Money Valuation Currency (in USD)', 'Post-Money Valuation Currency (in USD)'].mean()

# Reset index for better output format
output = output.reset_index()

output.to_csv('VC Average Deal Metrics by Year.csv', index=False)

