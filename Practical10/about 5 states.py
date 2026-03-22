import pandas as pd

# Creating DataFrame with 5 states data
data = {
    "State": ["Maharashtra", "Uttar Pradesh", "Bihar", "Rajasthan", "Madhya Pradesh"],
    "Area": [307713, 243286, 94163, 342239, 308252],   # in sq km
    "Population": [124000000, 240000000, 130000000, 81000000, 85000000]
}

df = pd.DataFrame(data)

# a) Print complete information
print("\n--- Complete State Information ---")
print(df)

# b) State with largest Area
largest_area_state = df.loc[df['Area'].idxmax(), 'State']
print("\nState with Largest Area:", largest_area_state)

# c) State with largest Population
largest_population_state = df.loc[df['Population'].idxmax(), 'State']
print("State with Largest Population:", largest_population_state)

# d) Calculate Population Density
df['Density'] = df['Population'] / df['Area']

print("\n--- Population Density of States ---")
print(df[['State', 'Density']])

# e) State with highest Population Density
highest_density_state = df.loc[df['Density'].idxmax(), 'State']
print("\nState with Highest Population Density:", highest_density_state)