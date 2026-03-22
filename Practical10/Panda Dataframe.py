import pandas as pd

# Read the CSV file
df = pd.read_csv("books.csv")

# a) Print complete report in tabular form
print("\n--- Complete Book Report ---")
print(df)

# b) Print list of books by a given author
author_name = input("\nEnter author name: ")
author_books = df[df['Author'] == author_name]

print("\n--- Books by Author ---")
if not author_books.empty:
    print(author_books)
else:
    print("No books found for this author.")

# c) Print list of books by a given publishing house
publisher_name = input("\nEnter publishing house: ")
publisher_books = df[df['Publisher'] == publisher_name]

print("\n--- Books by Publisher ---")
if not publisher_books.empty:
    print(publisher_books)
else:
    print("No books found for this publisher.")

# d) Print titles of cheapest and costliest book
cheapest = df.loc[df['Price'].idxmin()]
costliest = df.loc[df['Price'].idxmax()]

print("\n--- Cheapest Book ---")
print(cheapest['Title'], "-", cheapest['Price'])

print("\n--- Costliest Book ---")
print(costliest['Title'], "-", costliest['Price'])

# e) Sort books based on year of publication
sorted_df = df.sort_values(by='Year')

print("\n--- Books Sorted by Year of Publication ---")
print(sorted_df)