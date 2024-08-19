import pandas as pd
import matplotlib.pyplot as plt
data={'year':list(range(2010,2021)),'Job posting':[150,300,450,600,800,1200,1600,2100,2700,3400,4200]}
df=pd.DataFrame(data)
plt.plot(df['year'],df['Job posting'],marker='o')
plt.title('Trend of data science job posting')
plt.xlabel('year')
plt.ylabel('number of job posting')
plt.show()
