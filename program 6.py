import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv( '/kaggle/input/stores-area-and-sales-data/Stores.csv ')

# Summary Statistics
print(data.describe())

# univariate analysis
data[ 'Store_Sales '].hist(bins=20)
plt.title( ' Store Sales Distribution ')
plt.show()

data[ 'Daily_Customer_Count '].hist(bins=20)
plt.title( 'customer count  ')
plt.show()

# Bivariate Analysis
sns.scatterplot(x= 'Store_Sales ', y= 'Daily_Customer_Count ', data=data)
plt.title( 'Sales vs customer count ')
plt.show()

sns.heatmap(data.corr(), annot=True, cmap= 'coolwarm ')
plt.title( 'Correlation Matrix ')
plt.show()