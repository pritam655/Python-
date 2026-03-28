import pandas as pd
import matplotlib.pyplot as plt

# Sample data (you can replace with CSV file)
data = {
    'Month': ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    'Total_Profit': [211000,183300,224700,222700,209600,201400,295500,361400,234000,266700,412800,300200],
    'Facecream': [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900],
    'Facewash': [1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]
}

df = pd.DataFrame(data)

# a) Line Plot – Total Profit
plt.plot(df['Month'], df['Total_Profit'], marker='o')
plt.title("Total Profit Per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

# b) Multiline Plot – Product Sales
plt.plot(df['Month'], df['Facecream'], label='Face Cream')
plt.plot(df['Month'], df['Facewash'], label='Face Wash')
plt.legend()
plt.title("Product Sales Data")
plt.show()

# c) Bar Chart – Face Cream & Face Wash
plt.bar(df['Month'], df['Facecream'], label='Face Cream')
plt.bar(df['Month'], df['Facewash'], bottom=df['Facecream'], label='Face Wash')
plt.legend()
plt.title("Bar Chart - Product Sales")
plt.show()

# d) Pie Chart – Total Yearly Sales
total_sales = [df['Facecream'].sum(), df['Facewash'].sum()]
labels = ['Face Cream', 'Face Wash']

plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.title("Yearly Sales Distribution")
plt.show()