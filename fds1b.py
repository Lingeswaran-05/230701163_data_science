import matplotlib.pyplot as plt
roles=['Data Analyst','Data science','Data engineer']
posting=[100,50,200]
plt.bar(roles,posting,width=0.2)
plt.title('Distribution of various data science role')
plt.xlabel('Job')
plt.ylabel('no of posting')
plt.show()
