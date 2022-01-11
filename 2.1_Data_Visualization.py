#Steps invovlved in Data Visualization
# importing libraries
import seaborn as sns
import matplotlib.pyplot as plt

# setting a theme
sns.set_theme(style="ticks", color_codes=True)

# importing own or predefined data from lib
kashti = sns.load_dataset("titanic")
#print(kashti)

# plotting basic graph type1
p = sns.countplot(x ="sex", data= kashti) #countplot only takes one data variable
plt.show()

# plotting basic graph type2 with two variables
# we need to add hue(color) in this to represent two variables
# here p is defined as variable for plot
p = sns.countplot(x ="sex", data= kashti, hue="class") # coutplot only takes one variable
p.set_title("Junaid's first Data Plot")
plt.show()