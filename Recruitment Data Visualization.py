import matplotlib.pyplot as plt

companies = ['Microsoft','Google','Amazon','IBM','Amdocs']
recruitments = [120, 150, 180, 100, 90]

# a) Bar Chart
plt.bar(companies, recruitments)
plt.title("Recruitments in Companies")
plt.show()

# b) Pie Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

# c) Customized Pie Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%', explode=[0,0.1,0,0,0])
plt.title("Customized Pie Chart")
plt.show()

# d) Doughnut Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Doughnut Chart")
plt.show()

# Comparison: IBM vs Amdocs
plt.bar(['IBM','Amdocs'], [100,90])
plt.title("IBM vs Amdocs Recruitment")
plt.show()