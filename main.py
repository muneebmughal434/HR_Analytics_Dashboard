import pandas as pd
import matplotlib.pyplot as plt

# Simulate sample HR data
data = {'department': ['Sales', 'HR', 'Tech'], 'attrition_rate': [0.25, 0.1, 0.15]}
df = pd.DataFrame(data)

plt.bar(df['department'], df['attrition_rate'])
plt.title('Attrition by Department')
plt.ylabel('Rate')
plt.show()