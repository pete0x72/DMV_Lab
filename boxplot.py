import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('football_players.csv')

df['Fee(£ mln)'] = df['Fee(£ mln)'].replace('[£]', '', regex=True)
df['Fee(£ mln)'] = df['Fee(£ mln)'].astype(float)

plt.figure()
plt.boxplot(df['Fee(£ mln)'])

plt.title('Boxplot of Transfer Fees')
plt.ylabel('Fee (Million £)')

plt.show()